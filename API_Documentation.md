# Documentación de la API - Reservas del Sistema de Lavado de Autos

## Endpoints para Reservas

http://localhost:5000

### 1. Obtener todas las reservas
- **Ruta**: `/reservas`
- **Método**: `GET`
- **Descripción**: Obtiene todas las reservas.

### 2. Obtener una reserva por ID
- **Ruta**: `/reservas/<id_reserva>`
- **Método**: `GET`
- **Descripción**: Obtiene una reserva específica por su ID.
- **Parámetros**:
  - `id_reserva`: ID de la reserva que se desea obtener.

### 3. Crear una nueva reserva
- **Ruta**: `/reservas`
- **Método**: `POST`
- **Descripción**: Crea una nueva reserva.
- **Cuerpo de la solicitud** (formato JSON):
  ```json
  {
      "nombre_cliente": "Juan Pérez",
      "celular_cliente": "12345678",
      "id_categoria": 1,
      "id_tipo_lavado": 2,
      "fecha_hora_reserva": "2024-09-28 14:00:00",
      "estado_reserva": "Pendiente",
      "lavado_motor": true
  }
### 4. Actualizar una reserva existente
- **Ruta**: `/reservas/<id_reserva>`
- **Método**: `PUT`
- **Descripción**: Actualiza una reserva existente.
    ```json
    {
        "nombre_cliente": "Juan Pérez",
        "celular_cliente": "87654321",
        "id_categoria": 1,
        "id_tipo_lavado": 2,
        "fecha_hora_reserva": "2024-09-28 15:00:00",
        "estado_reserva": "Confirmada",
        "lavado_motor": false
    }

### 5. Eliminar una reserva
- **Ruta**: `/reservas/<id_reserva>`
- **Método**: `DELETE`
- **Descripción**: Elimina una reserva específica por su ID.
- **Parámetros**:
  - `id_categoria`: ID de la reserva que se desea eliminar.

## Endpoints para Categorías

### 1. Obtener todas las categorías
- **Ruta**: `/categorias`
- **Método**: `GET`
- **Descripción**: Obtiene todas las categorías de vehículos.

### 2. Obtener una categoría por ID
- **Ruta**: `/categorias/<id_categoria>`
- **Método**: `GET`
- **Descripción**: Obtiene una categoría específica por su ID.
- **Parámetros**:
  - `id_categoria`: ID de la categoría que se desea obtener.

### 3. Crear una nueva categoría
- **Ruta**: `/categorias`
- **Método**: `POST`
- **Descripción**: Crea una nueva categoría de vehículo.
- **Cuerpo de la solicitud** (formato JSON):
  ```json
  {
      "tipo": "M",
      "precio_base": 30.00
  }

### 4. Actualizar una categoría existente
- **Ruta**: `/categorias/<id_categoria>`
- **Método**: `PUT`
- **Descripción**: Actualiza una categoría existente.
- **Parámetros**:
    `id_categoria: ID de la categoría que se desea actualizar.`
    ```json
    {
    "tipo": "M",
    "precio_base": 35.00
    }

### 5. Eliminar una categoría
- **Ruta**: `/categorias/<id_categoria>`
- **Método**: `DELETE`
- **Descripción**: Elimina una categoría específica por su ID.
- **Parámetros**:
  - `id_categoria`: ID de la categoría que se desea eliminar.


## Endpoints para Tipos de Lavado

### 1. Obtener todos los tipos de lavado
- **Ruta**: `/tipolavado`
- **Método**: `GET`
- **Descripción**: Obtiene todos los tipos de lavado.

### 2. Obtener un tipo de lavado por ID
- **Ruta**: `/tipolavado/<id_tipo_lavado>`
- **Método**: `GET`
- **Descripción**: Obtiene un tipo de lavado específico por su ID.
- **Parámetros**:
  - `id_tipo_lavado`: ID del tipo de lavado que se desea obtener.

### 3. Crear un nuevo tipo de lavado
- **Ruta**: `/tipolavado`
- **Método**: `POST`
- **Descripción**: Crea un nuevo tipo de lavado.
- **Cuerpo de la solicitud** (formato JSON):
  ```json
  {
      "descripcion": "Lavado y aspirado",
      "costo_adicional": 10
  }

### 4. Actualizar un tipo de lavado existente
- **Ruta**: `/tipolavado/<id_tipo_lavado>`
- **Método**: `PUT`
- **Descripción**: Actualiza un tipo de lavado existente.
- **Parámetros**:
    `id_tipo_lavado: ID del tipo de lavado que se desea actualizar.`
    ```json
    {
    "descripcion": "Lavado completo",
    "costo_adicional": 100
    }

### 5. Eliminar un tipo de lavado
- **Ruta**: `/tipolavado/<id_tipo_lavado>`
- **Método**: `DELETE`
- **Descripción**: Elimina un tipo de lavado específico por su ID.
- **Parámetros**:
  - `id_tipo_lavado: ID del tipo de lavado que se desea eliminar.`
