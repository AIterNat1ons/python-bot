import random
import discord
import time
import asyncio
import praw
from discord.ext import commands, tasks

reddit = praw.Reddit(client_id='rw9ObcZ3_5gE6Q',
                     client_secret='ens6sHopI8z6LHY5gcprwoC3ePY',
                     password='azzouz2005',
                     user_agent='testscript by /u/AIterNat1ons',
                     username='AIterNat1ons')

print(reddit.user.me())


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
            other.set_footer(text = 'If you are currently on mobile and the pfp hasn\'t loaded its a glitch within discord, I\'m sorry that it does not work.')
            await ctx.send(embed = other)
        else:
            embed=discord.Embed(color=discord.Colour.red())
            embed.set_image(url=member.avatar_url)
            embed.set_footer(text = 'If you are currently on mobile and the pfp hasn\'t loaded its a glitch within discord, I\'m sorry that it does not work.')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown( 1, 5, commands.BucketType.channel)
    async def meme(self, ctx):
        subreddits = ['dankmemes',
                    'memes',
                    'meirl',
                    'wholesomememes'
                    ]
        meme_submissions = reddit.subreddit(random.choice(subreddits)).hot()
        post_to_pick = random.randint(1, 10)
        await ctx.trigger_typing()
        for i in range(0, post_to_pick):
            i = i
            submission = next(x for x in meme_submissions if not x.stickied)
            submissionembed = discord.Embed(title = submission.title, colour = discord.Colour.red())
            submissionembed.set_image(url = submission.url)
            submissionembed.set_footer(text = f'r/{submission.subreddit}')
        await ctx.send(embed = submissionembed)

    @commands.command()
    @commands.cooldown( 1, 5, commands.BucketType.channel)
    async def cat(self, ctx):
        meme_submissions = reddit.subreddit('cats').hot()
        post_to_pick = random.randint(1, 10)
        await ctx.trigger_typing()
        for i in range(0, post_to_pick):
            i = i
            submission = next(x for x in meme_submissions if not x.stickied)
            submissioncembed = discord.Embed(title = submission.title, colour = discord.Colour.red())
            submissioncembed.set_image(url = submission.url)
            submissioncembed.set_footer(text = f'r/{submission.subreddit}')
        await ctx.send(embed = submissioncembed)

    @commands.command()
    @commands.cooldown( 1, 5, commands.BucketType.channel)
    async def minecraft_meme(self, ctx):
        meme_submissions = reddit.subreddit('MinecraftMemes').hot()
        post_to_pick = random.randint(1, 10)
        await ctx.trigger_typing()
        for i in range(0, post_to_pick):
            i = i
            submission = next(x for x in meme_submissions if not x.stickied)
            submissionmcembed = discord.Embed(title = submission.title, colour = discord.Colour.red())
            submissionmcembed.set_image(url = submission.url)
            submissionmcembed.set_footer(text = f'r/{submission.subreddit}')
        await ctx.send(embed = submissionmcembed)

    @commands.command()
    @commands.cooldown( 1, 5, commands.BucketType.channel)
    async def roblox_meme(self, ctx):
        meme_submissions = reddit.subreddit('ROBLOXmemes').hot()
        post_to_pick = random.randint(1, 10)
        await ctx.trigger_typing()
        for i in range(0, post_to_pick):
            i = i
            submission = next(x for x in meme_submissions if not x.stickied)
            submissionmcembed = discord.Embed(title = submission.title, colour = discord.Colour.red())
            submissionmcembed.set_image(url = submission.url)
            submissionmcembed.set_footer(text = f'r/{submission.subreddit}')
        await ctx.send(embed = submissionmcembed)

    @meme.error
    async def meme_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cooldownembed = discord.Embed(
                title = 'Chill out bro, slow it down',
                description = f'You\'ll be able to use the command in **{round(error.retry_after, 1)} seconds**\nThe default cooldown is `5s`',
                colour = discord.Colour.blue()
            )
            await ctx.send(embed = cooldownembed)

    @minecraft_meme.error
    async def minecraft_meme_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cooldownembed = discord.Embed(
                title = 'Chill out bro, slow it down',
                description = f'You\'ll be able to use the command in **{round(error.retry_after, 1)} seconds**\nThe default cooldown is `5s`',
                colour = discord.Colour.blue()
            )
            await ctx.send(embed = cooldownembed)

    @cat.error
    async def cat_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cooldownembed = discord.Embed(
                title = 'Chill out bro, slow it down',
                description = f'You\'ll be able to use the command in **{round(error.retry_after, 1)} seconds**\nThe default cooldown is `5s`',
                colour = discord.Colour.blue()
            )
            await ctx.send(embed = cooldownembed)

    @roblox_meme.error
    async def roblox_meme_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cooldownembed = discord.Embed(
                title = 'Chill out bro, slow it down',
                description = f'You\'ll be able to use the command in **{round(error.retry_after, 1)} seconds**\nThe default cooldown is `5s`',
                colour = discord.Colour.blue()
            )
            await ctx.send(embed = cooldownembed)
  








def setup(client):
    client.add_cog(Image(client))
