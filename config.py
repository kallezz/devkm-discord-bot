import os
from dotenv import load_dotenv

load_dotenv()

# Discord Bot Configuration
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN not found in .env file")

# Bot Configuration
BOT_PREFIX = "!"
BOT_VERSION = "1.0.0"
BOT_DESCRIPTION = "A Class Discord Bot"

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "logs/bot.log")

# Environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")