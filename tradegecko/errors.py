import json
from typing import Dict, Any, Optional


class TradeGeckoError(Exception):
    def __init__(self, message: str):
        self.message = message
        try:
            self.data: Dict[str, Any] = json.loads(message)
        except Exception:
            self.data: Dict[str, Any] = {}

    @property
    def name(self):
        return self.__class__.__name__

    def get(self, key: str, default: Any = None) -> Optional[Any]:
        """Return the value from the data dict.

        If the key is not found default value will be returned.
        """
        return self.data.get(key, default=default)

    def __str__(self):
        return f"{self.name}({self.message})"

    __repr__ = __str__


class AuthenticationError(TradeGeckoError):
    pass


class ProcessingError(TradeGeckoError):
    pass


class RateLimitExceeded(TradeGeckoError):
    pass


class ListObjectsError(TradeGeckoError):
    pass


class GetObjectError(TradeGeckoError):
    pass


class CreateObjectError(TradeGeckoError):
    pass


class UpdateObjectError(TradeGeckoError):
    pass


class DeleteObjectError(TradeGeckoError):
    pass
