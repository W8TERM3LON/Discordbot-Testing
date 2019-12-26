import discord
from discord.ext import commands
import asyncio
import datetime

class Find(commands.Cog):
     
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def remove(self, ctx, *, number:int=None):
        try:
            if number is None:
                await ctx.send('Number required....')
            else:
                deleted = await ctx.message.channel.purge(limit=number)
                await ctx.send(f'Messages purged by {ctx.message.author.mention}: `{len(deleted)}`')
        except:
            await ctx.send("ERROR")
    
def setup(bot):
    bot.add_cog(Find(bot))
    print('Loaded Find')