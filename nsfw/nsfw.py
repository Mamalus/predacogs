import discord

from redbot.core import checks, commands
from redbot.core.i18n import Translator, cog_i18n

from typing import Union

from .core import Core
from . import constants as sub

_ = Translator("Nsfw", __file__)


@cog_i18n(_)
class Nsfw(Core, commands.Cog):
    """Send random NSFW images from random subreddits"""

    __author__ = ["Predä", "aikaterna", "Choco"]
    __version__ = "2.0.3"

    @commands.command()
    async def nsfwversion(self, ctx):
        """Get the version of the installed Nsfw cog"""

        await self._version_msg(ctx, self.__version__, self.__author__)

    @commands.command()
    async def nsfwhelp(self, ctx):
        """How to enable the command"""
        await ctx.send("You need the \"nsfw\" role to be able to use the commands. Ask the Admins or Moderators to give it to you.")


    @commands.command()
    @commands.has_role("nsfw")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cleandm(self, ctx, number: int):
        """
            Delete a number specified of DM's from the bot.

            `<number>`: Number of messages from the bot you want
            to delete in your DM's.
        """
        if ctx.guild:
            return await ctx.send(_("This command works only for DM's messages !"))
        async for message in ctx.channel.history(limit=number):
            if message.author.id == ctx.bot.user.id:
                await message.delete()
        await ctx.tick()

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(name="4k", aliases=["4K", "fourk"])
    async def four_k(self, ctx):
        """Show some 4k images from random subreddits."""

        await self._send_msg(ctx, _("4k"), sub=sub.FOUR_K)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["oface", "ofaces"])
    async def ahegao(self, ctx):
        """Show some ahegao images from random subreddits."""

        await self._send_msg(ctx, _("ahegao"), sub=sub.AHEGAO)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["butt", "booty"])
    async def ass(self, ctx):
        """Show some ass images from random subreddits."""

        await self._send_msg(ctx, _("ass"), sub=sub.ASS)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["sodomy"])
    async def anal(self, ctx):
        """Show some anal images/gifs from random subreddits."""

        await self._send_msg(ctx, _("anal"), sub=sub.ANAL)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["shibari"])
    async def bdsm(self, ctx):
        """Show some bdsm from random subreddits."""

        await self._send_msg(ctx, _("bdsm"), sub=sub.BDSM)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["blackdick", "bcock", "bdick", "blackcocks", "blackdicks"])
    async def blackcock(self, ctx):
        """Show some blackcock images from random subreddits."""

        await self._send_msg(ctx, _("black cock"), sub=sub.BLACKCOCK)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["blowjobs", "blowj", "bjob", "fellatio", "fellation"])
    async def blowjob(self, ctx):
        """Show some blowjob images/gifs from random subreddits."""

        await self._send_msg(ctx, _("blowjob"), sub=sub.BLOWJOB)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["boob", "boobies", "tits", "titties", "breasts", "breast"])
    async def boobs(self, ctx):
        """Show some boobs images from random subreddits."""

        await self._send_msg(ctx, _("boobs"), sub=sub.BOOBS)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["boless", "b_less"])
    async def bottomless(self, ctx):
        """Show some bottomless images from random subreddits."""

        await self._send_msg(ctx, _("bottomless"), sub=sub.BOTTOMLESS)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command()
    async def cosplay(self, ctx):
        """Show some nsfw cosplay images from random subreddits."""

        await self._send_msg(ctx, _("nsfw cosplay"), sub=sub.COSPLAY)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["cunni", "pussyeating"])
    async def cunnilingus(self, ctx):
        """Show some cunnilingus images from random subreddits."""

        await self._send_msg(ctx, _("cunnilingus"), sub=sub.CUNNI)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["cum", "cums", "cumshots"])
    async def cumshot(self, ctx):
        """Show some cumshot images/gifs from random subreddits."""

        await self._send_msg(ctx, _("cumshot"), sub=sub.CUMSHOTS)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["deept", "deepthroating"])
    async def deepthroat(self, ctx):
        """Show some deepthroat images from random subreddits."""

        await self._send_msg(ctx, _("deepthroat"), sub=sub.DEEPTHROAT)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["cock"])
    async def dick(self, ctx):
        """Show some dicks images from random subreddits."""

        await self._send_msg(ctx, _("dick"), sub=sub.DICK)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["doublep", "dpenetration", "doublepene", "doublepen"])
    async def doublepenetration(self, ctx):
        """Show some double penetration images/gifs from random subreddits."""

        await self._send_msg(ctx, _("double penetration"), sub=sub.DOUBLE_P)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["futanari"])
    async def futa(self, ctx):
        """Show some futa images from random subreddits."""

        await self._send_msg(ctx, _("futa"), sub=sub.FUTA)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["gpp"])
    async def gay(self, ctx):
        """Show some gay porn from random subreddits."""

        await self._send_msg(ctx, _("gay porn"), sub=sub.GAY_P)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["groups", "nudegroup", "nudegroups"])
    async def group(self, ctx):
        """Show some groups nudes from random subreddits."""

        await self._send_msg(ctx, "groups nudes", sub=sub.GROUPS)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["hentaigif"])
    async def hentai(self, ctx):
        """Show some hentai images/gifs from Nekobot API."""

        await self._send_msg_others(ctx, _("hentai"), api_category=["hentai_anal", "hentai"])

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["lesbians"])
    async def lesbian(self, ctx):
        """Show some lesbian gifs or images from random subreddits."""

        await self._send_msg(ctx, _("lesbian"), sub=sub.LESBIANS)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["milfs"])
    async def milf(self, ctx):
        """Show some milf images from random subreddits."""

        await self._send_msg(ctx, _("milf"), sub=sub.MILF)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["oralsex"])
    async def oral(self, ctx):
        """Show some oral gifs or images from random subreddits."""

        await self._send_msg(ctx, _("oral"), sub=sub.ORAL)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["pgif", "prongif"])
    async def porngif(self, ctx):
        """Show some porn gifs from Nekobot API."""

        await self._send_msg_others(ctx, _("porn gif"), api_category=["pgif"])

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["flashinggirl"])
    async def public(self, ctx):
        """Show some public nude images from random subreddits."""

        await self._send_msg(ctx, _("public nude"), sub=sub.PUBLIC)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["vagina", "puss"])
    async def pussy(self, ctx):
        """Show some pussy nude images from random subreddits."""

        await self._send_msg(ctx, _("pussy"), sub=sub.PUSSY)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command()
    async def realgirls(self, ctx):
        """Show some real girls images from random subreddits."""

        await self._send_msg(ctx, _("real nudes"), sub=sub.REAL_GIRLS)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["redheads", "ginger", "gingers"])
    async def redhead(self, ctx):
        """Show some red heads images from random subreddits."""

        await self._send_msg(ctx, _("red head"), sub=sub.REDHEADS)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["r34"])
    async def rule34(self, ctx):
        """Show some rule34 images from random subreddits."""

        await self._send_msg(ctx, _("rule34"), sub=sub.RULE_34)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["squirts"])
    async def squirt(self, ctx):
        """Show some squirts images from random subreddits."""

        await self._send_msg(ctx, _("squirt"), sub=sub.SQUIRTS)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["thighs", "legs"])
    async def thigh(self, ctx):
        """Show some thighs images from random subreddits."""

        await self._send_msg(ctx, _("thigh"), sub=sub.THIGHS)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["traps", "trans", "girldick", "girldicks", "shemale", "shemales"])
    async def trap(self, ctx):
        """Show some traps from random subreddits."""

        await self._send_msg(ctx, _("trap"), sub=sub.TRAPS)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["wild", "gwild"])
    async def gonewild(self, ctx):
        """Show some gonewild images from random subreddits."""

        await self._send_msg(ctx, _("gonewild"), sub=sub.WILD)

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_role("nsfw")
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["yiffs"])
    async def yiff(self, ctx):
        """Show some yiff images from random subreddits."""

        await self._send_msg(ctx, _("yiff"), sub=sub.YIFF)
