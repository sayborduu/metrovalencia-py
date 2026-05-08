from metrovalencia.http import HttpClient
from metrovalencia import exceptions
from metrovalencia.resources import (
    Previsiones,
    Paradas,
    Incidencias,
    Tarjetas,
    Rutas,
    Tarifas,
    Comunicaciones,
)
from metrovalencia.resources.v2 import V2Client


class MetroValencia:
    def __init__(
        self,
        user_agent: str | None = None,
        app_name: str | None = None,
        app_version: str = "1.0",
        contact: str | None = None,
        api_key: str | None = None,
        base_url: str = "https://metroapi.alexbadi.es",
        response_type: str = "class",
    ):
        if response_type not in ("class", "json", "parsed_json"):
            raise ValueError("response_type must be one of: class, json, parsed_json")

        final_user_agent = user_agent

        if not final_user_agent:
            if not contact:
                raise exceptions.MissingContactError()
            if not app_name:
                raise exceptions.MissingContactError()
            final_user_agent = f"{app_name}/{app_version} (Python; contact={contact})"

        self._http = HttpClient(
            base_url=base_url,
            user_agent=final_user_agent,
            api_key=api_key,
            response_type=response_type,
        )
        self.previsiones = Previsiones(self._http)
        self.paradas = Paradas(self._http)
        self.incidencias = Incidencias(self._http)
        self.tarjetas = Tarjetas(self._http)
        self.rutas = Rutas(self._http)
        self.tarifas = Tarifas(self._http)
        self.comunicaciones = Comunicaciones(self._http)
        self.v2 = V2Client(self._http)

    def close(self):
        self._http.close()