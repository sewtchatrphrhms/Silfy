import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

MESSAGE_ID = 0
ROLE_ID = 0
EMOJI = "🔥"

@bot.event
async def on_ready():
    print(f"ออนไลน์: {bot.user}")

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == MESSAGE_ID and str(payload.emoji) == EMOJI:
        guild = bot.get_guild(payload.guild_id)
        role = guild.get_role(ROLE_ID)
        member = guild.get_member(payload.user_id)
        if member:
            await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == MESSAGE_ID and str(payload.emoji) == EMOJI:
        guild = bot.get_guild(payload.guild_id)
        role = guild.get_role(ROLE_ID)
        member = guild.get_member(payload.user_id)
        if member:
            await member.remove_roles(role)

bot.run(TOKEN)
