from django.db import models

# Create your models here.
CREATE TABLE Candidatos (
    candidato_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefono VARCHAR(15),
    direccion VARCHAR(255)
);

CREATE TABLE Departamentos (
    departamento_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

CREATE TABLE Puestos (
    puesto_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    vacantes INT NOT NULL,
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES Departamentos(departamento_id)
);

CREATE TABLE Contratos (
    contrato_id INT PRIMARY KEY AUTO_INCREMENT,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    candidato_id INT,
    puesto_id INT,
    salario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (candidato_id) REFERENCES Candidatos(candidato_id),
    FOREIGN KEY (puesto_id) REFERENCES Puestos(puesto_id)
);

CREATE TABLE Evaluaciones (
    evaluacion_id INT PRIMARY KEY AUTO_INCREMENT,
    contrato_id INT,
    fecha DATE NOT NULL,
    puntaje INT NOT NULL,
    comentarios TEXT,
    FOREIGN KEY (contrato_id) REFERENCES Contratos(contrato_id)
);
