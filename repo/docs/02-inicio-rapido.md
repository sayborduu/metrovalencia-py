# Inicio Rápido

## Autenticación

El SDK requiere un identificador de User-Agent para todas las peticiones. Hay tres formas de configurarlo:

### Opción 1: Manual

```python
from metrovalencia import MetroValencia

metro = MetroValencia(user_agent="miapp/1.0 (Python; contact=dev@ejemplo.com)")
```

### Opción 2: Automático (Recomendado)

```python
from metrovalencia import MetroValencia

# Generará automáticamente: "miapp/1.0 (Python; contact=dev@ejemplo.com)"
metro = MetroValencia(
    app_name="miapp",
    contact="dev@ejemplo.com"
)
```

### Opción 3: Con API Key

```python
from metrovalencia import MetroValencia

metro = MetroValencia(
    app_name="miapp",
    contact="dev@ejemplo.com",
    api_key="mv_api_key_..."
)
```

## Ejemplo Básico

```python
from metrovalencia import MetroValencia

metro = MetroValencia(
    app_name="miapp",
    contact="dev@ejemplo.com"
)

previsiones = metro.previsiones.get("Alameda")
print(f"Trenes próximos: {len(previsiones.previsiones)}")

estado = metro.previsiones.estado("Colón")
print(f"Estado de Colón: {estado.estado}")

paradas = metro.paradas.buscar("Marítim")
print(f"Estaciones encontradas: {len(paradas.paradas)}")

metro.close()
```

## Tipos de Respuesta

Puedes elegir en qué formato recibir los datos con el parámetro `response_type`:

### 1. class (por defecto)

Utiliza `dataclasses` para los modelos.

```python
metro = MetroValencia(
    app_name="miapp",
    contact="dev@ejemplo.com",
    response_type="class"
)

result = metro.previsiones.get("Alameda")
print(result.previsiones[0].destino)
```

### 2. json

Devuelve los datos crudos (diccionarios y listas).

```python
metro = MetroValencia(
    app_name="miapp",
    contact="dev@ejemplo.com",
    response_type="json"
)

result = metro.previsiones.get("Alameda")
print(result["previsiones"][0]["destino"])
```

### 3. parsed_json

Devuelve diccionarios pero elimina valores nulos y convierte las claves a `snake_case`.

```python
metro = MetroValencia(
    app_name="miapp",
    contact="dev@ejemplo.com",
    response_type="parsed_json"
)

result = metro.previsiones.get("Alameda")
print(result["previsiones"][0]["line_id"])  # camelCase convertido a snake_case
```