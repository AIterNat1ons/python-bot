import time
import discord
import youtube_dl
import asyncio
from discord.ext import commands

youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):

        def __init__(self, client):
            self.client = client


        @commands.Cog.listener()
        async def on_ready(self):
            print('music.py has been loaded')

        @commands.command(pass_context = True)
        async def join(self, ctx):
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send(f'Successfully joined {channel}.')

        @commands.command(pass_context = True)
        async def leave(self, ctx):
            await ctx.voice_client.disconnect()
            await ctx.send('Successfully left the voice channel.')

        @commands.command(pass_context=True)
        async def play(self, ctx, *, url):
            print(url)
            server = ctx.message.guild
            voice_client = server.voice_client
            voice_client = voice_client

            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop= self.client.loop)
                ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
            await ctx.send('Now playing: {}'.format(player.title))




        








def setup(client):
    client.add_cog(Music(client))
