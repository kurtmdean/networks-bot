#!/usr/bin/python3

import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

"""
@bot.listen()
async def on_message(message):
    # on any new message, check the previous message in this channel.
    # Increment the connection between these two people in the network
        # If either of those people is not in the network, add them
"""
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def pong(ctx):
    await ctx.send('ping')

bot.run(os.getenv('BOT_TOKEN'))
