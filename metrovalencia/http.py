import httpx

from metrovalencia import exceptions


class HttpClient:
    def __init__(
        self,
        base_url: str,
        user_agent: str,
        api_key: str | None = None,
        response_type: str = "class",
    ):
        self._base_url = base_url.rstrip("/")
        self._user_agent = user_agent
        self._api_key = api_key
        self._response_type = response_type
        self._client = httpx.Client(timeout=30.0)

    def _build_headers(self) -> dict:
        headers = {"User-Agent": self._user_agent}
        if self._api_key:
            headers["Authorization"] = f"Bearer {self._api_key}"
        return headers

    def _handle_response(self, response: httpx.Response) -> httpx.Response:
        if response.status_code == 401:
            raise exceptions.AuthError("Unauthorized", 401)
        if response.status_code == 404:
            raise exceptions.NotFoundError("Resource not found", 404)
        if response.status_code == 429:
            retry_after = None
            if "Retry-After" in response.headers:
                try:
                    retry_after = int(response.headers["Retry-After"])
                except ValueError:
                    pass
            raise exceptions.RateLimitError("Rate limit exceeded", 429, retry_after)
        if response.status_code == 503:
            raise exceptions.ServiceUnavailable("Service unavailable", 503)
        if response.status_code == 400:
            raise exceptions.InvalidUserAgent("Invalid User-Agent", 400)
        response.raise_for_status()
        return response

    def get(self, path: str, params: dict | None = None) -> httpx.Response:
        url = f"{self._base_url}{path}"
        response = self._client.get(url, headers=self._build_headers(), params=params)
        return self._handle_response(response)

    def post(self, path: str, json: dict | None = None) -> httpx.Response:
        url = f"{self._base_url}{path}"
        response = self._client.post(url, headers=self._build_headers(), json=json)
        return self._handle_response(response)

    def close(self):
        self._client.close()