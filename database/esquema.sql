CREATE DATABASE IF NOT EXISTS BushiCode;
USE BushiCode;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    nivel ENUM(
        'BRONCE-3', 'BRONCE-2', 'BRONCE-1',
        'PLATA-3', 'PLATA-2', 'PLATA-1',
        'ORO-3', 'ORO-2', 'ORO-1',
        'PLATINO-3', 'PLATINO-2', 'PLATINO-1',
        'DIAMANTE-3', 'DIAMANTE-2', 'DIAMANTE-1',
        'MAESTRO-3', 'MAESTRO-2', 'MAESTRO-1',
        'CODE-PREDATOR'	
    ) DEFAULT 'BRONCE-3',
    completo_quiz BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS registro_accesos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    fecha_entrada DATETIME NOT NULL,
    observacion TEXT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE IF NOT EXISTS progreso_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    hecho VARCHAR(100) NOT NULL,
    UNIQUE(usuario_id, hecho)
);