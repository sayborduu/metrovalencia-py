from typing import Optional

from metrovalencia.resources.base import Resource
from metrovalencia.models.rutas import RutaPlan, RutaP


class Rutas(Resource):
    def plan(
        self,
        origen_id: int,
        destino_id: int,
        hora_salida: Optional[str] = None,
        fecha: Optional[str] = None,
    ):
        payload = {
            "origen": origen_id,
            "destino": destino_id,
        }
        if hora_salida:
            payload["hora_salida"] = hora_salida
        if fecha:
            payload["fecha"] = fecha
        resp = self._http.post("/plan", json=payload)
        data = resp.json()
        return self._process_response(data, RutaPlan)

    def rutap(self, origen: str, destino: str):
        resp = self._http.get("/beta/rutap", params={"origen": origen, "destino": destino})
        data = resp.json()
        return self._process_response(data, RutaP)