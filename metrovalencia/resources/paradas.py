import json
from pathlib import Path
from typing import Optional, List

from metrovalencia.resources.base import Resource
from metrovalencia.models.paradas import Parada, ParadasResponse, ParadaAll


_paradas_cache: Optional[List[dict]] = None


def _get_paradas_path() -> Path:
    module_dir = Path(__file__).parent.parent / "data" / "paradas.json"
    if module_dir.exists():
        return module_dir
    try:
        import importlib.resources
        data_file = importlib.resources.files("metrovalencia.data").joinpath("paradas.json")
        return Path(str(data_file))
    except Exception:
        pass
    raise FileNotFoundError("paradas.json not found")


class Paradas(Resource):
    def _load_local(self) -> list[dict]:
        global _paradas_cache
        if _paradas_cache is not None:
            return _paradas_cache
        data_file = _get_paradas_path()
        with open(data_file, "r", encoding="utf-8") as f:
            _paradas_cache = json.load(f)
        return _paradas_cache

    def all(self):
        resp = self._http.get("/beta/paradas")
        data = resp.json()
        if self._http._response_type == "class":
            return [ParadaAll.from_dict(p) for p in data]
        elif self._http._response_type == "parsed_json":
            from metrovalencia import utils
            return utils._clean_dict(data)
        return data

    def buscar(self, q: str):
        local = self._load_local()
        exact_match = next((p for p in local if p["nombre"].lower() == q.lower()), None)
        if exact_match:
            data = {"paradas": [exact_match], "total": 1}
            if self._http._response_type == "class":
                return ParadasResponse.from_dict(data)
            elif self._http._response_type == "parsed_json":
                from metrovalencia import utils
                return utils._clean_dict(data)
            return [exact_match]
        resp = self._http.get("/paradas/buscar", params={"q": q})
        data = resp.json()
        return self._process_response(data, ParadasResponse)