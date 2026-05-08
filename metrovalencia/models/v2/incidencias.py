from dataclasses import dataclass, field
from typing import Optional, List, Any


@dataclass
class IncidenciaV2:
    id: int
    titulo: str
    descripcion: str
    tipo: str
    severidad: str
    estado: str
    fecha_inicio: Optional[str] = None
    fecha_fin: Optional[str] = None
    lineas_afectadas: Optional[list[str]] = None

    @classmethod
    def from_dict(cls, data: dict) -> "IncidenciaV2":
        return cls(
            id=data.get("id", 0),
            titulo=data.get("titulo", ""),
            descripcion=data.get("descripcion", ""),
            tipo=data.get("tipo", ""),
            severidad=data.get("severidad", ""),
            estado=data.get("estado", ""),
            fecha_inicio=data.get("fechaInicio"),
            fecha_fin=data.get("fechaFin"),
            lineas_afectadas=data.get("lineasAfectadas"),
        )


@dataclass
class IncidenciasV2Response:
    success: bool
    timestamp: str
    data: dict = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> "IncidenciasV2Response":
        return cls(
            success=data.get("success", False),
            timestamp=data.get("timestamp", ""),
            data=data.get("data", {}),
        )