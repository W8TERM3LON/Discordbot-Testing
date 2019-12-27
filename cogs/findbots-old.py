#import
import discord
from discord.ext import commands, tasks
import asyncio, aiohttp, re, time, datetime, json, os
from itertools import cycle
import aioschedule as schedule

#Query Data
accessToken = json.loads(open(os.path.join('', 'api.json')).read())

no = 1

payload = "{\"query\":\"query ($p: Int) {\\n  Page(page: $p) {\\n    users(sort: ID_DESC) {\\n      id\\n      about\\n      statistics{\\n        anime{\\n          count\\n        }\\n        manga{\\n          count\\n        }\\n      }\\n    }\\n  }\\n}\",\"variables\":{\"p\":" + str(no) + "}}"
headers = {
    'content-type': "application/json",
        'authorization': "Bearer " + accessToken
  }

class FindBot(commands.Cog, name='FindBots'):
     
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Find Bots Ready')

    @tasks.loop(seconds=5)
    async def find(self):
        pass

        
    
def setup(bot):
    bot.add_cog(FindBot(bot))
    print('Loaded Find Bots')