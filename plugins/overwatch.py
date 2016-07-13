import aiohttp
from discord.ext import commands

class OverWatch:

    def __init__(self, bot):
        self.bot = bot
        self.baseurl = 'https://owapi.net/api/v2/u/'

    @commands.command(pass_context=True, description="Shows overwatch stats", name="ow")
    async def stats(self, ctx, *, battletag: str):
        with aiohttp.ClientSession() as session:
            async with session.get(self.baseurl + battletag + '/stats/general') as response:
                try:
                    assert response.url == 'https://owapi.net/api/v2/u/' + battletag + '/stats/general'
                    stats = await response.json()
                    await self.bot.say('```BattleTag: {}\nRegion: {}\nLevel: {}\nGames Played: {}\nLosses: {}\nWins: {}\nRank: {}\nWin Rate: {}```'.format(stats['battletag'], stats['region'], stats['overall_stats']['level'], stats['overall_stats']['games'], stats['overall_stats']['losses'], stats['overall_stats']['wins'], stats['overall_stats']['comprank'], stats['overall_stats']['win_rate']))
                except KeyError:
                    await self.bot.say('```404 Error. BattleTag not found (BattleTags are case sensitive, check that if you haven\'t!```')


def setup(bot):
    bot.add_cog(OverWatch(bot))
