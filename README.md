# IS2-TP-Final

Este proyecto implementa clases para soportar servicios corporativos interactuando con DynamoDB para almacenar datos y logs.

## Estructura del Proyecto


### **`corporate_data.py`**
Este archivo contiene la clase `CorporateData`, que interactúa con DynamoDB para recuperar datos y ofrece los siguientes métodos:

- **`getData(uuid_session, uuidCPU, id)`**  
  Retorna una estructura JSON con los siguientes datos:
  - Id de sede
  - Domicilio
  - Localidad
  - Código Postal (cp)
  - Provincia  
  En caso de error, retorna un mensaje de error.

- **`getCUIT(uuid_session, uuidCPU, id)`**  
  Similar a `getData`, pero retorna el CUIT de la sede.

- **`getSeqID(uuid_session, uuidCPU, id)`**  
  Retorna un identificador único de secuencia (`idSeq`) que luego es incrementado en 1 en la base de datos.

- **`listCorporateData(id)`**  
  Lista todos los datos en la tabla `CorporateData` relacionados con una clave (id) específica.

- **`listCorporateLog(cpu_id)`**  
  Lista todas las entradas en la tabla `CorporateLog` para una CPU específica.

### **`corporate_log.py`**
Este archivo implementa la clase `CorporateLog` usando el patrón Singleton. Dentro de esta clase se inicializa otra clase llamada `Log`, que se utiliza para registrar eventos de auditoría.

- **`post(uuid_session, method_name)`**  
  Registra un evento en la tabla `CorporateLog` con los siguientes datos:
  - UUID de la sesión
  - Nombre del método que invoca el log
  - Información del sistema (CPU) donde está corriendo
  - Timestamp de la operación

- **`list(cpu_id, uuid_session=None)`**  
  Lista todas las entradas en la tabla `CorporateLog` relacionadas con una CPU. Si se proporciona un UUID de sesión, lista solo los logs de esa sesión.

### **Scripts**

- **`UADER_IS2_listCorporateData.py`**  
  Imprime los datos de la tabla `CorporateData`.

- **`UADER_IS2_listLog.py`**  
  Retorna una estructura JSON con todas las filas de la tabla `CorporateLog` donde el `uuidCPU` coincida con la CPU que utiliza para el desarrollo.

### **Pruebas Unitarias**

- **`test_corporate_data.py`**  
  Este archivo contiene pruebas que validan los métodos de `CorporateData`:
  - Prueba con un ID válido
  - Prueba con un ID inválido
  - Prueba con un ID vacío
  - Prueba para un ID válido pero con campos vacíos
  - Verificación del patrón Singleton

- **`test_corporate_log.py`**  
  Contiene pruebas que validan los métodos de `CorporateLog`:
  - Prueba del registro de un evento exitoso
  - Prueba de la lista de logs con un ID de CPU inválido
  - Verificación del patrón Singleton

## Dependencias

- Python 3.x
- `boto3`: Para interactuar con DynamoDB
- `botocore.exceptions`: Para manejar errores de conexión a AWS














