    let preguntas = [];
    let indiceActual = 0;
    let respuestasUsuario = [];
    let seleccionActual = [];

    fetch('/api/preguntas')
        .then(response => response.json())
        .then(data => {
            preguntas = data;
            mostrarPregunta();
        });

function mostrarPregunta() {
    const q = preguntas[indiceActual];
    const hint = document.getElementById('hint-multiple');
    hint.style.display = (q.tipo === 'multiple') ? 'block' : 'none';

    seleccionActual = [];
    document.getElementById('texto-pregunta').innerText = 
        `Bloque ${q.bloque} - Pregunta ${indiceActual + 1}. ${q.pregunta}`;

    const contenedorOpciones = document.getElementById('contenedor-opciones');
    contenedorOpciones.innerHTML = ''; 
    const btnSiguiente = document.getElementById('btn-siguiente');
    
    btnSiguiente.style.display = 'block'; 
    btnSiguiente.classList.remove('habilitado');
    btnSiguiente.disabled = true;
    btnSiguiente.innerText = "Selecciona una opción";

    q.opciones.forEach((opcion, index) => {
        const boton = document.createElement('button');
        boton.className = 'opcion';
        boton.innerText = opcion;  
        boton.onclick = () => {
            if (q.tipo === 'single') {
                seleccionActual = [index];
                document.querySelectorAll('.opcion').forEach(b => b.classList.remove('opcion-seleccionada'));
                boton.classList.add('opcion-seleccionada');
            } else {
                const pos = seleccionActual.indexOf(index);
                if (pos === -1) {
                    seleccionActual.push(index);
                    boton.classList.add('opcion-seleccionada');
                } else {
                    seleccionActual.splice(pos, 1);
                    boton.classList.remove('opcion-seleccionada');
                }
            }

            if (seleccionActual.length > 0) {
                btnSiguiente.classList.add('habilitado');
                btnSiguiente.disabled = false;
                btnSiguiente.innerText = "Confirmar y Siguiente";
            } else {
                btnSiguiente.classList.remove('habilitado');
                btnSiguiente.disabled = true;
                btnSiguiente.innerText = "Selecciona una opción";
            }
        };
        contenedorOpciones.appendChild(boton);
    });  

}

function siguientePregunta() {
    respuestasUsuario.push([...seleccionActual]);
    indiceActual++;

    if (indiceActual < preguntas.length) {
        mostrarPregunta();
    } else {
        document.getElementById('caja-quiz').innerHTML = "<h2>Evaluando respuestas...</h2>";
        
        fetch('/quiz/resultado', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ respuestas: respuestasUsuario })
        })
            .then(res => res.json())
            .then(resultado => {
                document.getElementById('resultado-nivel').innerText = resultado.nivel;
                
                document.getElementById('resultado-categoria').innerText = resultado.categoria;
                
                document.getElementById('resultado-cursos').innerText = resultado.cursos_recomendados;
                
                const imagenNivel = document.getElementById('imagen-nivel');
                imagenNivel.src = resultado.imagen;
                imagenNivel.onerror = function() {
                    this.src = '/static/img/icons/default.png';
                };
                
                document.getElementById('resultado-bloque-nombre').innerText = resultado.bloque.replace('_', ' ');
                
                cambiarVistaLogin('resultado', true);
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById('caja-quiz').innerHTML = "<h2>Error al evaluar respuestas</h2>";
            });
    }
}

function cambiarVistaPortadaMaestra(vistaDestino) {
    document.getElementById('portada').classList.add('oculto');
    document.getElementById('red-semantica').classList.add('oculto');

    if (vistaDestino === 'portada') {
        document.getElementById('portada').classList.remove('oculto');
    } else if (vistaDestino === 'red-semantica') {
        document.getElementById('red-semantica').classList.remove('oculto'); 
    }
}

function cambiarVistaLogin(vistaDestino, limpiarErrores){
    document.getElementById('login').classList.add('oculto');
    document.getElementById('crear-usuario').classList.add('oculto');
    document.getElementById('preguntas').classList.add('oculto');
    document.getElementById('resultado').classList.add('oculto');

    if(vistaDestino == 'login'){
        document.getElementById('login').classList.remove('oculto');
    } else if(vistaDestino == 'crear-usuario'){
        document.getElementById('crear-usuario').classList.remove('oculto');
    } else if(vistaDestino == 'preguntas'){
        document.getElementById('preguntas').classList.remove('oculto');
    } else if(vistaDestino == 'resultado'){
        document.getElementById('resultado').classList.remove('oculto');
    }

    if (limpiarErrores == true){
        let listaErrores = document.querySelectorAll('.mensaje-error');
        for (let i = 0; i < listaErrores.length; i++) {
            listaErrores[i].remove(); 
        }
    }
}