from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class ParadaRuta:
    distancia_desde_anterior_km: float
    es_primera_parada_linea: bool
    id: str
    linea: str
    lineas_disponibles: List[str]
    nombre: str
    segundos_acumulados: int
    tiempo_llegada: str
    transbordo: bool
    aviso: Optional[str] = None
    estacion_cerrada: Optional[bool] = None
    predicted_time: Optional[bool] = None
    siguiente_tren: Optional[dict] = None

    @classmethod
    def from_dict(cls, data: dict) -> "ParadaRuta":
        return cls(
            distancia_desde_anterior_km=data.get("distancia_desde_anterior_km", 0.0),
            es_primera_parada_linea=data.get("es_primera_parada_linea", False),
            id=data.get("id", ""),
            linea=data.get("linea", ""),
            lineas_disponibles=data.get("lineas_disponibles", []),
            nombre=data.get("nombre", ""),
            segundos_acumulados=data.get("segundos_acumulados", 0),
            tiempo_llegada=data.get("tiempo_llegada", ""),
            transbordo=data.get("transbordo", False),
            aviso=data.get("aviso"),
            estacion_cerrada=data.get("estacion_cerrada"),
            predicted_time=data.get("predictedTime"),
            siguiente_tren=data.get("siguiente_tren"),
        )


@dataclass
class RutaPlan:
    origen: str
    destino: str
    duracion: int
    distancia: Optional[float] = None
    segmentos: List[dict] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> "RutaPlan":
        return cls(
            origen=data.get("origen", ""),
            destino=data.get("destino", ""),
            duracion=data.get("duracion", 0),
            distancia=data.get("distancia"),
            segmentos=data.get("segmentos", []),
        )


@dataclass
class RutaP:
    aviso_servicio: Optional[str] = None
    costo_shortest_path_length: Optional[float] = None
    distancia_total_km: float = 0.0
    proximos_trenes_origen: List[dict] = field(default_factory=list)
    ruta: List[ParadaRuta] = field(default_factory=list)
    tiempo_total_minutos: float = 0.0
    ultima_parada_abierta: Optional[str] = None
    avisos: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> "RutaP":
        return cls(
            aviso_servicio=data.get("aviso_servicio"),
            costo_shortest_path_length=data.get("costo___shortest_path_length"),
            distancia_total_km=data.get("distancia_total_km", 0.0),
            proximos_trenes_origen=data.get("proximos_trenes_origen", []),
            ruta=[ParadaRuta.from_dict(p) for p in data.get("ruta", [])],
            tiempo_total_minutos=data.get("tiempo_total_minutos", 0.0),
            ultima_parada_abierta=data.get("ultima_parada_abierta"),
            avisos=data.get("avisos", []),
        )