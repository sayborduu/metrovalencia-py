from dataclasses import dataclass
from typing import Optional


@dataclass
class Comunicacion:
    id: int
    titulo: str
    cuerpo: str
    fecha: str
    tipo: Optional[str] = None
    imagen_url: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Comunicacion":
        return cls(
            id=data.get("id", 0),
            titulo=data.get("titulo", ""),
            cuerpo=data.get("cuerpo", ""),
            fecha=data.get("fecha", ""),
            tipo=data.get("tipo"),
            imagen_url=data.get("imagenUrl"),
        )