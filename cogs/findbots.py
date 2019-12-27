#import
import discord
from discord.ext import commands, tasks
import asyncio, aiohttp, re, time, datetime, json, os, requests
from itertools import cycle
#import aioschedule as schedule

#Query Data
accessToken = json.loads(open(os.path.join('', 'api.json')).read())

url = "https://graphql.anilist.co/"

#Grab last page
startpage = int(1)
initpayload = "{\"query\":\"query ($p: Int) {\\n  Page(page: $p) {\\n    pageInfo {\\n      total\\n      perPage: currentPage\\n      lastPage\\n      hasNextPage\\n    }\\n    users(sort: ID_DESC) {\\n      id\\n      \\n    }\\n  }\\n}\"}"
initheaders = {
    'content-type': "application/json",
        'authorization': "Bearer " + accessToken
  }
initresponse = requests.request("POST", url, data=initpayload, headers=initheaders)
initresponse = initresponse.json()
initresponse = initresponse.get('data',{})
initresponse = initresponse.get('Page', {})
initresponse = initresponse.get('pageInfo', {})
initresponse = initresponse.get('lastPage', {})
print('Stopping at page: ' + str(initresponse))
stoppage = int(initresponse)


class FindBot(commands.Cog):
     
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Find Bots Ready')

    @tasks.loop(seconds=5)
    async def find(self, ctx, bot):
        global startpage
        channel = bot.get_channel("641472789299331074")
        if startpage < 5:
            async with aiohttp.ClientSession():
                no = startpage
                payload = "{\"query\":\"query ($p: Int) {\\n  Page(page: $p) {\\n    users(sort: ID_DESC) {\\n      id\\n      about\\n      statistics{\\n        anime{\\n          count\\n        }\\n        manga{\\n          count\\n        }\\n      }\\n    }\\n  }\\n}\",\"variables\":{\"p\":" + str(no) + "}}"
                headers = {
                    'content-type': "application/json",
                        'authorization': "Bearer " + accessToken
                    }
                async with aiohttp.request("POST", url, data=payload, headers=headers) as resp:
                    resp = await resp.json()
                    resp = resp.get('data',{})
                    resp = resp.get('Page', {})
                    resp = resp.get('users', {})
                    for info in resp:
                        about = info.get('about')
                        ident = info.get('id')
                        about = str(about).casefold()
                        ident = str(ident)
                        if about == "none":
                            pass
                        else:
                            #add words by putting said word in single quotes.
                            slurs = [" "]
                            for keywords in slurs:
                                if keywords in about:
                                    await bot.send_message(channel, 'https://anilist.co/user/' + ident)
                                    await bot.send_message(channel, about)
            startpage = startpage + 1
        else:
            startpage = 1
    
    @commands.command()
    async def test(self, ctx):
        channel = bot.get_channel("641472789299331074")
        await bot.send_message(channel, 'Working....')

        
    
def setup(bot):
    bot.add_cog(FindBot(bot))
    print('Loaded Find Bots')