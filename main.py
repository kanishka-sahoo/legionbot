import discord
from discord.ext import commands
from dotenv import dotenv_values
import random


# config = {"TOKEN" : "bot-token-here"}
# imports from the .env file
config = dotenv_values(".env")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="?")


@bot.command(name="ping")
async def _ping(ctx):
    """Answers with pong"""
    await ctx.send("Pong")


@bot.command(name="joindate")
async def _joindate(ctx, *, member: discord.Member):
    await ctx.send(f"{member} joined on {member.joined_at}")


@bot.command(name="say")
async def say(ctx, *what):
    """Repeats what the users enters"""
    if len(what):
        await ctx.send(" ".join(what))
    else:
        await ctx.send("Say What?")


@bot.command(name="serverinfo")
async def serverinfo(ctx):
    """Displays Server information"""
    server = ctx.guild
    await ctx.send(f'Server Name: {server.name}\n\
        Server ID: {server.id}\nMembers: {server.member_count}')


@bot.command(name="roll")
async def roll(ctx, sides: int = 6):
    """Rolls a random number by default is till 6"""
    num = random.randint(1, sides)
    await ctx.send(f'You rolled a {num} on a {sides} sided dice!')

bot.run(config["TOKEN"])

