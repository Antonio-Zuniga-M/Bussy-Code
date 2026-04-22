from flask import Flask, render_template, send_file, request, redirect, url_for, session, jsonify, flash
import mysql.connector
from red_semantica import generar_imagen_red
from database.conexion import obtener_conexion
from preguntas import preguntas_quiz
from motor_inferencia import inferir_nivel

import rule_engine

from datetime import datetime

NIVELES_CATEGORIA = {
    'BRONCE-3': 'Básico', 'BRONCE-2': 'Básico', 'BRONCE-1': 'Básico',
    'PLATA-3': 'Intermedio', 'PLATA-2': 'Intermedio', 'PLATA-1': 'Intermedio',
    'ORO-3': 'Avanzado', 'ORO-2': 'Avanzado', 'ORO-1': 'Avanzado',
    'PLATINO-3': 'Avanzado', 'PLATINO-2': 'Avanzado', 'PLATINO-1': 'Avanzado',
    'DIAMANTE-3': 'Experto', 'DIAMANTE-2': 'Experto', 'DIAMANTE-1': 'Experto',
    'MAESTRO-3': 'Experto', 'MAESTRO-2': 'Experto', 'MAESTRO-1': 'Experto',
    'CODE-PREDATOR': 'Leyenda'
}

NIVELES_IMAGENES = {
    'BRONCE-3': 'you_re_tiering_me_apart_bronze_rs26.png',
    'BRONCE-2': 'you_re_tiering_me_apart_bronze_rs26.png',
    'BRONCE-1': 'you_re_tiering_me_apart_bronze_rs26.png',
    'PLATA-3': 'you_re_tiering_me_apart_silver_rs26.png',
    'PLATA-2': 'you_re_tiering_me_apart_silver_rs26.png',
    'PLATA-1': 'you_re_tiering_me_apart_silver_rs26.png',
    'ORO-3': 'you_re_tiering_me_apart_gold_rs26.png',
    'ORO-2': 'you_re_tiering_me_apart_gold_rs26.png',
    'ORO-1': 'you_re_tiering_me_apart_gold_rs26.png',
    'PLATINO-3': 'you_re_tiering_me_apart_platinum_rs26.png',
    'PLATINO-2': 'you_re_tiering_me_apart_platinum_rs26.png',
    'PLATINO-1': 'you_re_tiering_me_apart_platinum_rs26.png',
    'DIAMANTE-3': 'you_re_tiering_me_apart_diamond_rs26.png',
    'DIAMANTE-2': 'you_re_tiering_me_apart_diamond_rs26.png',
    'DIAMANTE-1': 'you_re_tiering_me_apart_diamond_rs26.png',
    'MAESTRO-3': 'you_re_tiering_me_apart_master_rs26.png',
    'MAESTRO-2': 'you_re_tiering_me_apart_master_rs26.png',
    'MAESTRO-1': 'you_re_tiering_me_apart_master_rs26.png',
    'CODE-PREDATOR': 'you_re_tiering_me_apart_apex_predator_rs26.png'
}

CURSOS_RECOMENDADOS = {
    'BRONCE-3': 'Hola Mundo - Variables',
    'BRONCE-2': 'Variables - Tipos de Datos',
    'BRONCE-1': 'Tipos de Datos - Operadores',
    'PLATA-3': 'Operadores - Condicionales',
    'PLATA-2': 'Condicionales - Ciclos',
    'PLATA-1': 'Ciclos - Listas',
    'ORO-3': 'Listas - Tuplas',
    'ORO-2': 'Tuplas - Diccionarios',
    'ORO-1': 'Diccionarios - Funciones',
    'PLATINO-3': 'Funciones - Scope',
    'PLATINO-2': 'Scope - Lambdas',
    'PLATINO-1': 'Lambdas - Manejo de Errores',
    'DIAMANTE-3': 'Manejo de Errores - Archivos',
    'DIAMANTE-2': 'Archivos - P.O.O.',
    'DIAMANTE-1': 'P.O.O. - Decoradores',
    'MAESTRO-3': 'Decoradores - Modules',
    'MAESTRO-2': 'Modules - APIs',
    'MAESTRO-1': 'APIs - Bases de Datos',
    'CODE-PREDATOR': 'Domina Python - Proyectos Avanzados'
}

app = Flask(__name__)
app.secret_key = 'bushicode_secreto_123' 

@app.route('/')
def inicio():
    return render_template('portada-maestra.html')

@app.route('/api/red-semantica')
def mostrar_red_semantica():
    imagen_en_memoria = generar_imagen_red()
    return send_file(imagen_en_memoria, mimetype='image/png')

"""
@app.route('/login')
def mostrar_login():
    return render_template('login.html')
"""

@app.route('/api/preguntas')
def api_preguntas():
    return jsonify(preguntas_quiz)

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        usuario = request.form.get("usuario")
        correo = request.form.get("correo")
        contrasena = request.form.get("contrasena")

        conexion = obtener_conexion()
        if conexion:
            cursor = None
            try:
                cursor = conexion.cursor()
                consulta = "insert into usuarios (nombre, usuario, correo, contrasena) values (%s, %s, %s, %s)"
                cursor.execute(consulta, (nombre, usuario, correo, contrasena))
                conexion.commit()

                session['usuario_id'] = cursor.lastrowid
                session['usuario_logeado'] = usuario
                session['nombre_completo'] = nombre
                session['nivel'] = None 
                session['usuario_creado'] = True
                return render_template('login.html', vista_activa='preguntas', usuario_creado=True)
                
            except mysql.connector.Error as error_:                
                return render_template('login.html', vista_activa='crear-usuario', error_registro="El usuario o correo ya existen. Intenta con otro.")
            finally:
                if cursor:
                    cursor.close()
                if conexion.is_connected():
                    conexion.close()
        return "Error al conectar con la base de datos."

@app.route('/logout')
def logout():
    session.clear() 
    return redirect(url_for('inicio'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario_html = request.form.get('usuario')
        contrasena_html = request.form.get('contrasena')
        
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            
            consulta = """
                SELECT * FROM usuarios 
                WHERE (usuario = %s OR correo = %s) AND contrasena = %s
            """
            cursor.execute(consulta, (usuario_html, usuario_html, contrasena_html))
            user_data = cursor.fetchone()
            
            if user_data:
                session['usuario_id'] = user_data['id']
                session['usuario_logeado'] = user_data['usuario']
                session['nombre_completo'] = user_data['nombre']
                session['nivel'] = user_data['nivel']
                
                from datetime import datetime 
                fecha_actual = datetime.now()
                cursor.execute("INSERT INTO registro_accesos (usuario_id, fecha_entrada) VALUES (%s, %s)", 
                               (user_data['id'], fecha_actual))
                conexion.commit()
                
                cursor.close()
                conexion.close()
                
                if not user_data['completo_quiz']:
                    return render_template('login.html', vista_activa='preguntas')
                else:
                    return redirect(url_for('ver_curso'))
            else:
                cursor.close()
                conexion.close()
                return render_template('login.html', vista_activa='login', error="Usuario, correo o contraseña incorrectos.")
                
    return render_template('login.html', vista_activa='login')

@app.route('/quiz/resultado', methods=['POST'])
def quiz_resultado():
    datos = request.get_json()
    respuestas_usuario = datos.get('respuestas', []) 
    
    resultado = inferir_nivel(respuestas_usuario)
    nivel_asignado = resultado["rango"]
    
    if 'usuario_id' in session:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                UPDATE usuarios 
                SET nivel = %s, completo_quiz = TRUE 
                WHERE id = %s
            """, (nivel_asignado, session['usuario_id']))
            conexion.commit()
            cursor.close()
            conexion.close()
            
            session['nivel'] = nivel_asignado 
    
    categoria = NIVELES_CATEGORIA.get(nivel_asignado, 'Desconocida')
    cursos = CURSOS_RECOMENDADOS.get(nivel_asignado, 'Cursos Avanzados')
    imagen = NIVELES_IMAGENES.get(nivel_asignado, 'you_re_tiering_me_apart_bronze_rs26.png')
    
    return jsonify({
        "nivel": nivel_asignado,
        "bloque": resultado["bloque"],
        "mensaje": "Diagnóstico completado.",
        "categoria": categoria,
        "cursos_recomendados": cursos,
        "imagen": f"/static/img/icons/{imagen}"
    })

@app.route('/cursos')
def ver_curso():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        
        cursor.execute("SELECT id, nombre, usuario, nivel FROM usuarios WHERE id = %s", 
                       (session['usuario_id'],))
        user_data = cursor.fetchone()
        
        cursor.execute("""
            SELECT COUNT(*) as total_entradas, MAX(fecha_entrada) as ultima_entrada
            FROM registro_accesos
            WHERE usuario_id = %s
        """, (session['usuario_id'],))
        accesos_data = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        
        if user_data and accesos_data:
            categoria_nivel = NIVELES_CATEGORIA.get(user_data['nivel'], 'Desconocido')
            ultima_entrada_formateada = accesos_data['ultima_entrada'].strftime('%d/%m/%Y %H:%M') if accesos_data['ultima_entrada'] else 'Nunca'
            
            return render_template('cursos.html', 
                                   nombre=user_data['nombre'],
                                   usuario=user_data['usuario'],
                                   usuario_id=user_data['id'],
                                   nivel=user_data['nivel'],
                                   categoria_nivel=categoria_nivel,
                                   total_entradas=accesos_data['total_entradas'],
                                   ultima_entrada=ultima_entrada_formateada)
    
    return "Error al cargar la información del usuario"

@app.route('/enviar_observacion', methods=['POST'])
def enviar_observacion():
    if 'usuario_id' in session:
        observacion = request.form.get('observacion')
        usuario_id = session['usuario_id']
        fecha_actual = datetime.now()
        
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO registro_accesos (usuario_id, fecha_entrada, observacion) 
                VALUES (%s, %s, %s)
            """, (usuario_id, fecha_actual, observacion))
            conexion.commit()
            cursor.close()
            conexion.close()
            
    return redirect(url_for('ver_curso'))

@app.route('/subir_nivel', methods=['POST'])
def subir_nivel():
    if 'usuario_id' not in session:
        return jsonify({'success': False, 'message': 'No autorizado'}), 401
        
    usuario_id = session['usuario_id']
    nuevo_nivel = request.form.get('nuevo_nivel')
    hecho_completado = f"Completó el curso {session.get('nivel')}"
    
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("UPDATE usuarios SET nivel = %s WHERE id = %s", (nuevo_nivel, usuario_id))
            cursor.execute("INSERT IGNORE INTO progreso_usuario (usuario_id, hecho) VALUES (%s, %s)", (usuario_id, hecho_completado))
            conexion.commit()
            session['nivel'] = nuevo_nivel # Actualizamos sesión
            return jsonify({'success': True, 'message': f'Nivel actualizado a {nuevo_nivel}'}), 200
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return jsonify({'success': False, 'message': 'Error en la base de datos'}), 500
        finally:
            cursor.close()
            conexion.close()
    
    return jsonify({'success': False, 'message': 'No se pudo conectar a la base de datos'}), 500

@app.route('/api/comentarios')
def api_comentarios():
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("""
            SELECT u.usuario, u.nivel, r.observacion, r.fecha_entrada
            FROM registro_accesos r
            JOIN usuarios u ON r.usuario_id = u.id
            WHERE r.observacion IS NOT NULL
            ORDER BY r.fecha_entrada DESC
            LIMIT 50
        """)
        registros = cursor.fetchall()
        cursor.close()
        conexion.close()
        
        comentarios = []
        for r in registros:
            obs = r['observacion']
            if '[Nivel:' in obs:
                partes = obs.split('] - ', 1)
                texto = partes[1] if len(partes) > 1 else obs
                nivel = partes[0].replace('[Nivel: ', '')
            else:
                texto = obs
                nivel = 'Desconocido'
            
            comentarios.append({
                'usuario': r['usuario'],
                'nivel': nivel,
                'texto': texto,
                'fecha': r['fecha_entrada'].strftime('%d/%m/%Y %H:%M') if r['fecha_entrada'] else 'Sin fecha'
            })
        
        return jsonify({'comentarios': comentarios})
    
    return jsonify({'comentarios': []})

@app.route('/guardar_comentario', methods=['POST'])
def guardar_comentario():
    if 'usuario_id' not in session:
        return jsonify({'success': False, 'error': 'No autenticado'}), 401

    usuario_id = session['usuario_id']
    comentario = request.form.get('comentario')
    nivel_curso = request.form.get('nivel_curso', 'Desconocido') 
    
    observacion_completa = f"[Nivel: {nivel_curso}] - {comentario}"
    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conexion = obtener_conexion()
    
    if conexion:
        try:
            cursor = conexion.cursor() 
            sql = """
                INSERT INTO registro_accesos (usuario_id, fecha_entrada, observacion) 
                VALUES (%s, %s, %s)
            """
            valores = (usuario_id, fecha_actual, observacion_completa)
            
            cursor.execute(sql, valores)
            conexion.commit() 
            cursor.close()
            
            return jsonify({'success': True, 'message': 'Comentario guardado'})
            
        except Exception as e:
            print(f"Error al guardar comentario: {e}")
            return jsonify({'success': False, 'error': str(e)}), 500
            
        finally:
            conexion.close()
    
    return jsonify({'success': False, 'error': 'Error de conexión'}), 500

if __name__ == '__main__':
    app.run(debug=True)
