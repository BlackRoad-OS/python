"""Tests for Logger class."""

import logging

from blackroad.logger import Logger


def test_logger_initialization():
    """Test basic Logger initialization."""
    logger = Logger("test", level="DEBUG")
    assert logger.logger.name == "test"
    assert logger.logger.level == logging.DEBUG


def test_logger_levels():
    """Test different logging levels."""
    logger = Logger("test", level="INFO")
    assert logger.logger.level == logging.INFO

    logger = Logger("test", level="WARNING")
    assert logger.logger.level == logging.WARNING

    logger = Logger("test", level="ERROR")
    assert logger.logger.level == logging.ERROR


def test_logger_methods():
    """Test logger methods don't raise errors."""
    logger = Logger("test", level="DEBUG")

    # These should not raise exceptions
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
