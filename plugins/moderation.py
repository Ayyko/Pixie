from discord.ext import commands


def is_owner(ctx):
    with open('setup.json') as file:
        setup = json.load(file)
        return ctx.message.author.id == setup['ownerid']


class Moderation:

    def __init__(self, bot):
        self.bot = bot

    @commands.check(is_owner)
    @commands.command(pass_context=True, description="Allows mass deletion of messages", name="purge")
    async def purge(self, ctx, *, limit: int):
        try:
            await self.bot.purge_from(ctx.message.channel, limit=limit, before=ctx.message)
            await self.bot.say("```{} messages deleted.```".format(limit))
        except PermissionError:
            await self.bot.say('```Manage messages permission needed.```')

    @commands.check(is_owner)
    @commands.command(pass_context=True, description="Allows bans to be done through a bot", name="ban")
    async def ban_member(self, ctx, bannedfor, *, reason:  str):
        try:
            await self.bot.ban(ctx.message.mentions[0], delete_message_days=1)
            await self.bot.say('```{} has been banned for {}```'.format(bannedfor, reason))
        except:
            await self.bot.say('```Ban failed. Check permissions.```')

    @commands.check(is_owner)
    @commands.command(pass_context=True, description="Allows user to be kicked from server via bot command", name="kick")
    async def kick_member(self, ctx):
        await self.bot.kick(ctx.message.mentions[0])


def setup(bot):
    bot.add_cog(Moderation(bot))
