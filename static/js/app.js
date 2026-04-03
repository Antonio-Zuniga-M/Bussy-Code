function cambiarVista(vistaDestino) {
    document.getElementById('portada').classList.add('oculto');
    document.getElementById('red-semantica').classList.add('oculto');

    if (vistaDestino === 'portada') {
        document.getElementById('portada').classList.remove('oculto');
    } else if (vistaDestino === 'red-semantica') {
        document.getElementById('red-semantica').classList.remove('oculto'); 
    }
}