"""
Configuration Module

Handles all application configuration through environment variables.
Follows SOC 2 compliance by never storing secrets in code.

Usage:
    from src.config import settings
    api_key = settings.groq_api_key
"""

import os
import sys
from dataclasses import dataclass

from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


class ConfigurationError(Exception):
    """Raised when required configuration is missing or invalid."""
    pass


@dataclass(frozen=True)
class Settings:
    """
    Immutable application settings loaded from environment variables.
    
    Attributes:
        groq_api_key: API key for Groq (required)
        groq_model: Model ID for Groq
        website_url: URL for appointment website (required)
        login_email: Email for website login (required)
        login_password: Password for website login (required)
        debug_mode: Enable debug logging
        default_timeout: Browser automation timeout in seconds
        headless_mode: Run browser in headless mode
    """
    groq_api_key: str
    groq_model: str
    website_url: str
    login_email: str
    login_password: str
    debug_mode: bool
    default_timeout: int
    headless_mode: bool
    
    def __post_init__(self) -> None:
        """Validate settings after initialization."""
        if not self.groq_api_key:
            raise ConfigurationError(
                "GROQ_API_KEY is required. "
                "Copy .env.example to .env and set your API key."
            )
        if not self.website_url:
            raise ConfigurationError("WEBSITE_URL is required in .env file.")
        if not self.login_email:
            raise ConfigurationError("LOGIN_EMAIL is required in .env file.")
        if not self.login_password:
            raise ConfigurationError("LOGIN_PASSWORD is required in .env file.")


def _get_bool_env(key: str, default: bool = False) -> bool:
    """Parse boolean from environment variable."""
    value = os.getenv(key, str(default)).lower()
    return value in ("true", "1", "yes", "on")


def _get_int_env(key: str, default: int) -> int:
    """Parse integer from environment variable."""
    try:
        return int(os.getenv(key, str(default)))
    except ValueError:
        return default


def load_settings() -> Settings:
    """
    Load and validate settings from environment variables.
    
    Returns:
        Validated Settings instance
        
    Raises:
        ConfigurationError: If required settings are missing
    """
    return Settings(
        groq_api_key=os.getenv("GROQ_API_KEY", ""),
        groq_model=os.getenv("GROQ_MODEL", "moonshotai/kimi-k2-instruct-0905"),
        website_url=os.getenv("WEBSITE_URL", ""),
        login_email=os.getenv("LOGIN_EMAIL", ""),
        login_password=os.getenv("LOGIN_PASSWORD", ""),
        debug_mode=_get_bool_env("DEBUG_MODE", False),
        default_timeout=_get_int_env("DEFAULT_TIMEOUT", 60),
        headless_mode=_get_bool_env("HEADLESS_MODE", False),
    )


def get_settings() -> Settings:
    """
    Get application settings with proper error handling.
    
    Returns:
        Settings instance
        
    Note:
        Exits the application if configuration is invalid.
    """
    try:
        return load_settings()
    except ConfigurationError as e:
        print(f"❌ Configuration Error: {e}", file=sys.stderr)
        sys.exit(1)


# Global settings instance - loaded on import
settings = get_settings()


