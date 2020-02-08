import time
import discord
from discord.ext import commands

class ping(commands.Cog):

    def __init__(self, client):
            self.client = client
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('ping.py has been loaded')

    #Commands
    @commands.command()
    async def ping(self, ctx): 
     await ctx.send(f'Heres Your Ping : {round(self.client.latency  * 1000)}ms')



def setup(client):
    client.add_cog(ping(client))
    