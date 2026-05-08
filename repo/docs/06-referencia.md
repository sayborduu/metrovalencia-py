# Referencia de la API

## MetroValencia

El cliente principal que controla todas las interacciones con la API.

```python
from metrovalencia import MetroValencia

metro = MetroValencia(
    user_agent: str | None = None,    # Proporcionar el UA manualmente
    app_name: str | None = None,      # Nombre de tu app 
    app_version: str = "1.0",         # Versión
    contact: str | None = None,       # Email de contacto (necesario para generar el UA)
    api_key: str | None = None,       # API Key alternativa
    base_url: str = "https://metroapi.alexbadi.es",  # URL base de las peticiones
    response_type: str = "class"      # Puede ser "class", "json", o "parsed_json"
)
```

### Atributos

- `previsiones`: Datos de los horarios.
- `paradas`: Listados y búsquedas de paradas.
- `incidencias`: Incidencias publicadas.
- `tarjetas`: Información y control de pases de tarjetas (Suma recomendada).
- `rutas`: Planificador de rutas.
- `tarifas`: Información de facturación o zonificación.
- `comunicaciones`: Avisos oficiales.
- `v2`: Versión 2 de ciertos endpoints.

### Métodos

- `close()`: Cierra la conexión y libera uso de puertos.

---

## HttpClient

El módulo interno para procesar peticiones HTTP. Raramente debe usarse o llamarse.

```python
from metrovalencia.http import HttpClient

http = HttpClient(
    base_url: str,
    user_agent: str,
    api_key: str | None = None,
    response_type: str = "class"
)
```

### Métodos principales

- `get(path: str, params: dict | None = None)`: Procesa y enruta peticiones GET.
- `post(path: str, json: dict | None = None)`: Enruta llamadas POST.

---

## Resource (Base)

La clase con la lógica modelo para manejar recursos subyacentes.

```python
from metrovalencia.resources.base import Resource
```

---

## Especificar formato `response_type`

Permite determinar cómo se devolverá la respuesta a los procesos generales de métodos en endpoints:

| Valor | ¿Qué hace? |
|-------|-------------|
| `"class"` | Devuelve los datos formateados a través de `dataclasses` (Por defecto) |
| `"json"` | Devuelve el JSON extraído exactamente provisto por peticiones crudas web |
| `"parsed_json"` | Convierte e interactúa como dict, pero las claves se convierten a `snake_case` y se remueven nulos |

---

## Constantes Principales

```python
from metrovalencia import __version__

print(__version__)  # Ej. "0.1.0"
```

---

## Módulos

```python
# Para inicializar
from metrovalencia import MetroValencia

# Para atrapar excepciones de peticiones a métodos
from metrovalencia import exceptions
from metrovalencia.exceptions import (
    MetroAPIError,
    AuthError,
    NotFoundError,
    RateLimitError,
    ServiceUnavailable,
    InvalidUserAgent,
    MissingContactError
)

# Para usar interfaces de Dataclasses de la respuesta configurada
from metrovalencia.models import PrevisionesResponse
from metrovalencia import models
from metrovalencia.models import (
    PrevisionesResponse,
    Prevision,
    AforoBloqueado,
    EstadoParada,
    ParadaAll,
    TarjetaInfo,
    Viaje,
    ViajesResponse,
    RutaP,
    RutaPlan,
    TarifasResponse,
    Comunicacion,
    IncidenciasV2Response
)
```