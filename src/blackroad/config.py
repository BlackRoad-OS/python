"""
Configuration management for BlackRoad OS applications.

Provides environment-based configuration loading and validation.
"""

import os
from typing import Any, Optional


class Config:
    """Configuration manager for BlackRoad OS applications."""

    def __init__(
        self,
        env: str = "development",
        log_level: str = "info",
        api_url: str = "https://api.blackroad.io",
        **kwargs: Any,
    ):
        """
        Initialize configuration.

        Args:
            env: Environment (development, staging, production)
            log_level: Logging level (debug, info, warning, error)
            api_url: BlackRoad API endpoint URL
            **kwargs: Additional configuration options
        """
        self.env = env
        self.log_level = log_level
        self.api_url = api_url
        self.extra = kwargs

    @classmethod
    def from_env(cls, prefix: str = "BLACKROAD_") -> "Config":
        """
        Load configuration from environment variables.

        Args:
            prefix: Prefix for environment variables (default: BLACKROAD_)

        Returns:
            Config instance with values from environment
        """
        env = os.getenv(f"{prefix}ENV", "development")
        log_level = os.getenv(f"{prefix}LOG_LEVEL", "info")
        api_url = os.getenv(f"{prefix}API_URL", "https://api.blackroad.io")

        # Load all prefixed environment variables
        extra = {}
        for key, value in os.environ.items():
            if key.startswith(prefix) and key not in [
                f"{prefix}ENV",
                f"{prefix}LOG_LEVEL",
                f"{prefix}API_URL",
            ]:
                # Convert BLACKROAD_FOO_BAR to foo_bar
                config_key = key[len(prefix) :].lower()
                extra[config_key] = value

        return cls(env=env, log_level=log_level, api_url=api_url, **extra)

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Get configuration value.

        Args:
            key: Configuration key
            default: Default value if key not found

        Returns:
            Configuration value or default
        """
        return getattr(self, key, self.extra.get(key, default))

    def to_dict(self) -> dict[str, Any]:
        """
        Convert configuration to dictionary.

        Returns:
            Dictionary of configuration values
        """
        return {
            "env": self.env,
            "log_level": self.log_level,
            "api_url": self.api_url,
            **self.extra,
        }

    def __repr__(self) -> str:
        """String representation of configuration."""
        return f"Config(env={self.env!r}, log_level={self.log_level!r})"
