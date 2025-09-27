"""
SuperCodex Services Module
Business logic services for the SuperCodex installation system
"""

from .codex_md import CODEXMdService
from .config import ConfigService
from .files import FileService
from .settings import SettingsService

# Backward compatibility alias
CLAUDEMdService = CODEXMdService

__all__ = [
    'CODEXMdService',
    'CLAUDEMdService',  # Keep for backward compatibility
    'ConfigService', 
    'FileService',
    'SettingsService'
]