from rapidfuzz import fuzz

from metrovalencia.resources.base import Resource
from metrovalencia.resources.paradas import Paradas
from metrovalencia.models.previsiones import (
    PrevisionesResponse,
    EstadoParada,
)


class Previsiones(Resource):
    def _resolve_parada(self, parada: int | str) -> int:
        if isinstance(parada, int):
            return parada
        paradas = Paradas(self._http)
        local = paradas._load_local()
        matches = [(p, fuzz.ratio(p["nombre"].lower(), parada.lower())) for p in local]
        matches.sort(key=lambda x: x[1], reverse=True)
        if matches and matches[0][1] > 70:
            return matches[0][0]["id"]
        raise ValueError(f"Could not resolve parada: {parada}")

    def get(self, parada: int | str):
        """Get parsed predictions for a stop. Accepts stop ID (int) or name (str)."""
        parada_id = self._resolve_parada(parada)
        resp = self._http.get(f"/prevision/{parada_id}/parse")
        data = resp.json()
        return self._process_response(data, PrevisionesResponse)

    def estado(self, parada: int | str):
        """Get station status. Accepts stop ID (int) or name (str)."""
        parada_id = self._resolve_parada(parada)
        resp = self._http.get(f"/prevision/{parada_id}/estado")
        data = resp.json()
        return self._process_response(data, EstadoParada)