from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TarjetaInfo:
    numero: int
    tipo: str
    saldo: float
    zona: Optional[str] = None
    fecha_expiracion: Optional[str] = None
    activa: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: dict) -> "TarjetaInfo":
        return cls(
            numero=data.get("numero", 0),
            tipo=data.get("tipo", ""),
            saldo=data.get("saldo", 0.0),
            zona=data.get("zona"),
            fecha_expiracion=data.get("fechaExpiracion"),
            activa=data.get("activa"),
        )


@dataclass
class Viaje:
    id: int
    fecha: str
    origen: str
    destino: str
    linea: str
    importe: float

    @classmethod
    def from_dict(cls, data: dict) -> "Viaje":
        return cls(
            id=data.get("id", 0),
            fecha=data.get("fecha", ""),
            origen=data.get("origen", ""),
            destino=data.get("destino", ""),
            linea=data.get("linea", ""),
            importe=data.get("importe", 0.0),
        )


@dataclass
class ViajesResponse:
    info: dict
    viajes: List[Viaje]

    @classmethod
    def from_dict(cls, data: dict) -> "ViajesResponse":
        return cls(
            info=data.get("info", {}),
            viajes=[Viaje.from_dict(v) for v in data.get("viajes", [])],
        )