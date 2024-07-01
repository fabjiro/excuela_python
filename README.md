# Flask API Clean Architecture

## Configuración

1. Crear y activar el entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

2. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3. Configurar las variables de entorno en un archivo `.env`:
    ```plaintext
    SECRET_KEY=your_secret_key
    ```

4. Inicializar la base de datos:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Ejecutar la aplicación:
    ```bash
    python run.py
    ```

## Rutas

- `POST /register`: Registro de un nuevo usuario.
- `POST /login`: Login de usuario y generación de JWT.
- `GET /user`: Obtener información del usuario autenticado.
- `PUT /user`: Actualizar información del usuario autenticado.
- `DELETE /user`: Eliminar la cuenta del usuario autenticado.

## Pruebas

Para ejecutar las pruebas:
    ```bash
    pytest
    ```
