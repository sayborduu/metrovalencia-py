from metrovalencia.resources.base import Resource
from metrovalencia.models.comunicaciones import Comunicacion


class Comunicaciones(Resource):
    def get(self):
        resp = self._http.get("/comunicaciones")
        data = resp.json()
        if self._http._response_type == "class":
            return [Comunicacion.from_dict(c) for c in data]
        elif self._http._response_type == "parsed_json":
            from metrovalencia import utils
            return utils._clean_dict(data)
        return data