from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Parada:
    id: int
    latitud: float
    longitud: float
    nombre: str
    zona: str

    @classmethod
    def from_dict(cls, data: dict) -> "Parada":
        return cls(
            id=data.get("id", 0),
            latitud=data.get("latitud", 0.0),
            longitud=data.get("longitud", 0.0),
            nombre=data.get("nombre", ""),
            zona=data.get("zona", ""),
        )


@dataclass
class ParadasResponse:
    paradas: List[Parada]
    total: int

    @classmethod
    def from_dict(cls, data: dict) -> "ParadasResponse":
        return cls(
            paradas=[Parada.from_dict(p) for p in data.get("paradas", [])],
            total=data.get("total", 0),
        )


@dataclass
class BusquedaParada:
    id: int
    nombre: str

    @classmethod
    def from_dict(cls, data: dict) -> "BusquedaParada":
        return cls(
            id=data.get("id", 0),
            nombre=data.get("nombre", ""),
        )


@dataclass
class ParadaAll:
    id: str
    name: str
    lines: list[str]

    @classmethod
    def from_dict(cls, data: dict) -> "ParadaAll":
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            lines=data.get("lines", []),
        )