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
            await ctx.send(embed = other)
        else:
            embed=discord.Embed(color=discord.Colour.red())
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed = embed)

    @commands.command()
    async def meme(self, ctx):
        meme_submissions = reddit.subreddit('Dankmemes').hot()
        post_to_pick = random.randint(1, 10)
        await ctx.trigger_typing()
        for i in range(0, post_to_pick):
            i = i
            submission = next(x for x in meme_submissions if not x.stickied)
            submissionembed = discord.Embed(colour = discord.Colour.red())
            submissionembed.set_image(url = submission.url)
        await ctx.send(embed = submissionembed)

    








def setup(client):
    client.add_cog(Image(client))
