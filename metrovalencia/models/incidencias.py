from dataclasses import dataclass
from typing import Optional, List


@dataclass
class IncidenciaTransporte:
    id: int
    titulo: str
    descripcion: str
    tipo: Optional[str] = None
    linea: Optional[str] = None
    estado: Optional[str] = None
    fecha_inicio: Optional[str] = None
    fecha_fin: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "IncidenciaTransporte":
        return cls(
            id=data.get("id", 0),
            titulo=data.get("titulo", ""),
            descripcion=data.get("descripcion", ""),
            tipo=data.get("tipo"),
            linea=data.get("linea"),
            estado=data.get("estado"),
            fecha_inicio=data.get("fechaInicio"),
            fecha_fin=data.get("fechaFin"),
        )


@dataclass
class IncidenciaAccesibilidad:
    id: int
    titulo: str
    descripcion: str
    tipo: Optional[str] = None
    estado: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "IncidenciaAccesibilidad":
        return cls(
            id=data.get("id", 0),
            titulo=data.get("titulo", ""),
            descripcion=data.get("descripcion", ""),
            tipo=data.get("tipo"),
            estado=data.get("estado"),
        )


@dataclass
class IncidenciasTransporteResponse:
    incidencias: List[IncidenciaTransporte]

    @classmethod
    def from_dict(cls, data: dict) -> "IncidenciasTransporteResponse":
        return cls(
            incidencias=[IncidenciaTransporte.from_dict(i) for i in data.get("incidencias", [])],
        )


@dataclass
class IncidenciasAccesibilidadResponse:
    incidencias: List[IncidenciaAccesibilidad]

    @classmethod
    def from_dict(cls, data: dict) -> "IncidenciasAccesibilidadResponse":
        return cls(
            incidencias=[IncidenciaAccesibilidad.from_dict(i) for i in data.get("incidencias", [])],
        )