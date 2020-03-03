#!/usr/bin/python3

import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

bot.network = {}

"""
On startup, set presence and load network (empty for now).
"""
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("with Status"))
    bot.network = {}

@bot.listen()
async def on_message(message):
    src = message.author.id
    messages = await message.channel.history(limit=123).flatten()
    dst = messages[1].author.id # author of previous message, TODO: probably breaks on first message in new channel
    if src == dst: # ignore replies to self
        return
    if messages[1].author.bot or message.author.bot: #ignore bots
        return

    # update network
    if src not in bot.network.keys():
        bot.network[src] = {}
    if dst not in bot.network.keys():
        bot.network[dst] = {}
    if dst not in bot.network[src].keys():
        bot.network[src][dst] = 0
    if src not in bot.network[dst].keys():
        bot.network[dst][src] = 0
    bot.network[src][dst] += 1
    bot.network[dst][src] += 1

@bot.command()
async def print(ctx):
    await ctx.send(str(bot.network))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def pong(ctx):
    await ctx.send('ping')

bot.run(os.getenv('BOT_TOKEN'))
