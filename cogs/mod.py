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
    async def clear(self, ctx, amount : int):
     await ctx.channel.purge(limit = amount + 1)
     await ctx.send(f'Deleted {amount} messages', delete_after = 1)


    @commands.command()
    @has_permissions(kick_members = True)
    async def kick (self, ctx, member : discord.Member, *, reason = None):
     await member.kick(reason = reason)
     await ctx.send(f'Successfully kicked {member.mention} for reason {reason}')

    @commands.command()
    @has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.send(f'Successfully banned {member.mention} for reason {reason}') 

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'Sorry {ctx.message.author.mention}, you do not have permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to specify a member to kick somebody!')
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'Sorry {ctx.message.author.mention}, you do not have permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to specify a member to ban somebody!')
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'Sorry {ctx.message.author.mention}, you do not have permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to specify an amount of number to be able to delete messages!')





    @commands.command()
    @has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send (f'Succesfully unbanned {user.mention}')
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('The member was either not found or they are not banned!')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to specify a member to unban somebody!')


def setup(client):
    client.add_cog(mod(client))
