import discord
import random
import time
import asyncio
import json
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class Config(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
          print ('Config.py has been loaded')



    @commands.command()
    async def set_prefix(self, ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        await ctx.send(f':white_check_mark: Successfully changed your prefix to \'{prefix}\'')

        prefixes [str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent = 4)

    @commands.command()
    @has_permissions(manage_roles = True)
    async def addrole(self, ctx, *, name):
        await ctx.guild.create_role(name = name)
        await ctx.send(f'Successfully added the role {name}.')


def setup(client):
    client.add_cog(Config(client))
