import os
import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import sys
import traceback

#load Discord token from .env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!!', case_insensitive=True)

@bot.event
async def on_ready():
    print('Online')
    return await bot.change_presence(activity=discord.Activity(name='AniList', type=0, state='Browsing.....', details='Testing', large_image_url='https://i.imgur.com/fqyhsZ5.png', small_image_url='https://i.imgur.com/fqyhsZ5.png', large_image_text='AniList', small_image_text='AniList'))

#initial_extensions = ['cogs.findbots', 'cogs.global-links', 'cogs.global-pictures', 'cogs.profile-banner', 'cogs.profile-image', 'cogs.profile-links']
#initial_extensions = ['cogs.Find', 'cogs.Global', 'cogs.Profile']
initial_extensions = ['cogs.findbots']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension: {extension}', file=sys.stderr)
            traceback.print_exc()

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def clear(ctx, *, number:int=None):
    try:
        if number is None:
            await ctx.send('Number required....')
        else:
            deleted = await ctx.message.channel.purge(limit=number)
            await ctx.send(f'{len(deleted)} Message(s) purged by {ctx.message.author.mention}')
    except:
        await ctx.send("ERROR")

bot.run(token)
