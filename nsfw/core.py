import discord

import aiohttp
import asyncio
import random
import json

from redbot.core import commands, Config

from .subs import EMOJIS
from . import subs

BASE_URL = "https://api.reddit.com/r/"
ENDPOINT = "/random"

IMGUR_LINKS = "http://imgur.com", "https://m.imgur.com", "https://imgur.com"
GOOD_EXTENSIONS = ".png", ".jpg", ".jpeg", ".gif"

class Functions:
    def __init__(self, bot):
        self.bot = bot
        self.ctx = commands.Context
        self.config = Config.get_conf(self, 3329804706503720962, force_registration=True)
        default_guild = {"channel_id": None, "enabled": False}
        self.config.register_guild(**default_guild)
        self.session = aiohttp.ClientSession()

    async def _autoporn_channel(self, ctx, channel=None):
        enabled = await self.config.guild(ctx.guild).enabled()
        if not enabled:
            if channel is None:
                channel = ctx.message.channel
            if channel.is_nsfw() == True:
                await self.config.guild(ctx.guild).channel_id.set(channel.id)
                await self.config.guild(ctx.guild).enabled.set(True)
                await ctx.send(f"Autoporn enabled in : <#{channel.id}>.")
            else:
                return await ctx.send("Autoporn can be enabled only in NSFW channels.")
        elif enabled and channel:
            if channel.is_nsfw() == True:
                await self.config.guild(ctx.guild).channel_id.set(channel.id)
                await self.config.guild(ctx.guild).enabled.set(True)
                await ctx.send(f"Autoporn channel changed to : <#{channel.id}>.")
            else:
                return await ctx.send("Autoporn can be enabled only in NSFW channels.")
        else:
            await self.config.guild(ctx.guild).channel_id.set(None)
            await self.config.guild(ctx.guild).enabled.set(False)
            await ctx.send(
                f"Autoporn disabled. Use `{ctx.prefix}autoporn` command again to get back autoporn."
            )

    # TODO: Use something different for getting images, like caching.
    # Or maybe not ? Works well now without ctx.invoke.
    async def _get_imgs(self, ctx, sub=None, url=None, subr=None):
        csub = random.choice(sub)
        async with self.session.get(BASE_URL + csub + ENDPOINT) as reddit:
            try:
                data = await reddit.json(content_type=None)
                content = data[0]["data"]["children"][0]["data"]
                url = content["url"]
                subr = content["subreddit"]
                text = content["selftext"]
            except (KeyError, ValueError, json.decoder.JSONDecodeError):
                url, subr, text = await self._get_imgs(ctx, sub=sub, url=url)
            if url.startswith(IMGUR_LINKS):
                url = url + ".png"
            if url.endswith(".mp4"):
                url = url[:-3] + "gif"
            if url.endswith(".gifv"):
                url = url[:-1]
            if (
                text
                or not url.endswith(GOOD_EXTENSIONS)
                and not url.startswith("https://gfycat.com")
            ):
                url, subr = await self._get_imgs(ctx, sub=sub, url=url)
        return url, subr

    async def _nsfw_channel_check(self, ctx, embed=None):
        if ctx.message.channel.is_nsfw() == False:
            embed = discord.Embed(
                title="\N{LOCK} You can't use that command in a non-NSFW channel !", color=0xAA0000
            )
        return embed

    async def _emojis(self, emoji=None):
        emoji = random.choice(EMOJIS)
        return emoji

    async def _make_embed(self, ctx, subr, name, url):
        emoji = await self._emojis(emoji=None)
        em = discord.Embed(
            color=0x891193,
            title="Here is {name} image ... \N{EYES}".format(name=name),
            description="[**Link if you don't see image**]({url})".format(url=url),
        )
        em.set_footer(
            text="Requested by {req} {emoji} • From r/{r}".format(
                req=ctx.author.display_name, emoji=emoji, r=subr
            )
        )
        if url.endswith(GOOD_EXTENSIONS):
            em.set_image(url=url)
        if url.startswith("https://gfycat.com"):
            em = "Here is {name} gif ... \N{EYES}\n\nRequested by **{req}** {emoji} • From **r/{r}**\n{url}".format(
                name=name, req=ctx.author.display_name, emoji=emoji, r=subr, url=url
            )
        return em

    async def _make_embed_others(self, ctx, name, api_category=None):
        api = subs.NEKOBOT_BASEURL + random.choice(api_category)
        async with self.session.get(api) as i:
            data = await i.json(content_type=None)
            url = data["message"]
            emoji = await self._emojis(emoji=None)
            if ctx.guild:
                if ctx.message.channel.is_nsfw() == True:
                    em = discord.Embed(
                        color=0x891193,
                        title="Here is {name} image ... \N{EYES}".format(name=name),
                        description="[**Link if you don't see image**]({url})".format(url=url),
                    )
                    em.set_image(url=url)
                    em.set_footer(
                        text="Requested by {req} {emoji} • From Nekobot API".format(
                            req=ctx.author.display_name, emoji=emoji
                        )
                    )
                else:
                    em = await self._nsfw_channel_check(ctx)
            else:
                em = discord.Embed(
                    color=0x891193,
                    title="Here is {name} image ... \N{EYES}".format(name=name),
                    description="[**Link if you don't see image**]({url})".format(url=url),
                )
                em.set_image(url=url)
                em.set_footer(
                    text="Requested by {req} {emoji} • From Nekobot API".format(
                        req=ctx.author.display_name, emoji=emoji
                    )
                )
            return await ctx.send(embed=em)

    async def _make_embed_autoporn(self, ctx, subr, name, url):
        emoji = await self._emojis(emoji=None)
        em = discord.Embed(
            color=0x891193,
            title="Here is {name} image ... \N{EYES}".format(name=name),
            description="[**Link if you don't see image**]({url})".format(url=url),
        )
        em.set_footer(
            text="From r/{r} {emoji}".format(
                r=subr, emoji=emoji
            )
        )
        if url.endswith(GOOD_EXTENSIONS):
            em.set_image(url=url)
        if url.startswith("https://gfycat.com"):
            em = "Here is {name} gif ... \N{EYES}\nFrom **r/{r}** {emoji}\n{url}".format(
                name=name, r=subr, emoji=emoji, url=url
            )
        return em

    async def _maybe_embed(self, ctx, embed):
        if type(embed) == discord.Embed:
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed)

    async def _send_msg(self, ctx, name, sub=None, subr=None):
        async with ctx.typing():
            if ctx.guild:
                if ctx.message.channel.is_nsfw() == True:
                    url, subr = await self._get_imgs(ctx, sub=sub, url=None, subr=None)
                    embed = await self._make_embed(ctx, subr, name, url)
                else:
                    embed = await self._nsfw_channel_check(ctx)
            else:
                url, subr = await self._get_imgs(ctx, sub=sub, url=None, subr=None)
                embed = await self._make_embed(ctx, subr, name, url)
        await self._maybe_embed(ctx, embed=embed)

    async def _maybe_send_autoporn(self, ctx, name, guild=None, sub=None, subr=None):
        # await self.bot.wait_until_ready()
        # while self == self.bot.get_cog("Nsfw"):
        while True:
            enabled = await self.config.guild(guild).enabled()
            if enabled == True:
                async with ctx.typing():
                    url, subr = await self._get_imgs(ctx, sub=sub, url=None, subr=None)
                    embed = await self._make_embed_autoporn(ctx, subr, name, url)
                try:
                    await self._maybe_embed(ctx, embed=embed)
                    await asyncio.sleep(random.randint(5, 10)) # Low ints for tests.
                except:
                    break
            else:
                break


    def __unload(self):
        self.bot.loop.create_task(self.session.close())
