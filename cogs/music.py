import time
import discord
from discord.ext import commands

class Music(commands.Cog):

        def __init__(self, client):
            self.client = client

        @commands.Cog.listener()
        async def on_ready(self):
            print('music.py has been loaded')

        @commands.command(pass_context = True)
        async def join(self, ctx):
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send(f'Successfully joined {channel}.')

        @commands.command(pass_context = True)
        async def leave(self, ctx):
            channel = self.client.voice.channel
            await ctx.voice_client.disconnect()
            await ctx.send('Successfully left the voice channel.')


        








def setup(client):
    client.add_cog(Music(client))
