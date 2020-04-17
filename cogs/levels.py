import random
import discord
import time
import asyncio
import json
import datetime
from discord.ext import commands, tasks

epoch = datetime.datetime.utcfromtimestamp(0)

class level(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('fun.py has been loaded')




    async def lvl_exp(self, user):
        cur_xp = user['exp']
        cur_lvl = user['level']

        if cur_xp >= round((4 * (cur_lvl ** 3)) / 5):
            await self.client.pg_con.execute("UPDATE users SET level = $1 WHERE user_id = $2 AND guild_id = $3", cur_lvl + 1, user['user_id'], user['guild_id'])
            return True
        else:
            return False


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == True:
            await asyncio.sleep(0.1)
        else:

            author_id = str(message.author.id)
            guild_id = str(message.guild.id)

            user = await self.client.pg_con.fetch("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)

            if not user:
                await self.client.pg_con.execute("INSERT INTO users (user_id, guild_id, level, exp, exp_time) VALUES ($1, $2, 0, 0, $3)", author_id, guild_id, (datetime.datetime.utcnow() - epoch).total_seconds())

            users = await self.client.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)
            time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - users['exp_time']
            if time_diff >= 30:
                user = await self.client.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)
                await self.client.pg_con.execute("UPDATE users SET exp = $1 WHERE user_id = $2 AND guild_id = $3", user['exp'] + 1, author_id, guild_id)
                await self.client.pg_con.execute("UPDATE users SET exp_time = $1 WHERE user_id = $2 AND guild_id = $3", (datetime.datetime.utcnow() - epoch).total_seconds(), author_id, guild_id)


                if await self.lvl_exp(user):
                    await message.channel.send(f"Congrats {message.author.mention}, you are now level {user['level'] + 1}")

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)
        guild_id = str(ctx.guild.id)
        user = await self.client.pg_con.fetch("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", member_id, guild_id)
        if not user:
            await ctx.send(f'{member} does not have a level yet!')
        else:
            embed = discord.Embed(title = f'{member} Level')
            embed.add_field(name='Level', value=user[0]['level'])
            embed.add_field(name='EXP', value=user[0]['exp'])
            embed.set_thumbnail(url = member.avatar_url)
            await ctx.send(embed = embed)


    

def setup(client):
    client.add_cog(level(client))