from typing import List

from metrovalencia.resources.base import Resource
from metrovalencia.models.tarjetas import TarjetaInfo, Viaje, ViajesResponse


class Tarjetas(Resource):
    def info(self, numero: int):
        resp = self._http.get(f"/tarjeta/{numero}")
        data = resp.json()
        return self._process_response(data, TarjetaInfo)

    def viajes(self, numero: int):
        resp = self._http.get(f"/viajes/{numero}")
        data = resp.json()
        return self._process_response(data, ViajesResponse)