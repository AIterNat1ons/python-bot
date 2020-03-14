import time
import discord
import youtube_dl
import asyncio
from discord.ext import commands
songs = asyncio.Queue()
play_next_song = asyncio.Event()
queues = {}

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

        async def audio_player_task(self, client):
            while True:
                play_next_song.clear()
                current = await queues[id].get()
                current.start()
                await play_next_song.wait()

        def toggle_next(self, client):
            client.loop.call_soon_threadsafe(play_next_song.set)
            

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
            try:
                await ctx.voice_client.disconnect()
                await ctx.send('Successfully left the voice channel.')
            except:
                await ctx.send('I\'m not in a voice channel for me to leave.')
            

        @commands.command(aliases = ['p'])
        async def play(self, ctx, *, song):
                queues[ctx.author.guild.id] = songs
                print(song)
                server = ctx.message.guild
                voice_client = server.voice_client
                voice_client = voice_client
                embed = discord.Embed(
                title = 'Music',
                description = (f'Loading \'{song}\''),
                colour = discord.Colour.purple()
                )
                embed.set_thumbnail(url = 'https://media.giphy.com/media/pgnxJGob9PQQ0/giphy.gif')
                embed.set_author(name = ctx.author.name,
                icon_url= ctx.author.avatar_url)
                try:
                    channel = ctx.author.voice.channel
                    await channel.connect()
                    message = await ctx.send(embed = embed)
                    player = await YTDLSource.from_url(song, loop= self.client.loop)
                    ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
                    loaded = discord.Embed(
                    title = 'Music',
                    description = ('Now playing: {}'.format(player.title)),
                    colour = discord.Colour.green()
                    )
                    loaded.set_thumbnail(url = 'https://media1.tenor.com/images/b0dd371498f7ea7ca14a9165f2e9711f/tenor.gif?itemid=8958511')
                    loaded.set_author(name = ctx.author.name,
                    icon_url= ctx.author.avatar_url)
                    await message.edit(embed = loaded)
                except:
                    message = await ctx.send(embed = embed)
                    player = await YTDLSource.from_url(song, loop= self.client.loop)
                    ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
                    loaded = discord.Embed(
                    title = 'Music',
                    description = ('Now playing: {}'.format(player.title)),
                    colour = discord.Colour.green()
                    )
                    loaded.set_thumbnail(url = 'https://media1.tenor.com/images/b0dd371498f7ea7ca14a9165f2e9711f/tenor.gif?itemid=8958511')
                    loaded.set_author(name = ctx.author.name,
                    icon_url= ctx.author.avatar_url)
                    await message.edit(embed = loaded)

        @commands.command()
        async def stop(self, ctx):
            server = ctx.message.guild
            voice_client = server.voice_client
            voice_client = voice_client
            try:
                if ctx.voice_client.is_playing():
                    ctx.voice_client.stop()
                    await ctx.send('I have successfully stopped the music for you.')
                else:
                    await ctx.send('Nothing is playing for me to stop.')                        
            except:
                await ctx.send('I am not in a voice channel!')

        @commands.command()
        async def pause(self, ctx):
            server = ctx.message.guild
            voice_client = server.voice_client
            voice_client = voice_client
            try:
                if ctx.voice_client.is_playing():
                    ctx.voice_client.pause()
                    await ctx.send('I have successfully paused the music for you.')
                else:
                    await ctx.send('Nothing is playing for me to pause.')                        
            except:
                await ctx.send('I am not in a voice channel!')     

        @commands.command()
        async def resume(self, ctx):
            server = ctx.message.guild
            voice_client = server.voice_client
            voice_client = voice_client
            try:
                if not ctx.voice_client.is_playing():
                    ctx.voice_client.resume()
                    await ctx.send('I have successfully resumed the music for you.')
                else:
                    await ctx.send('No need to resume, I am already playing something.')                        
            except:
                await ctx.send('I am not in a voice channel!')   

         





        








def setup(client):
    client.add_cog(Music(client))
