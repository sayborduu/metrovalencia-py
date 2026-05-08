# Modelos de Datos

El SDK utiliza `dataclasses` para estructurar la información obtenida. Todos provienen con un método `from_dict()`, permitiendo crear instancias manualmente.

## Previsiones

### PrevisionesResponse

```python
from metrovalencia.models import PrevisionesResponse

@dataclass
class PrevisionesResponse:
    aforo_bloqueado: AforoBloqueado  # Muestra información de accesibilidad a la estación
    previsiones: List[Prevision]     # Lista de previsiones
```

### Prevision

```python
from metrovalencia.models import Prevision

@dataclass
class Prevision:
    cabecera: bool        # Si es inicio de la ruta
    capacity: int        # Capacidad del tren
    destino: str         # Estación de destino
    hora: str            # Timestamp en formato hora
    line: int            # Número de línea
    line_id: int         # ID de la línea
    seconds: int         # Segundos restantes para llegada
    train_timestamp: int  # Timestamp del tren
    vehicle: Optional[int]          # ID asignado del vehículo 
    latitude: Optional[float]        # Latitud 
    longitude: Optional[float]       # Longitud
    meters: Optional[float]          # Distancia a la parada
```

### AforoBloqueado

```python
@dataclass
class AforoBloqueado:
    desde: Optional[str]  # Cuándo empezó el corte de aforo
    hasta: Optional[str]  # Hasta cuándo durará (estimado)
```

### EstadoParada

```python
@dataclass
class EstadoParada:
    id: int      # ID de la parada
    nombre: str  # Nombre (ej. "Alameda")
    estado: str # "ABIERTO", "CERRADO", o información asociada
```

---

## Paradas

### ParadaAll

```python
@dataclass
class ParadaAll:
    id: str           # ID
    name: str         # Nombre
    lines: List[str]  # Lista de las líneas que pasan
```

### ParadasResponse

```python
@dataclass
class ParadasResponse:
    paradas: List[Parada]  # Todas las paradas recuperadas
    total: int             # Cantidad del listado
```

---

## Incidencias

### IncidenciaTransporte

```python
@dataclass
class IncidenciaTransporte:
    id: int                    # ID
    titulo: str                # Titular de la incidencia
    descripcion: str           # Descripción en detalle
    tipo: Optional[str]        # El tipo (retraso, avería, etc.)
    linea: Optional[str]       # Línea afectada
    estado: Optional[str]      # Si sigue activa o si finalizó
    fecha_inicio: Optional[str] # Cuándo comenzó
    fecha_fin: Optional[str]   # Previsión final
```

### IncidenciaAccesibilidad

```python
@dataclass
class IncidenciaAccesibilidad:
    id: int                    # ID
    titulo: str                # Titular 
    descripcion: str           # Descripción detallada
    tipo: Optional[str]        # Ascensor, escalera...
    estado: Optional[str]      # Estado
```

---

## Tarjetas

### TarjetaInfo

```python
@dataclass
class TarjetaInfo:
    numero: int               # Número de tarjeta
    tipo: str                 # Tipo de tarjeta
    saldo: float              # Saldo actual
    zona: Optional[str]       # Zona
    fecha_expiracion: Optional[str]  # Fecha de expiración
    activa: Optional[bool]    # Si está activa
```

### Viaje

```python
@dataclass
class Viaje:
    id: int       # ID del viaje
    fecha: str    # Fecha del viaje
    origen: str   # Estación de origen
    destino: str  # Estación de destino
    linea: str    # Línea utilizada
    importe: float # Importe del viaje
```

### ViajesResponse

```python
@dataclass
class ViajesResponse:
    info: dict             # Información de la tarjeta
    viajes: List[Viaje]    # Lista de viajes
```

---

## Rutas

### ParadaRuta

```python
@dataclass
class ParadaRuta:
    distancia_desde_anterior_km: float   # Distancia desde anterior
    es_primera_parada_linea: bool        # Primera parada de línea
    id: str                               # ID de la parada
    linea: str                            # Línea
    lineas_disponibles: List[str]        # Líneas disponibles
    nombre: str                           # Nombre de la parada
    segundos_acumulados: int             # Segundos acumulados
    tiempo_llegada: str                  # Hora de llegada
    transbordo: bool                     # Si es transbordo
    aviso: Optional[str]                 # Aviso especial
    estacion_cerrada: Optional[bool]     # Si la estación está cerrada
```

### RutaP

```python
@dataclass
class RutaP:
    aviso_servicio: Optional[str]              # Aviso del servicio
    costo_shortest_path_length: Optional[float] # Coste del camino
    distancia_total_km: float                   # Distancia total en km
    proximos_trenes_origen: List[dict]          # Próximos trenes
    ruta: List[ParadaRuta]                      # Ruta calculada
    tiempo_total_minutos: float                 # Tiempo total en minutos
    ultima_parada_abierta: Optional[str]        # Última parada abierta
    avisos: List[str]                           # Avisos
```

---

## Tarifas

### Tarifa

```python
@dataclass
class Tarifa:
    zona: str       # Zona
    categoria: str  # Categoría
    titulo: str     # Título
    precio: float   # Precio
```

### TarifasResponse

```python
@dataclass
class TarifasResponse:
    idioma: str              # Idioma
    tarifas: List[Tarifa]    # Lista de tarifas
    ultima_actualizacion: str # Última actualización
```

---

## V2

### IncidenciaV2

```python
@dataclass
class IncidenciaV2:
    id: int                         # ID
    titulo: str                     # Título
    descripcion: str                # Descripción
    tipo: str                       # Tipo
    severidad: str                  # Severidad
    estado: str                     # Estado
    fecha_inicio: Optional[str]     # Fecha inicio
    fecha_fin: Optional[str]        # Fecha fin
    lineas_afectadas: Optional[List[str]]  # Líneas afectadas
```

### IncidenciasV2Response

```python
@dataclass
class IncidenciasV2Response:
    success: bool     # Si la petición fue exitosa
    timestamp: str    # Timestamp de la respuesta
    data: dict        # Datos de la respuesta
```

---

## Importar Modelos

```python
# Importar todos los modelos
from metrovalencia.models import (
    PrevisionesResponse,
    Prevision,
    ParadaAll,
    TarjetaInfo,
    Viaje,
    RutaP,
    # ... etc
)

# O importar modelos específicos
from metrovalencia.models.previsiones import PrevisionesResponse
from metrovalencia.models.rutas import RutaP
```