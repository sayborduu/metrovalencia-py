# Manejo de Excepciones

El SDK define tipos de excepciones para manejar los errores de la API. 

## Jerarquía de Excepciones

```
MetroAPIError (Base principal)
├── AuthError           # 401 - Fallo de llave de API
├── NotFoundError        # 404 - Recursos no encontrado
├── RateLimitError       # 429 - Límite de peticiones sobrepasado
├── ServiceUnavailable   # 503 - Problemas de conexión a MetroValencia
└── InvalidUserAgent     # 400 - User-Agent inválido o erróneo

MissingContactError     # Ocurre cuando falta contacto o app_name al inicio
```

## Excepciones Notables

### MetroAPIError

Excepción base de la red y API.

```python
from metrovalencia import exceptions

try:
    # Operación de red API
    pass
except exceptions.MetroAPIError as e:
    print(f"Error: {e.message}")
    print(f"Código HTTP: {e.status_code}")
```

### AuthError

Cuando falta la autorización provista por la API (HTTP 401).

```python
from metrovalencia import exceptions

try:
    metro = MetroValencia(
        app_name="miapp",
        contact="dev@ejemplo.com",
        api_key="api_key_erronea_o_eliminada"
    )
except exceptions.AuthError as e:
    print(f"Error de credenciales: {e}")
```

### NotFoundError

Se ha requerido de un endpoint o recurso inexistente en el servidor (HTTP 404).

```python
try:
    result = metro.previsiones.get(99999)  # ID inexistente
except exceptions.NotFoundError as e:
    print(f"Error de búsqueda: {e}")
```

### RateLimitError

La API restringe el número excesivo de peticiones (HTTP 429).

```python
try:
    # Operación o iteración rápida de peticiones...
    pass
except exceptions.RateLimitError as e:
    print(f"Pausando cliente, rate-limit: {e}")
    if e.retry_after:
        print(f"Espera sugerida: {e.retry_after}s")
```

**Información adicional:**
- `retry_after` (int): Segundo devueltos por cabecera de la API, recomendación a seguir en espera.

### ServiceUnavailable

El servidor de MetroValencia se encuentra fuera de línea o inaccesible (HTTP 503).

```python
try:
    pass
except exceptions.ServiceUnavailable as e:
    print(f"Servidor en mantenimiento o no accesible: {e}")
```

### InvalidUserAgent

Se ha entregado información insuficiente o irreconocible para el User-Agent (HTTP 400).

```python
try:
    pass
except exceptions.InvalidUserAgent as e:
    print(f"Agente incompatible en cabecera: {e}")
```

### MissingContactError

Ocurre si intentas inicializar al cliente falto del email / User-Agent.

```python
from metrovalencia import exceptions

try:
    # Sin app_name ni contact
    metro = MetroValencia()
except exceptions.MissingContactError as e:
    print(f"Error: {e}")
    # Salida: "User-Agent is required. Provide either 'user_agent' or ('app_name' + 'contact') on init."
```

---

## Ejemplo Completo de Manejo de Errores

```python
from metrovalencia import MetroValencia, exceptions

def obtener_previsiones(parada: str):
    try:
        metro = MetroValencia(
            app_name="miapp",
            contact="dev@ejemplo.com"
        )

        result = metro.previsiones.get(parada)
        metro.close()
        return result

    except exceptions.MissingContactError as e:
        print(f"Error de configuración: {e}")
        return None

    except exceptions.AuthError as e:
        print(f"Error de autenticación: {e}")
        return None

    except exceptions.NotFoundError as e:
        print(f"Parada no encontrada: {e}")
        return None

    except exceptions.RateLimitError as e:
        print(f"Límite de peticiones excedido")
        if e.retry_after:
            print(f"Reintentar en {e.retry_after} segundos")
        return None

    except exceptions.ServiceUnavailable as e:
        print(f"Servicio no disponible: {e}")
        return None

    except exceptions.MetroAPIError as e:
        print(f"Error de la API: {e}")
        return None
```

---

## Validación de Entrada

Algunas operaciones pueden lanzar `ValueError` para invalidar parámetros:

```python
from metrovalencia import MetroValencia

metro = MetroValencia(app_name="miapp", contact="dev@ejemplo.com")

# Idioma inválido para tarifas
try:
    tarifas = metro.tarifas.get("FR")  # FR no es válido
except ValueError as e:
    print(f"Idioma inválido: {e}")
    # Salida: "idioma must be one of: ES, CA, EN"

# Resolución de parada fallida
try:
    result = metro.previsiones.get("ParadaInexistente123")
except ValueError as e:
    print(f"No se pudo resolver la parada: {e}")

metro.close()
```