import time
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('mod.py has been loaded')

    @commands.command()
    @has_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 5):
     await ctx.channel.purge(limit = amount + 1)
     await ctx.send(f'Deleted {amount} messages')
     time.sleep(2)
     await ctx.channel.purge(limit = 1)

    @commands.command()
    @has_permissions(kick_members = True)
    async def kick (self, ctx, member : discord.Member, *, reason = None):
     await member.kick(reason = reason)
     await ctx.send(f'Successfully kicked {member.mention} for reason {reason}')

    @commands.command(name = 'ban')
    @has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.send(f'Successfully banned {member.mention} for reason {reason}') 

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'Sorry {ctx.message.author.mention}, you do not have permissions to do that!')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'Sorry {ctx.message.author.mention}, you do not have permissions to do that!')

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'Sorry {ctx.message.author.mention}, you do not have permissions to do that!')






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
