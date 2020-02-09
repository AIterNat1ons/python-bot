import time
import discord
from discord.ext import commands

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

        @commands.command(pass_context = True)
        async def join(self, ctx):
            channel = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(channel)

        @commands.command(pass_context = True)
        async def leave(self, ctx):
            server = ctx.message.author
            voice_client = client.voice_client_in(server)
            await voice_client.disconnect()

        








def setup(client):
    client.add_cog(Music(client))
