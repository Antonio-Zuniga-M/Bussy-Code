from flask import Flask, render_template, send_file, request, redirect, url_for, session, jsonify
import mysql.connector
from red_semantica import generar_imagen_red
from database.conexion import obtener_conexion
from preguntas import preguntas_quiz
from motor_inferencia import inferir_nivel

app = Flask(__name__)
app.secret_key = 'bushicode_secreto_123' 

@app.route('/')
def inicio():
    return render_template('portada-maestra.html')

@app.route('/api/red-semantica')
def mostrar_red_semantica():
    imagen_en_memoria = generar_imagen_red()
    return send_file(imagen_en_memoria, mimetype='image/png')

@app.route('/login')
def mostrar_login():
    return render_template('login.html')

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

@app.route('/logout')
def logout():
    session.clear() 
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)
