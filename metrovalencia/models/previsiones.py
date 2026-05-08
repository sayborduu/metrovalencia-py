from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Prevision:
    cabecera: bool
    capacity: int
    destino: str
    hora: str
    line: int
    line_id: int
    seconds: int
    train_timestamp: int
    vehicle: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    meters: Optional[float] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Prevision":
        return cls(
            cabecera=data.get("cabecera", False),
            capacity=data.get("capacity", 0),
            destino=data.get("destino", ""),
            hora=data.get("hora", ""),
            line=data.get("line", 0),
            line_id=data.get("lineId", 0),
            seconds=data.get("seconds", 0),
            train_timestamp=data.get("trainTimestamp", 0),
            vehicle=data.get("vehicle"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            meters=data.get("meters"),
        )


@dataclass
class AforoBloqueado:
    desde: Optional[str] = None
    hasta: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict | None) -> "AforoBloqueado":
        if data is None:
            return cls()
        return cls(
            desde=data.get("desde"),
            hasta=data.get("hasta"),
        )


@dataclass
class PrevisionesResponse:
    aforo_bloqueado: AforoBloqueado
    previsiones: List[Prevision]

    @classmethod
    def from_dict(cls, data: dict) -> "PrevisionesResponse":
        return cls(
            aforo_bloqueado=AforoBloqueado.from_dict(data.get("aforoBloqueado")),
            previsiones=[Prevision.from_dict(p) for p in data.get("previsiones", [])],
        )


@dataclass
class PrevisionSimple:
    id: int
    nombre: str

    @classmethod
    def from_dict(cls, data: dict) -> "PrevisionSimple":
        return cls(
            id=data.get("id", 0),
            nombre=data.get("nombre", ""),
        )


@dataclass
class EstadoParada:
    id: int
    nombre: str
    estado: str

    @classmethod
    def from_dict(cls, data: dict) -> "EstadoParada":
        return cls(
            id=data.get("id", 0),
            nombre=data.get("nombre", ""),
            estado=data.get("estado", ""),
        )