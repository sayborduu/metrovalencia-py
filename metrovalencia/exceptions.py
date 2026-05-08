from typing import Optional


class MetroAPIError(Exception):
    def __init__(self, message: str, status_code: Optional[int] = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.__str__())

    def __str__(self) -> str:
        if self.status_code:
            return f"[{self.status_code}] {self.message}"
        return self.message


class AuthError(MetroAPIError):
    pass


class NotFoundError(MetroAPIError):
    pass


class RateLimitError(MetroAPIError):
    def __init__(self, message: str, status_code: Optional[int] = None, retry_after: Optional[int] = None):
        self.retry_after = retry_after
        super().__init__(message, status_code)

    def __str__(self) -> str:
        base = super().__str__()
        if self.retry_after:
            return f"{base} (retry after {self.retry_after}s)"
        return base


class ServiceUnavailable(MetroAPIError):
    pass


class InvalidUserAgent(MetroAPIError):
    pass


class MissingContactError(Exception):
    def __init__(self):
        msg = "User-Agent is required. Provide either 'user_agent' or ('app_name' + 'contact') on init."
        super().__init__(msg)