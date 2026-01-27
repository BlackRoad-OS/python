"""
Exception classes for BlackRoad OS applications.
"""


class BlackRoadError(Exception):
    """Base exception for all BlackRoad errors."""

    def __init__(self, message: str, code: str = "BLACKROAD_ERROR"):
        """
        Initialize exception.

        Args:
            message: Error message
            code: Error code for categorization
        """
        self.message = message
        self.code = code
        super().__init__(message)

    def __str__(self) -> str:
        """String representation of error."""
        return f"[{self.code}] {self.message}"


class ConfigurationError(BlackRoadError):
    """Configuration-related error."""

    def __init__(self, message: str):
        """Initialize configuration error."""
        super().__init__(message, "CONFIG_ERROR")


class ConnectionError(BlackRoadError):
    """Connection-related error."""

    def __init__(self, message: str):
        """Initialize connection error."""
        super().__init__(message, "CONNECTION_ERROR")


class ValidationError(BlackRoadError):
    """Validation-related error."""

    def __init__(self, message: str):
        """Initialize validation error."""
        super().__init__(message, "VALIDATION_ERROR")
