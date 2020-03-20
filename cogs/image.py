import random
import discord
import time
import asyncio
from discord.ext import commands, tasks



class Image(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
          print ('image.py has been loaded')

    @commands.command()
    async def pfp(self, ctx, *, member : discord.Member = None):
        if member == None:
            other=discord.Embed(color=discord.Colour.red())
            other.set_image(url=ctx.author.avatar_url)
            await ctx.send(embed = other)
        else:
            embed=discord.Embed(color=discord.Colour.red())
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed = embed)



    








def setup(client):
    client.add_cog(Image(client))
