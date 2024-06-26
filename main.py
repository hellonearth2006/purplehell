import nextcord
from nextcord.ext import commands
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define intents
intents = nextcord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True
intents.message_content = True

# Bot setup
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    logger.info('Bot is ready and running.')
    await bot.sync_application_commands()
    logger.info('Application commands synced.')

@bot.slash_command(
    name="login",
    description="Sends an ephemeral message with the link to your website."
)
async def login(interaction: nextcord.Interaction):
    website_link = "https://media.discordapp.net/attachments/1214301893153521818/1254566343664205854/877c81f89d39439a749cd52f80121b99.png?ex=6679f575&is=6678a3f5&hm=c72f47bd4f209642b80ee768031aceb58dac9d9490d059ced2f93f262ef02250&"

    try:
        logger.info(f"Interaction received: {interaction}")

        # Immediate acknowledgement
        await interaction.response.defer(ephemeral=True)
        logger.info("Interaction deferred successfully.")

        # Send follow-up message
        await interaction.followup.send(content=f"Click the link to access your website: {website_link}", ephemeral=True)
        logger.info(f"Response sent to interaction: {interaction.id}")
    except nextcord.errors.NotFound as e:
        logger.error(f"Interaction not found or expired: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

# Retrieve bot token from environment variable
bot_token = os.getenv('DISCORD_TOKEN')

if bot_token:
    try:
        bot.run(bot_token)
    except Exception as e:
        logger.error(f"Failed to run bot: {e}")
else:
    logger.error("Error: DISCORD_TOKEN environment variable not set.")
