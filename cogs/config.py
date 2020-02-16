import discord
import random
import time
import asyncio
import json
from discord.ext import commands


class Config(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
          print ('fun.py has been loaded')



    @commands.command()
    async def set_prefix(self, ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)



        prefixes [str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent = 4)
        await ctx.send(f':white_check_mark: Successfully changed your prefix to \'{prefix}\'')


def setup(client):
    client.add_cog(Config(client))
