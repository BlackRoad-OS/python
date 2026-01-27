"""Tests for Config class."""

from blackroad.config import Config


def test_config_initialization():
    """Test basic Config initialization."""
    config = Config(env="production", log_level="debug")
    assert config.env == "production"
    assert config.log_level == "debug"
    assert config.api_url == "https://api.blackroad.io"


def test_config_from_env(monkeypatch):
    """Test Config.from_env() method."""
    monkeypatch.setenv("BLACKROAD_ENV", "staging")
    monkeypatch.setenv("BLACKROAD_LOG_LEVEL", "warning")
    monkeypatch.setenv("BLACKROAD_CUSTOM_VALUE", "test123")

    config = Config.from_env()
    assert config.env == "staging"
    assert config.log_level == "warning"
    assert config.get("custom_value") == "test123"


def test_config_get_method():
    """Test Config.get() method."""
    config = Config(env="development")
    assert config.get("env") == "development"
    assert config.get("nonexistent", "default") == "default"


def test_config_to_dict():
    """Test Config.to_dict() method."""
    config = Config(env="test", log_level="info", custom="value")
    config_dict = config.to_dict()
    assert config_dict["env"] == "test"
    assert config_dict["log_level"] == "info"
    assert config_dict["custom"] == "value"


def test_config_repr():
    """Test Config string representation."""
    config = Config(env="production", log_level="error")
    repr_str = repr(config)
    assert "production" in repr_str
    assert "error" in repr_str
