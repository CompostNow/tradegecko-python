class TradeGeckoError(Exception):
    def __init__(self, message):
        self.message = message

    @property
    def name(self):
        return self.__class__.__name__

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
