import os
import discord
import random
import time
from discord.ext import commands

client = commands.Bot(command_prefix = '.')





for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['TOKEN'])
