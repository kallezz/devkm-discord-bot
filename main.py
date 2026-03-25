import asyncio
import logging
from bot.client import BotClient
from config import DISCORD_TOKEN, LOG_LEVEL, LOG_FILE
from bot.services.logging import setup_logging

# Setup logging
setup_logging(LOG_LEVEL, LOG_FILE)
logger = logging.getLogger(__name__)

async def main():
    """Main entry point for the bot"""
    async with BotClient() as bot:
        try:
            logger.info("Starting Discord bot...")
            await bot.start(DISCORD_TOKEN)
        except Exception as e:
            logger.error(f"Failed to start bot: {e}", exc_info=True)
            raise

if __name__ == "__main__":
    asyncio.run(main())