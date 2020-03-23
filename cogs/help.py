import random
import discord
import time
import asyncio
from discord.ext import commands, tasks


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
          print ('help.py has been loaded')

    @commands.command()
    async def help(self, ctx, number = None):
        if number == None:
            helpembed = discord.Embed(
                title = '**Categories**',
                description = '**fun\nmusic\nimage \nconfig \nmod**'
            )
            helpembed.set_footer(text = 'These are the categories for the bot, if you want more information on the category do .help <category>.')
            await ctx.send(embed = helpembed)
        if number == 'fun':
            funhelpembed = discord.Embed(
                title = '**Fun Commands!**',
                description = '**8ball**: 8ball is a mysterious balls which will answer your yes or no question ask it any question by doing this .8ball <question>! \n**gayrate**: This will rate how gay you are or someone you specify. To do this do .gayrate <person>! \n**penis**: This will tell you how long your penis is using a machine. To do this you do .penis <person>! \n**count**: This will count down from 10 all the way to 0. \n**slap**: Slap the person you would like to slap by specifying a member. \n**rock**: Playing rock paper scissors with the bot using rock and see if you win! \n**paper**: Playing rock paper scissors with the bot using paper and see if you win! \n**scissors**: Playing rock paper scissors with the bot using scissors and see if you win!'
            )
            funhelpembed.set_footer(text = 'This is only commands for the category \'fun\', if you want to see the rest of the categories type in only .help.')
            await ctx.send(embed = funhelpembed)

        if number == 'config':
            confighelpembed = discord.Embed(
                title = '**Config Commands!**',
                description = '**addrole**: Adds a role that you specify by .addrole <name> <song>! \n**ping**: Shows the ping of the bot!'
            )
            confighelpembed.set_footer(text = 'This is only commands for the category \'config\', if you want to see the rest of the categories type in only .help.')
            await ctx.send(embed = confighelpembed)

        if number == 'mod':
            modhelpembed = discord.Embed(
                title = '**Mod Commands!**',
                description = '**kick**: Kicks the user who you specify by .kick <member> <reason>. \n**ban**: Bans the user who you specify by .ban <member> <reason>. \n**clear**: Clears an amount of messages you specify by .clear <amount>. \n**unban**: Unbans the user that has been banned by doing .unban <member>.'
            )
            modhelpembed.set_footer(text = 'This is only commands for the category \'mod\', if you want to see the rest of the categories type in only .help.')
            await ctx.send(embed = modhelpembed)

        if number == 'image':
            imagehelpembed = discord.Embed(
                title = '**Image Commands!**',
                description = '**pfp**: Shows either your pfp or a specified user\'s pfp by doing .pfp <member>. \n**meme**: The bot will show you a random meme from reddit. \n**minecraft_meme**: This will show you a random minecraft meme from reddit! \n**roblox_meme**: This will show you a random roblox meme from reddit! \n**cat**: This will show you a random cat meme from reddit! \n**motivate_me**: This will get you motivated with some inspirational quotes!'
            )
            imagehelpembed.set_footer(text = 'This is only commands for the category \'image\', if you want to see the rest of the categories type in only .help.')
            await ctx.send(embed = imagehelpembed)

        if number == 'music':
            imagehelpembed = discord.Embed(
                title = '**Music Commands!**',
                description = '**play**: This will play a music in the channel you are in by doing .play <song>. \n**stop**: This will stop the music that\'s playing and will leave the voice channel. \n**pause**: This will pause the music that is currently playing in the music player. \n**resume**: This will resume the currently stopped music. \n**join**: This will join the music channel that you are in! \n**queue**: This will show you the upcoming queued songs! \n**volume**: This will change the volume of the music in percentages. \n**skip**: Skips the current music playing. \n**now_playing**: This will show you the current playing music.'
            )
            imagehelpembed.set_footer(text = 'This is only commands for the category \'music\', if you want to see the rest of the categories type in only .help.')
            await ctx.send(embed = imagehelpembed)










def setup(client):
    client.add_cog(Help(client))
