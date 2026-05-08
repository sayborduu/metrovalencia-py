import re
from typing import Any


def _camel_to_snake(name: str) -> str:
    pattern = re.compile(r"(?<!^)(?=[A-Z])")
    return pattern.sub("_", name).lower()


def _clean_dict(data: Any) -> Any:
    if data is None:
        return None
    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            snake_key = _camel_to_snake(key)
            cleaned_value = _clean_dict(value)
            if cleaned_value is not None:
                result[snake_key] = cleaned_value
        return result
    if isinstance(data, list):
        return [_clean_dict(item) for item in data]
    return data