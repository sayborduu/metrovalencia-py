# metrovalencia

Python SDK for MetroValencia API (`https://metroapi.alexbadi.es`).

## Installation

```bash
pip install metrovalencia
```

## Quick Start

```python
from metrovalencia import MetroValencia

metro = MetroValencia(
    app_name="myapp",
    contact="dev@example.com"
)

previsiones = metro.previsiones.get("Alameda")
print(previsiones)
```

## Authentication

The API requires a User-Agent header identifying your application. Provide it in one of three ways:

**Option 1 — Manual override:**
```python
metro = MetroValencia(user_agent="myapp/1.0 (Python; contact=me@email.com)")
```

**Option 2 — Auto-generated (recommended):**
```python
metro = MetroValencia(
    app_name="myapp",
    app_version="1.0",   # optional, defaults to "1.0"
    contact="me@email.com"
)
# Generates: "myapp/1.0 (Python; contact=me@email.com)"
```

**Option 3 — With API key:**
```python
metro = MetroValencia(
    app_name="myapp",
    contact="me@email.com",
    api_key="mv_..."
)
```

If neither `user_agent` nor `contact` is provided, a `MissingContactError` is raised.

## Updating `paradas.json`

The `paradas.json` file is bundled with the package. To refresh it:

```bash
python scripts/fetch_paradas.py
```

## Resources

- `previsiones.get(parada)` — Get predictions (accepts stop ID or name)
- `previsiones.parsed(parada_id)` — Get parsed predictions
- `previsiones.estado(parada_id)` — Get station status
- `paradas.all()` — List all stops
- `paradas.buscar(q)` — Search stops by name
- `incidencias.transporte()` — Get transport incidents
- `incidencias.accesibilidad()` — Get accessibility incidents
- `tarjetas.info(numero)` — Get card info
- `tarjetas.viajes(numero)` — Get card travel history
- `rutas.plan(origen_id, destino_id, hora_salida, fecha)` — Plan route (POST)
- `rutas.rutap(origen, destino)` — Get route between stops
- `tarifas.get(idioma)` — Get fares (ES, CA, EN)
- `comunicaciones.get()` — Get communications
- `v2.incidencias.get()` — Get incidents (v2)

## License

MIT