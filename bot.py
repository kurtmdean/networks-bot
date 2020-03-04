#!/usr/bin/python3

import discord
import asyncio
import os
import copy
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

bot.network = {}

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

async def uid2nick(dictionary, context):
    for uid in dictionary:
        guild = context.guild
        member = guild.get_member(uid)
        if member is not None:
            if isinstance(dictionary[uid], dict):
                await uid2nick(dictionary[uid], context)
            dictionary[member.nick] = dictionary[uid]
            dictionary.pop(uid)

@bot.command()
async def network(ctx):
    message = copy.deepcopy(bot.network)
    await uid2nick(message, ctx)
    await ctx.send(str(message))

@bot.command()
async def weight(ctx, member):
    member = ctx.guild.get_member_named(member)
    if ctx.author.id in bot.network.keys() and member is not None and member.id in bot.network.keys() and ctx.author.id != member.id:
        author = ctx.author
        alist = bot.network[author.id]
        val = alist[member.id]
        await ctx.send(str(val))
    else:
        await ctx.send(member.nick + " is not a member of this server.")

bot.run(os.getenv('BOT_TOKEN'))
