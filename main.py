import discord
from discord.ext import commands
from dotenv import dotenv_values


# config = {"TOKEN" : "bot-token-here"}
# imports from the .env file
config = dotenv_values(".env")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="?")


@bot.command(name="ping")
async def _ping(ctx):
    await ctx.send("Pong")


@bot.command(name="joindate")
async def _joindate(ctx, *, member: discord.Member):
    await ctx.send(f"{member} joined on {member.joined_at}")

bot.run(config["TOKEN"])
