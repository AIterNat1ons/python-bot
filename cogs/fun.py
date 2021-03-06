
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
    async def slap(self, ctx, member : discord.Member):
        if member == ctx.author:
            await ctx.send('Silly you, trying to slap yourself don\'t do that!')
        else:
            slapways = [
                'https://media.giphy.com/media/vxvNnIYFcYqEE/giphy.gif',
                'https://media.giphy.com/media/AW8xRg8LNiR2g/giphy.gif',
                'https://media1.giphy.com/media/Y6c59hTH3TJoA/giphy.gif',
                'https://media2.giphy.com/media/uqSU9IEYEKAbS/giphy.gif',
                'https://media2.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif',
                'https://media1.tenor.com/images/b71b1ef1f8b26ff391d5fb372e90a27f/tenor.gif?itemid=11326073',
                'https://media.giphy.com/media/ylqr4JvFaZqnK/giphy.gif',
                'https://media2.giphy.com/media/tV0HkQju9zHR6/giphy.gif',
                'https://media2.giphy.com/media/YwxsiPgxjk3Fm/source.gif',
                'https://media0.giphy.com/media/10L38gtN2vVpgk/giphy.gif',
                'https://media2.giphy.com/media/11sV0mwXMM5sJi/giphy.gif',
                'https://media2.giphy.com/media/l0G18UUiIN9qhsR68/giphy.gif',
                'https://i.pinimg.com/originals/a0/dc/ce/a0dcce4e6eda2eba39d9f1fca82d32b6.gif',
                'https://media3.giphy.com/media/3oz8xF47ifDGuUALUk/giphy.gif',
                'https://media1.tenor.com/images/0d93bbf490dd498185c69d33825208d3/tenor.gif?itemid=13795345',
                'https://gifimage.net/wp-content/uploads/2017/07/anime-slap-gif-14.gif',
                'https://media1.tenor.com/images/8f2ac924c2cbb874236bd4db6dc7985c/tenor.gif?itemid=14841042'
            ]
            slapways = slapways
            slapembed = discord.Embed(
                title = 'Get slapped!',
                description = (f'{ctx.author.mention} brutally slapped {member.mention}.'),
                colour = discord.Colour.red()
            )
            slapembed.set_image(url = random.choice(slapways))
            await ctx.send(embed = slapembed)
    
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def rock(self, ctx):
        answers = [
            'rock',
            'paper',
            'scissors'
        ]
        answer = random.choice(answers)
        if answer == 'rock':
            await ctx.send('I picked rock, hmm seems like a draw!')

        if answer == 'paper':
            await ctx.send('I picked paper, hah I win!')

        if answer == 'scissors':
            await ctx.send('I picked scissors, rip I lost oh well congratulations!')
    
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def scissors(self, ctx):
        answers = [
            'rock',
            'paper',
            'scissors'
        ]
        answer = random.choice(answers)
        if answer == 'rock':
            await ctx.send('I picked rock, hah I win!')

        if answer == 'paper':
            await ctx.send('I picked paper, rip I lost oh well congratulations!')

        if answer == 'scissors':
            await ctx.send('I picked scissors, hmm seems like a draw!')

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def paper(self, ctx):
        answers = [
            'rock',
            'paper',
            'scissors'
        ]
        answer = random.choice(answers)
        if answer == 'rock':
            await ctx.send('I picked rock, rip I lost oh well congratulations!')

        if answer == 'paper':
            await ctx.send('I picked paper, hmm seems like a draw!')

        if answer == 'scissors':
            await ctx.send('I picked scissors, hah I win!')

    @commands.command(aliases = ['DP'])
    async def death_prediction(self, ctx, *, someone):
        years  = list(range(1, 101))
        waysofdeath = ['by lung disease',
        'by a disease',
        'from bacteria',
        'by lossing of breathe',
        'from drowning',
        'from someone murdering them',
        'by suicide',
        'by a heart attack',
        'by their family',
        'by a cooker',
        'from being in lava',
        'from getting shot',
        'by lossing blood',
        'by falling',
        'by getting cooked in the oven',
        'by electricuing yourself',
        'by giving birth']
        await ctx.send(f'{someone} will die in {random.choice(years)} year {random.choice(waysofdeath)}.')

    @commands.command(aliases = ['WP'])
    async def wife_prediction(self, ctx, *, someone):
        whetheryougonnagetmarried = ['yes', 'no']
        married = random.choice(whetheryougonnagetmarried)
        if married == 'yes':
            years  = list(range(1, 101))
            waysofdeath = ['a sexy womman',
            'a fat woman',
            'an ugly woman',
            'a woman with big boobs',
            'a woman with a huge ass',
            'a woman who will cheat on them',
            'a woman who hates them',
            'a woman who will murder them',]
            await ctx.send(f'{someone} will get married in {random.choice(years)} years by {random.choice(waysofdeath)}.')
        if married == 'no':
            await ctx.send(f'I\'m sorry but {someone} will not get married at all.')

    @commands.command(aliases = ['HP'])
    async def husband_prediction(self, ctx, *, someone):
        whetheryougonnagetmarried = ['yes', 'no']
        married = random.choice(whetheryougonnagetmarried)
        if married == 'yes':
            years  = list(range(1, 101))
            waysofdeath = [
            'a sexy man',
            'a fat man',
            'an ugly man',
            'a man with long penis',
            'a man with who will cheat on them',
            'a man who hates them',
            'a man who will murder them',]
            await ctx.send(f'{someone} will get married in {random.choice(years)} years by {random.choice(waysofdeath)}.')
        if married == 'no':
            await ctx.send(f'I\'m sorry but {someone} will not get married at all.')


    #errors
    @paper.error
    async def paper_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cooldownembed = discord.Embed(
                title = 'Chill out bro, slow it down',
                description = f'You\'ll be able to use the command in **{round(error.retry_after, 1)} seconds**\nThe default cooldown is `3s`',
                colour = discord.Colour.blue()
            )
            await ctx.send(embed = cooldownembed)
            
    @scissors.error
    async def scissors_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cooldownembed = discord.Embed(
                title = 'Chill out bro, slow it down',
                description = f'You\'ll be able to use the command in **{round(error.retry_after, 1)} seconds**\nThe default cooldown is `3s`',
                colour = discord.Colour.blue()
            )
            await ctx.send(embed = cooldownembed)
    
    @rock.error
    async def rock_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cooldownembed = discord.Embed(
                title = 'Chill out bro, slow it down',
                description = f'You\'ll be able to use the command in **{round(error.retry_after, 1)} seconds**\nThe default cooldown is `3s`',
                colour = discord.Colour.blue()
            )
            await ctx.send(embed = cooldownembed)

def setup(client):
    client.add_cog(Fun(client))
