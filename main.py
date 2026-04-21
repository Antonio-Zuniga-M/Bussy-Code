from flask import Flask, render_template, send_file, request, redirect, url_for, session, jsonify
import mysql.connector
from red_semantica import generar_imagen_red
from database.conexion import obtener_conexion
from preguntas import preguntas_quiz
from motor_inferencia import inferir_nivel


from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime


from datetime import datetime

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
                return render_template('login.html', vista_activa='preguntas')
                #redirect?
                
            except mysql.connector.Error as error_:                
                return render_template('login.html', vista_activa='crear-usuario', error_registro="El usuario o correo ya existen. Intenta con otro.")
            finally:
                if cursor:
                    cursor.close()
                if conexion.is_connected():
                    conexion.close()
        return "Error al conectar con la base de datos."

"""
@app.route('/quiz/resultado', methods=['POST'])
def quiz_resultado():
    datos = request.get_json()
    respuestas_usuario = datos.get('respuestas', []) 
    resultado = inferir_nivel(respuestas_usuario)
    return jsonify({
        "nivel": resultado["rango"],
        "bloque": resultado["bloque"],
        "mensaje": "Diagnóstico completado."
    })
"""
@app.route('/logout')
def logout():
    session.clear() 
    return redirect(url_for('inicio'))
























# ... (Tus otras importaciones de red_semantica, motor_inferencia, etc.) ...

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 1. Recibimos los datos del formulario
        usuario_html = request.form.get('usuario')
        contrasena_html = request.form.get('contrasena')
        
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            
            # 2. Buscamos por ID de usuario O por correo
            consulta = """
                SELECT * FROM usuarios 
                WHERE (usuario = %s OR correo = %s) AND contrasena = %s
            """
            # Pasamos usuario_html dos veces para que busque en ambas columnas
            cursor.execute(consulta, (usuario_html, usuario_html, contrasena_html))
            user_data = cursor.fetchone()
            
            if user_data:
                # 3. Si los datos son correctos, guardamos la sesión
                session['usuario_id'] = user_data['id']
                session['usuario_logeado'] = user_data['usuario']
                session['nombre_completo'] = user_data['nombre']
                session['nivel'] = user_data['nivel']
                
                # 4. Registramos el acceso en la base de datos
                from datetime import datetime # Asegúrate de que esto esté al inicio de tu archivo main.py
                fecha_actual = datetime.now()
                cursor.execute("INSERT INTO registro_accesos (usuario_id, fecha_entrada) VALUES (%s, %s)", 
                               (user_data['id'], fecha_actual))
                conexion.commit()
                
                cursor.close()
                conexion.close()
                
                # 5. Redirección dependiendo del progreso
                if not user_data['completo_quiz']:
                    # Si no ha hecho el quiz, lo dejamos en login.html pero mostramos las preguntas
                    return render_template('login.html', vista_activa='preguntas')
                else:
                    # Si ya lo hizo, lo mandamos directo a cursos
                    return redirect(url_for('ver_curso'))
            else:
                cursor.close()
                conexion.close()
                # Si fallan las credenciales, recargamos el login con un error
                return render_template('login.html', vista_activa='login', error="Usuario, correo o contraseña incorrectos.")
                
    return render_template('login.html', vista_activa='login')

@app.route('/quiz/resultado', methods=['POST'])
def quiz_resultado():
    datos = request.get_json()
    respuestas_usuario = datos.get('respuestas', []) 
    
    # Tu motor de inferencia saca el rango
    resultado = inferir_nivel(respuestas_usuario)
    nivel_asignado = resultado["rango"]
    
    # Guardarlo en la base de datos
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
            
            session['nivel'] = nivel_asignado # Actualizamos la sesión
            
    return jsonify({
        "nivel": nivel_asignado,
        "bloque": resultado["bloque"],
        "mensaje": "Diagnóstico completado."
    })

# --- NUEVAS RUTAS PARA EL CURSO ---

@app.route('/cursos')
def ver_curso():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    # Pasamos las variables de sesión al HTML
    return render_template('cursos.html', 
                           nombre=session.get('nombre_completo'), 
                           nivel=session.get('nivel'))

@app.route('/enviar_observacion', methods=['POST'])
def enviar_observacion():
    if 'usuario_id' in session:
        observacion = request.form.get('observacion')
        usuario_id = session['usuario_id']
        fecha_actual = datetime.now()
        
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            # Registramos la observación
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
    # Esta ruta se llama cuando pasan el examen final de un módulo
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
        
    usuario_id = session['usuario_id']
    nuevo_nivel = request.form.get('nuevo_nivel')
    hecho_completado = f"Completó el curso {session.get('nivel')}"
    
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            # 1. Actualizar rango en usuarios
            cursor.execute("UPDATE usuarios SET nivel = %s WHERE id = %s", (nuevo_nivel, usuario_id))
            # 2. Registrar en progreso_usuario (usamos IGNORE por si ya lo había pasado)
            cursor.execute("INSERT IGNORE INTO progreso_usuario (usuario_id, hecho) VALUES (%s, %s)", (usuario_id, hecho_completado))
            conexion.commit()
            session['nivel'] = nuevo_nivel # Actualizamos sesión
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conexion.close()
            
    return redirect(url_for('ver_curso'))


# Importa aquí tu conector de base de datos (pymysql, mysql.connector, etc.)

@app.route('/guardar_comentario', methods=['POST'])
def guardar_comentario():
    # 1. Verificar sesión
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    # 2. Capturar datos del HTML
    usuario_id = session['usuario_id']
    comentario = request.form.get('comentario')
    nivel_curso = request.form.get('nivel_curso', 'Desconocido') 
    
    observacion_completa = f"[Nivel: {nivel_curso}] - {comentario}"
    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 3. Abrir conexión a la BD (¡Esto faltaba!)
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
            
        except Exception as e:
            print(f"Error al guardar comentario: {e}")
            
        finally:
            conexion.close() # Siempre es buena práctica cerrar la conexión al terminar
            
    # 4. Redirigir usando el nombre exacto de tu función principal (ver_curso)
    return redirect(url_for('ver_curso'))

if __name__ == '__main__':
    app.run(debug=True)
