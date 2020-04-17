import os
import discord
import json
import random
import time
from discord.ext import commands

def get_prefix(client, message):
    with open('prefixes.json', 'r')as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = '.', case_insensitive = True)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.Game, name='with commands | .help'))
    print('Bot is online!')
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command wasn\'t found, make sure the command exists and check if it is spelled correctly.')  
        
async def create_db_pool():
    client.pg_con = await asyncpg.create_pool(database = 'levels', user = 'postgres', password = 'abdoullahstuff')
    
@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes [str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)
            

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
client.loop.run_until_complete(create_db_pool())

client.run(os.environ['TOKEN'])
