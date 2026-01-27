"""Tests for exception classes."""

import pytest

from blackroad.exceptions import (
    BlackRoadError,
    ConfigurationError,
    ConnectionError,
    ValidationError,
)


def test_blackroad_error():
    """Test BlackRoadError base exception."""
    error = BlackRoadError("Test error")
    assert error.message == "Test error"
    assert error.code == "BLACKROAD_ERROR"
    assert "[BLACKROAD_ERROR]" in str(error)


def test_blackroad_error_custom_code():
    """Test BlackRoadError with custom code."""
    error = BlackRoadError("Test error", code="CUSTOM_CODE")
    assert error.code == "CUSTOM_CODE"
    assert "[CUSTOM_CODE]" in str(error)


def test_configuration_error():
    """Test ConfigurationError."""
    error = ConfigurationError("Invalid config")
    assert error.message == "Invalid config"
    assert error.code == "CONFIG_ERROR"
    assert isinstance(error, BlackRoadError)


def test_connection_error():
    """Test ConnectionError."""
    error = ConnectionError("Connection failed")
    assert error.message == "Connection failed"
    assert error.code == "CONNECTION_ERROR"
    assert isinstance(error, BlackRoadError)


def test_validation_error():
    """Test ValidationError."""
    error = ValidationError("Validation failed")
    assert error.message == "Validation failed"
    assert error.code == "VALIDATION_ERROR"
    assert isinstance(error, BlackRoadError)


def test_exception_raising():
    """Test that exceptions can be raised and caught."""
    with pytest.raises(BlackRoadError) as exc_info:
        raise BlackRoadError("Test error")

    assert "Test error" in str(exc_info.value)

    with pytest.raises(ConfigurationError) as exc_info:
        raise ConfigurationError("Config error")

    assert "Config error" in str(exc_info.value)
