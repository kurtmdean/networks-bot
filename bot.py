#!/usr/bin/python3

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def pong(ctx):
    await ctx.send('ping')

bot.run(os.getenv('BOT_TOKEN'))
