from flask import Flask, render_template, send_file
from red_semantica import generar_imagen_red

app = Flask(__name__)
app.secret_key = 'bushicode_secreto_123' 

@app.route('/')
def inicio():
    return render_template('portada-maestra.html')

@app.route('/api/red-semantica')
def mostrar_red_semantica():
    imagen_en_memoria = generar_imagen_red()
    return send_file(imagen_en_memoria, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
