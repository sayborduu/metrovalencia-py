from metrovalencia.resources.v2.base import Resource
from metrovalencia.models.v2.incidencias import IncidenciaV2, IncidenciasV2Response


class Incidencias(Resource):
    def get(self):
        resp = self._http.get("/v2/incidencias")
        data = resp.json()
        return self._process_response(data, IncidenciasV2Response)