from metrovalencia.http import HttpClient
from metrovalencia import utils


class Resource:
    def __init__(self, http: HttpClient):
        self._http = http

    def _process_response(self, data: dict, model_class=None):
        response_type = self._http._response_type
        if response_type == "class" and model_class:
            return model_class.from_dict(data)
        elif response_type == "parsed_json":
            return utils._clean_dict(data)
        else:
            return data