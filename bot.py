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
    bot.network = {}


@bot.listen()
async def on_message(message):

    prev = message.author.id
    history = await message.channel.history(limit=5).flatten()
    curr = history[1].author.id

    # ignore replies to self
    if prev == curr:
        return

    # ignore bots
    if message.author.bot or history[1].author.bot:
        return

    # update network
    if prev not in bot.network.keys():
        bot.network[prev] = {}
    if curr not in bot.network.keys():
        bot.network[curr] = {}
    if curr not in bot.network[prev].keys():
        bot.network[prev][curr] = 0
    if prev not in bot.network[curr].keys():
        bot.network[curr][prev] = 0
    bot.network[prev][curr] += 1
    bot.network[curr][prev] += 1


def uid2nick(ctx, network):
    for uid in network:
        guild = ctx.guild
        member = guild.get_member(uid)
        if member is not None:
            if isinstance(network[uid], dict):
                uid2nick(ctx, network[uid])
            network[member.nick] = network[uid]
            network.pop(uid)


@bot.command()
async def network(ctx, id="name"):
    message = None
    if id == "uid":
        message = str(bot.network)
    if id == "name":
        message = copy.deepcopy(bot.network)
        uid2nick(ctx, message)
    await ctx.send(str(message))


@bot.command()
async def weight(ctx, nick1, nick2=None):
    member1 = member2 = None
    if nick2 is None:
        member1 = ctx.author
        member2 = ctx.guild.get_member_named(nick1)
        if member2 is None:
            await ctx.send(f'{nick1} is not a member of this guild.')
    else:
        member1 = ctx.guild.get_member_named(nick1)
        if member1 is None:
            await ctx.send(f'{nick1} is not a member of this guild.')
        member2 = ctx.guild.get_member_named(nick2)
        if member2 is None:
            await ctx.send(f'{nick2} is not a member of this guild.')

    if member1.id not in bot.network.keys(
    ) or member2.id not in bot.network[member1.id]:
        await ctx.send(f'{member1.nick} is not connected to {member2.nick}.')
    else:
        await ctx.send(
            f'{member1.nick} is connected to {member2.nick} with a link of weight {bot.network[member1.id][member2.id]}.'
        )


bot.run(os.getenv('BOT_TOKEN'))
