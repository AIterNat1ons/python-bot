
import random
import discord
import time
import asyncio
from discord.ext import commands, tasks


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
        for8ball = discord.Embed(
        title = '8ball',
        description = (f'Question: {question} \nAnswer: {random.choice(responses)}'),
        colour = discord.Colour.orange()
            )
        for8ball.set_thumbnail(url = 'https://p7.hiclipart.com/preview/90/451/830/magic-8-ball-8-ball-pool-eight-ball-crystal-ball-8.jpg')
        for8ball.set_author(name = ctx.author.name,
        icon_url= ctx.author.avatar_url)
        await ctx.send(embed = for8ball)

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

    @commands.command(aliases = ['howgay'])
    async def gayrate(self, ctx, *, person):
        answer = [
        '1%',
        '2%',
        '3%',
        '4%',
        '5%',
        '6%',
        '7%',
        '8%',
        '9%',
        '10%',
        '11%',
        '12%',
        '13%',
        '14%',
        '15%',
        '16%',
        '17%',
        '18%',
        '19%',
        '20%',
        '21%',
        '22%',
        '23%',
        '24%',
        '25%',
        '26%',
        '27%',
        '28%',
        '29%',
        '30%',
        '31%',
        '32%',
        '33%',
        '34%',
        '35%',
        '36%',
        '37%',
        '38%',
        '39%',
        '40%',
        '41%',
        '42%',
        '43%',
        '44%',
        '45%',
        '46%',
        '47%',
        '48%',
        '49%',
        '50%',
        '51%',
        '52%',
        '53%',
        '54%',
        '55%',
        '56%',
        '57%',
        '58%',
        '59%',
        '60%',
        '61%',
        '62%',
        '63%',
        '64%',
        '65%',
        '66%',
        '67%',
        '68%',
        '69%',
        '70%',
        '72%',
        '73%',
        '74%',
        '75%',
        '76%',
        '77%',
        '78%',
        '79%',
        '80%',
        '81%',
        '82%',
        '83%',
        '84%',
        '85%',
        '86%',
        '87%',
        '88%',
        '89%',
        '90%',
        '91%',
        '92%',
        '93%',
        '94%',
        '95%',
        '96%',
        '97%',
        '98%',
        '99%',
        '100%'
        ]
        embed = discord.Embed(
        title = 'Gayrate',
        description = (f'{person} is {random.choice(answer)} gay'),
        colour = discord.Colour.blue()
            )
        embed.set_thumbnail(url = 'https://i.pinimg.com/originals/d3/18/69/d31869ab8d293ba04af2e3cb6d4d1973.jpg')
        embed.set_author(name = ctx.author.name,
        icon_url= ctx.author.avatar_url)
        await ctx.send(embed = embed)

    @commands.command()
    async def penis(self, ctx, *, someone = None):
        penisize = [
        '8D',
        '8=D',
        '8==D',
        '8===D',
        '8====D',
        '8=====D',
        '8======D',
        '8=======D',
        '8========D',
        '8=========D',
        '8==========D',
        '8===========D',]

        if someone == None:
            someone = ctx.message.author.mention

        penisembed = discord.Embed(
        title = 'Penis size machine',
        description = (f'{someone} penis size: \n{random.choice(penisize)}'),
        colour = discord.Colour.red()
        )
        penisembed.set_author(name = ctx.author.name,
        icon_url = ctx.author.avatar_url)
        await ctx.send(embed = penisembed)
    
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
    client.add_cog(Fun(client))
