from enum import Enum


class PolygonApiException(Exception):
    class ErrorType(Enum):
        UNKNOWN = 0
        NOT_FOUND = 1
        INVALID_API_KEY = 2

    def __init__(self, error_type: ErrorType = ErrorType.UNKNOWN, message: str = None):
        self.error_type = error_type
        self.message = message
        super().__init__(self.message)

    def to_json(self):
        return {
            "error_type": self.error_type.name,
            "message": self.message
        }

    def __str__(self):
        return f"{self.error_type.name}: {self.message}"