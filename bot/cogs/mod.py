import time
import discord
from discord.ext import commands

class mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('mod.py has been loaded')

    @commands.command()
    async def clear(self, ctx, amount = 5):
     await ctx.channel.purge(limit = amount + 1)
     await ctx.send(f'Deleted {amount} messages')
     time.sleep(2)
     await ctx.channel.purge(limit = 1)

    @commands.command()
    async def kick (self, ctx, member : discord.Member, *, reason = None):
     await member.kick(reason = reason)
     await ctx.send(f'Successfully kicked {member.mention} for reason {reason}')

    @commands.command()
    async def ban (self, ctx, member : discord.Member, *, reason = None):
     await member.ban(reason = reason)
     await ctx.send(f'Successfully banned {member.mention} for reason {reason}')     

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send (f'Succesfully unbanned {user.mention}')
                return

def setup(client):
    client.add_cog(mod(client))
