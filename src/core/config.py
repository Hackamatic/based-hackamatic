"""
Configuration settings for Based Hackamatic
"""
from pathlib import Path
import os

# Base paths
ROOT_DIR = Path(__file__).parent.parent.parent
SRC_DIR = ROOT_DIR / "src"
DATA_DIR = ROOT_DIR / "data"
LOGS_DIR = ROOT_DIR / "logs"

# Create necessary directories
for directory in [DATA_DIR, LOGS_DIR]:
    directory.mkdir(exist_ok=True)

# Agent configuration
AGENT_CONFIG = {
    "model": "gpt-4",
    "temperature": 0.2,
    "network_id": os.getenv("NETWORK_ID", "base-sepolia"),
}

# Wallet configuration
WALLET_CONFIG = {
    "min_balance": "0.01",  # Minimum balance to maintain in ETH
    "max_transaction": "1.0",  # Maximum transaction amount in ETH
    "gas_limit": 300000,  # Default gas limit for transactions
}

# Project templates
PROJECT_TEMPLATES = {
    "default": {
        "directories": [
            "src",
            "tests",
            "docs",
            "contracts",
        ],
        "files": {
            "README.md": "Project README template",
            ".env.example": "Environment variables template",
            ".gitignore": "Git ignore template",
        }
    }
}

# Logging configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": str(LOGS_DIR / "hackamatic.log"),
            "formatter": "standard",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": "INFO",
        }
    }
}

# Security settings
SECURITY_CONFIG = {
    "max_retries": 3,
    "timeout": 30,
    "required_confirmations": 2,
} 