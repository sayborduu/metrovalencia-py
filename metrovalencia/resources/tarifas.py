from metrovalencia.resources.base import Resource
from metrovalencia.models.tarifas import TarifasResponse


class Tarifas(Resource):
    def get(self, idioma: str = "ES"):
        if idioma not in ("ES", "CA", "EN"):
            raise ValueError("idioma must be one of: ES, CA, EN")
        resp = self._http.get(f"/tarifas/{idioma}")
        data = resp.json()
        return self._process_response(data, TarifasResponse)