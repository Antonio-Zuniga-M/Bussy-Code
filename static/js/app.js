function cambiarVistaPortadaMaestra(vistaDestino) {
    document.getElementById('portada').classList.add('oculto');
    document.getElementById('red-semantica').classList.add('oculto');

    if (vistaDestino === 'portada') {
        document.getElementById('portada').classList.remove('oculto');
    } else if (vistaDestino === 'red-semantica') {
        document.getElementById('red-semantica').classList.remove('oculto'); 
    }
}

function cambiarVistaLogin(vistaDestino){
    document.getElementById('login').classList.add('oculto');
    document.getElementById('crear-usuario').classList.add('oculto');
    document.getElementById('preguntas').classList.add('oculto');

    if(vistaDestino == 'login'){
        document.getElementById('login').classList.remove('oculto');
    } else if(vistaDestino == 'crear-usuario'){
        document.getElementById('crear-usuario').classList.remove('oculto');
    } else if(vistaDestino == 'preguntas')
        document.getElementById('preguntas').classList.remove('oculto');
}