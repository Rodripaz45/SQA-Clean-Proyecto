-- SQL Database Creation for Auto Wash Reservation System

-- Use or create the database (adjust the database name as needed)
CREATE DATABASE IF NOT EXISTS AutoWashDB;
USE AutoWashDB;

-- Creating table for Vehicle Categories
CREATE TABLE IF NOT EXISTS CategoriasVehiculos (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('S', 'M', 'L', 'XL') NOT NULL,
    precio_base DECIMAL(5, 2) NOT NULL
);

-- Inserting vehicle categories into CategoriasVehiculos
INSERT INTO CategoriasVehiculos (tipo, precio_base) VALUES
('S', 40.00),
('M', 60.00),
('L', 80.00),
('XL', 100.00);

-- Creating table for Washing Types
CREATE TABLE IF NOT EXISTS TipoLavado (
    id_tipo_lavado INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL,
    costo_adicional DECIMAL(5, 2) NOT NULL
);

-- Inserting washing types into TipoLavado
INSERT INTO TipoLavado (descripcion, costo_adicional) VALUES
('Lavado normal (lavado)', 0),
('Lavado y aspirado', 10),
('Lavado, aspirado y encerado', 20),
('Lavado completo (lavado, aspirado, encerado, motor, sacada de asientos)', 100);

-- Creating table for Reservations
CREATE TABLE IF NOT EXISTS Reservas (
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    nombre_cliente VARCHAR(255) NOT NULL,
    celular_cliente CHAR(8) NOT NULL,
    id_categoria INT NOT NULL,
    id_tipo_lavado INT NOT NULL, 
    fecha_hora_reserva DATETIME NOT NULL,  -- Combina fecha y hora en un solo campo
    estado_reserva ENUM('Confirmada', 'Pendiente', 'Cancelada') NOT NULL,
    precio_total DECIMAL(7, 2) NOT NULL DEFAULT 0,
    lavado_motor BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (id_categoria) REFERENCES CategoriasVehiculos(id_categoria),
    FOREIGN KEY (id_tipo_lavado) REFERENCES TipoLavado(id_tipo_lavado)
);


-- Creating table for Administrators
CREATE TABLE IF NOT EXISTS Administradores (
    id_admin INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);