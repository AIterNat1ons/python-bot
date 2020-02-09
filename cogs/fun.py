import discord
import random
import time
import asyncio
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
          print ('fun.py has been loaded')

    #8ball command    
    @commands.command(aliases = ['8ball'])
    async def _8ball(self, ctx, *, question ):
        responses = [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
        await ctx.send (f'Question: {question} \nAnswer: {random.choice(responses)}')

    @commands.command()
    async def count(self, ctx):
     message = await ctx.send('10 seconds')
     await asyncio.sleep(1)
     await message.edit(content ='9 seconds')
     await asyncio.sleep(1)
     await message.edit(content ='8 seconds')
     await asyncio.sleep(1)
     await message.edit(content ='7 seconds')
     await asyncio.sleep(1)
     await message.edit(content ='6 seconds')
     await asyncio.sleep(1)
     await message.edit(content ='5 seconds')
     await asyncio.sleep(1)
     await message.edit(content ='4 seconds')
     await asyncio.sleep(1)
     await message.edit(content ='3 seconds')
     await asyncio.sleep(1)
     await message.edit(content ='2 seconds')
     await asyncio.sleep(1)
     await message.edit(content ='1 seconds')
     await asyncio.sleep(1)
     await message.edit(content ='0 seconds')
    

    
    


def setup(client):
    client.add_cog(Fun(client))
