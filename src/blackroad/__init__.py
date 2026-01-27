"""
BlackRoad Python - Core utilities and libraries for BlackRoad OS ecosystem.

This package provides foundational Python components that enable communication
and interoperability across all BlackRoad-OS repositories.
"""

__version__ = "0.1.0"
__author__ = "BlackRoad OS"
__email__ = "blackroad.systems@gmail.com"
__license__ = "Proprietary"

# Core exports
from .config import Config
from .exceptions import BlackRoadError
from .logger import Logger

__all__ = [
    "Config",
    "Logger",
    "BlackRoadError",
    "__version__",
]
