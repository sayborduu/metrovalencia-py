# Recursos

## Previsiones

Proporciona información sobre el estado de las paradas y el tiempo de llegada de los trenes.

### Métodos

#### `previsiones.get(parada: int | str)`

Obtiene las previsiones de llegada para una parada específica.

**Parámetros:**
- `parada` (int | str): ID de la parada o nombre de la estación ("Alameda", "Colón").

**Retorno:** `PrevisionesResponse`.

```python
result = metro.previsiones.get("Alameda")
for prev in result.previsiones:
    print(f"Línea {prev.line} a {prev.destino} en {prev.seconds} segundos")
```

#### `previsiones.estado(parada: int | str)`

Obtiene el estado de una estación concreta.

**Parámetros:**
- `parada` (int | str): ID o nombre de la estación.

**Retorno:** `EstadoParada`.

```python
estado = metro.previsiones.estado("Colón")
print(f"El estado es: {estado.estado}")
```

---

## Paradas

Información general de las estaciones del metro.

### Métodos

#### `paradas.all()`

Obtiene el listado completo de todas las paradas en la red.

**Retorno:** Lista de objetos `ParadaAll`.

```python
todas = metro.paradas.all()
for parada in todas:
    print(f"- {parada.name} - Líneas conectadas: {parada.lines}!")
```

#### `paradas.buscar(q: str)`

Busca una parada mediante un string de texto. Primero comprueba la caché local.

**Parámetros:**
- `q` (str): Término de búsqueda (ej: "Alameda")

**Retorno:** `ParadasResponse`.

```python
result = metro.paradas.buscar("Alameda")
print(f"Encontradas {len(result.paradas)} estaciones")
```

---

## Incidencias

Información de incidencias en la red.

### Métodos

#### `incidencias.transporte()`

Obtiene todas las incidencias de transporte activas.

**Retorno:** `IncidenciasTransporteResponse`.

```python
incidencias = metro.incidencias.transporte()
for inc in incidencias.incidencias:
    print(f"Incidencia: {inc.titulo} -> {inc.descripcion}")
```

#### `incidencias.accesibilidad()`

Obtiene las incidencias relacionadas con la accesibilidad de las estaciones.

**Retorno:** `IncidenciasAccesibilidadResponse`

```python
incidencias = metro.incidencias.accesibilidad()
```

---

## Tarjetas

Gestión de tarjetas de transporte.

### Métodos

#### `tarjetas.info(numero: int)`

Obtiene información de una tarjeta.

**Parámetros:**
- `numero` (int): Número de tarjeta

**Retorna:** `TarjetaInfo` (dataclass)

```python
info = metro.tarjetas.info(123456789)
print(f"Saldo: {info.saldo} €")
```

#### `tarjetas.viajes(numero: int)`

Obtiene el historial de viajes de una tarjeta.

**Parámetros:**
- `numero` (int): Número de tarjeta

**Retorna:** `ViajesResponse` (dataclass)

```python
viajes = metro.tarjetas.viajes(123456789)
for viaje in viajes.viajes:
    print(f"{viaje.fecha}: {viaje.origen} → {viaje.destino}")
```

---

## Rutas

Planificación de rutas entre estaciones.

### Métodos

#### `rutas.plan(origen_id: int, destino_id: int, hora_salida: str = None, fecha: str = None)`

Planifica una ruta entre dos estaciones (requiere IDs de estación).

**Parámetros:**
- `origen_id` (int): ID de la estación de origen
- `destino_id` (int): ID de la estación de destino
- `hora_salida` (str, opcional): Hora de salida (formato HH:MM)
- `fecha` (str, opcional): Fecha de viaje (formato YYYY-MM-DD)

**Retorna:** `RutaPlan` (dataclass)

```python
ruta = metro.rutas.plan(10, 14)
print(f"Duración: {ruta.duracion} minutos")
```

#### `rutas.rutap(origen: str, destino: str)`

Obtiene la ruta entre dos paradas por nombre.

**Parámetros:**
- `origen` (str): Nombre de la parada de origen
- `destino` (str): Nombre de la parada de destino

**Retorna:** `RutaP` (dataclass)

```python
ruta = metro.rutas.rutap("Colón", "Bailén")
print(f"Distancia: {ruta.distancia_total_km} km")
print(f"Tiempo: {ruta.tiempo_total_minutos:.2f} minutos")
for parada in ruta.ruta:
    print(f"  - {parada.nombre} ({parada.linea})")
```

---

## Tarifas

Información sobre tarifas y precios.

### Métodos

#### `tarifas.get(idioma: str = "ES")`

Obtiene las tarifas disponibles.

**Parámetros:**
- `idioma` (str): Idioma de las tarifas ("ES", "CA", "EN"). Predeterminado: "ES"

**Retorna:** `TarifasResponse` (dataclass)

**Raises:** `ValueError` si el idioma no es válido

```python
tarifas = metro.tarifas.get("ES")
for tarifa in tarifas.tarifas:
    print(f"{tarifa.titulo}: {tarifa.precio} €")
```

---

## Comunicaciones

Comunicados y noticias del servicio.

### Métodos

#### `comunicaciones.get()`

Obtiene los comunicados disponibles.

**Retorna:** Lista de objetos `Comunicacion` (dataclass)

```python
coms = metro.comunicaciones.get()
for c in coms:
    print(f"{c.fecha}: {c.titulo}")
```

---

## V2 (En desarrollo)

Endpoints experimentales de la API v2.

### Incidencias V2

#### `v2.incidencias.get()`

Obtiene incidencias de la API v2.

**Retorna:** `IncidenciasV2Response` (dataclass)

```python
result = metro.v2.incidencias.get()
print(f"Éxito: {result.success}")
print(f"Datos: {result.data}")
```