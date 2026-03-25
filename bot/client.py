import discord
from discord.ext import commands
import logging

logger = logging.getLogger(__name__)


class BotClient(commands.Bot):
    """Custom Discord bot client"""

    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.guild_reactions = True

        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=commands.DefaultHelpCommand(),
            *args,
            **kwargs
        )

    async def on_ready(self):
        """Called when the bot is ready"""
        logger.info(f"Bot logged in as {self.user}")
        logger.info(f"Bot ID: {self.user.id}")
        logger.info(f"Guilds: {len(self.guilds)}")

        try:
            synced = await self.tree.sync()
            logger.info(f"Synced {len(synced)} command(s)")
        except Exception as e:
            logger.error(f"Failed to sync commands: {e}")

    async def setup_hook(self):
        """Setup hook - load all cogs"""
        await self.load_cogs()

    async def load_cogs(self):
        """Load all cogs from the cogs directory"""
        cog_modules = [
            "bot.cogs.moderation",
            "bot.cogs.fun",
            "bot.cogs.utility",
            "bot.cogs.music",
        ]

        for cog in cog_modules:
            try:
                await self.load_extension(cog)
                logger.info(f"Loaded cog: {cog}")
            except Exception as e:
                logger.error(f"Failed to load cog {cog}: {e}")

    async def on_error(self, event, *args, **kwargs):
        """Global error handler"""
        logger.exception(f"Error in {event}")