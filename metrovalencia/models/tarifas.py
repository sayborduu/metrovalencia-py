from dataclasses import dataclass, field
from typing import List


@dataclass
class TarifaDetalle:
    titulo: str
    precio: float

    @classmethod
    def from_dict(cls, data: dict) -> "TarifaDetalle":
        return cls(
            titulo=data.get("titulo", ""),
            precio=data.get("precio", 0.0),
        )


@dataclass
class Tarifa:
    zona: str
    categoria: str
    titulo: str
    precio: float

    @classmethod
    def from_dict(cls, data: dict) -> "Tarifa":
        return cls(
            zona=data.get("zona", ""),
            categoria=data.get("categoria", ""),
            titulo=data.get("titulo", ""),
            precio=data.get("precio", 0.0),
        )


@dataclass
class TarifasResponse:
    idioma: str
    tarifas: List[Tarifa]
    ultima_actualizacion: str = ""

    @classmethod
    def from_dict(cls, data: dict) -> "TarifasResponse":
        return cls(
            idioma=data.get("idioma", ""),
            tarifas=[Tarifa.from_dict(t) for t in data.get("tarifas", [])],
            ultima_actualizacion=data.get("ultimaActualizacion", ""),
        )