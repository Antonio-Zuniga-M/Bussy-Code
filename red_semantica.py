import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io

def generar_imagen_red():
    G = nx.DiGraph()
    
    # --- 1. EL TRUCO: ORDENAMIENTO FORZADO ---
    # Al ingresar los nodos en este orden estricto (de izquierda a derecha), 
    # evitamos que NetworkX los revuelva y cruce las líneas.
    nodos_ordenados = [
        # Raíz (Nivel 0)
        "Bushicode",
        
        # Ramas Principales (Nivel 1)
        "programación", "Modelo_dominio", "Modelo_estudiante", "Modelo_pedagogico", "Modelo_evaluacion", "python",
        
        # Sub-ramas (Nivel 2) ordenadas según su padre
        "temario", "banco de ejercicios", # De Modelo Dominio
        "Errores frecuentes", "progreso", "nivel", "Perfil_de_aprendizaje", # De Modelo Estudiante
        "Que enseñar", "dificultad", "gamification", "retroalimentacion", # De Modelo Pedagogico
        "Salida esperada", "Lógica del programa", "Código del estudiante", "Errores sintácticos", # De Modelo Evaluacion
        
        # Detalles finales (Nivel 3) ordenados justo debajo de sus padres
        "ciclos", "condicionales", "funciones", "variables", "listas", # De Temario
        "retos", "Opcion multiple", "Correccion de errores", "Codigo incompleto", # De Banco de ejercicios
        "Ruta personalizada", # De Perfil de aprendizaje
        "xp", "niveles", "motivacion", # De Gamification
        "positiva", "correctiva" # De Retroalimentacion
    ]
    
    # Agregamos los nodos primero para fijar su orden horizontal
    G.add_nodes_from(nodos_ordenados)

    # Definimos y agregamos las relaciones
    relaciones = [
        ("Bushicode", "programación", "enseña"),
        ("Bushicode", "python", "incluye"),
        ("Bushicode", "Modelo_dominio", "tiene"),
        ("Bushicode", "Modelo_estudiante", "tiene"),
        ("Bushicode", "Modelo_pedagogico", "tiene"),
        ("Bushicode", "Modelo_evaluacion", "incluye"),
        ("Modelo_dominio", "temario", "contiene"), 
        ("Modelo_dominio", "banco de ejercicios", "contiene"), 
        ("temario", "ciclos", "incluye"),
        ("temario", "condicionales", "incluye"),
        ("temario", "funciones", "incluye"),
        ("temario", "variables", "incluye"),
        ("temario", "listas", "incluye"),
        ("banco de ejercicios", "retos", "incluye"),
        ("banco de ejercicios", "Opcion multiple", "incluye"),
        ("banco de ejercicios", "Correccion de errores", "incluye"),
        ("banco de ejercicios", "Codigo incompleto", "incluye"),
        ("Modelo_estudiante", "Errores frecuentes", "almacena"),
        ("Modelo_estudiante", "progreso", "almacena"),
        ("Modelo_estudiante", "nivel", "almacena"),
        ("Modelo_estudiante", "Perfil_de_aprendizaje", "genera"),
        ("Perfil_de_aprendizaje", "dificultad", "determina"),
        ("Perfil_de_aprendizaje", "Ruta personalizada", "ajusta"),
        ("Modelo_pedagogico", "Que enseñar", "decide"),
        ("Modelo_pedagogico", "dificultad", "adapta"),
        ("Modelo_pedagogico", "gamification", "activa"),
        ("Modelo_pedagogico", "retroalimentacion", "genera"),
        ("gamification", "xp", "otorga"),
        ("gamification", "niveles", "desbloquea"),
        ("gamification", "motivacion", "mantiene"),
        ("retroalimentacion", "positiva", "puede ser"),
        ("retroalimentacion", "correctiva", "puede ser"),
        ("Modelo_evaluacion", "Salida esperada", "compara"),
        ("Modelo_evaluacion", "Lógica del programa", "evalua"),
        ("Modelo_evaluacion", "Código del estudiante", "analiza"),
        ("Modelo_evaluacion", "Errores sintácticos", "detecta")
    ]

    #for origen, destino, relacion in relaciones:
        #G.add_edge(origen, destino, label=relacion)
    
    # CÓDIGO MODIFICADO
    for origen, destino, relacion in relaciones:
        # Intercambiamos origen por destino para que la flecha apunte al padre
        G.add_edge(destino, origen, label=relacion)

    # --- 2. ORDENAMIENTO Y ESPACIADO ---
    for nodo in G.nodes():
        try:
            #nivel = nx.shortest_path_length(G, "Bushicode", nodo)
            # CÓDIGO MODIFICADO
            # Calculamos la distancia de cada nodo HACIA "Bushicode"
            nivel = nx.shortest_path_length(G, nodo, "Bushicode")
        except nx.NetworkXNoPath:
            nivel = 0 
        G.nodes[nodo]['layer'] = nivel

    pos = nx.multipartite_layout(G, subset_key="layer", align="horizontal")

    # Invertimos el eje Y (raíz arriba) y estiramos el eje X (horizontal) para que respiren los nodos
    for nodo in pos:
        pos[nodo][1] = -pos[nodo][1] 
        pos[nodo][0] = pos[nodo][0] * 3.5 

    # --- 3. DISEÑO VISUAL ---
    plt.figure(figsize=(32, 16), facecolor="#F8F9FA")

    colores_niveles = {
        0: "#F1C40F", # Amarillo principal
        1: "#3498DB", # Azul principal
        2: "#2ECC71", # Verde subtemas
        3: "#E74C3C", # Rojo detalles
        4: "#9B59B6"  # Morado extra
    }

    # Flechas un poco más sutiles en su curva (rad=0.03) para que no hagan "moños" extraños
    nx.draw_networkx_edges(
        G, pos, 
        arrows=True, arrowsize=18, edge_color="#95A5A6", width=1.5,
        connectionstyle="arc3,rad=0.03", node_size=4000
    )

    for nodo, (x, y) in pos.items():
        nivel_nodo = G.nodes[nodo].get('layer', 0)
        color_fondo = colores_niveles.get(nivel_nodo, "#BDC3C7") 
        
        plt.text(
            x, y, nodo, 
            fontsize=11, fontweight='bold', color='black',
            ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.5", ec="black", fc=color_fondo, lw=1.5)
        )

    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(
        G, pos, 
        edge_labels=edge_labels, font_size=9, font_color="#C0392B", font_weight="bold",
        bbox=dict(boxstyle="round,pad=0.1", ec="none", fc="#F8F9FA", alpha=0.9) 
    )

    plt.title("Red Semántica - Bushicode Project", fontsize=28, fontweight="bold", color="#2C3E50", pad=20)
    plt.axis("off") 
    plt.tight_layout()

    # --- 4. EXPORTACIÓN ---
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=120, facecolor="#F8F9FA") 
    img.seek(0)
    plt.close()

    return img