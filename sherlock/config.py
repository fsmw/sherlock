"""Configuration constants for Sherlock."""

from pathlib import Path

# API endpoints
PROVIDERS = {
    "anthropic": {
        "host": "api.anthropic.com",
        "base_url": "https://api.anthropic.com",
        "env_vars": ["ANTHROPIC_BASE_URL"],
    },
    "openai": {
        "host": "api.openai.com",
        "base_url": "https://api.openai.com",
        "env_vars": ["OPENAI_BASE_URL"],
    },
    "gemini": {
        "host": "generativelanguage.googleapis.com",
        "base_url": "https://generativelanguage.googleapis.com",
        "env_vars": [
            "GOOGLE_GEMINI_BASE_URL",
            "GEMINI_API_BASE_URL",
            "GEMINI_BASEURL",
        ],
    },
}

# Legacy compatibility
ANTHROPIC_HOST = PROVIDERS["anthropic"]["host"]
INTERCEPTED_HOSTS = [p["host"] for p in PROVIDERS.values()]

# Default token limits
DEFAULT_TOKEN_LIMIT = 200_000

# Default proxy port
DEFAULT_PROXY_PORT = 8080

# Data directories
SHERLOCK_DIR = Path.home() / ".sherlock"
HISTORY_FILE = SHERLOCK_DIR / "history.json"
PROMPTS_DIR = SHERLOCK_DIR / "prompts"

# IPC file for communication between interceptor and dashboard
IPC_FILENAME = "sherlock_ipc.jsonl"

# Dashboard settings
PROMPT_PREVIEW_LENGTH = 200
MAX_LOG_ENTRIES = 100

# OpenCode configuration
OPENCODE_PROVIDERS = {
    "anthropic": {
        "config_key": "anthropic",
        "base_url_path": ["provider", "anthropic", "options", "baseURL"],
    },
    "openai": {
        "config_key": "openai",
        "base_url_path": ["provider", "openai", "options", "baseURL"],
    },
    "google": {
        "config_key": "google",
        "base_url_path": ["provider", "google", "options", "baseURL"],
    },
}

# Possible OpenCode config file locations
OPENCODE_CONFIG_PATHS = [
    Path.home() / ".config" / "opencode" / "opencode.json",
    Path.home() / ".opencode" / "opencode.json",
    Path.home() / ".opencode.json",
]
