from metrovalencia.resources.base import Resource
from metrovalencia.models.incidencias import (
    IncidenciasTransporteResponse,
    IncidenciasAccesibilidadResponse,
)


class Incidencias(Resource):
    def transporte(self):
        resp = self._http.get("/incidencias/parse")
        data = resp.json()
        return self._process_response(data, IncidenciasTransporteResponse)

    def accesibilidad(self):
        resp = self._http.get("/accesibilidad/parse")
        data = resp.json()
        return self._process_response(data, IncidenciasAccesibilidadResponse)