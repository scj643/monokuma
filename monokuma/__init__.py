# noinspection PyPackageRequirements
from discord.ext import commands
# noinspection PyPackageRequirements
import discord
import random
from .assets import *
from .postgres import get_character, get_character_media, list_characters, get_db, get_character_next_bday
import re
import logging
import os

logger = logging.getLogger(__name__)

__author__ = "Charles Surett"

bot = commands.Bot(command_prefix="$")


@bot.command()
async def hello(ctx: commands.context.Context):
    """Say hello"""
    await ctx.send('I am Monokuma')


@bot.command()
async def role_sub(ctx: commands.context.Context, role: discord.Role):
    """
    Subscribe to a role
    :param ctx:
    :param role: Role name to subscribe to
    :return:
    """
    if role in ctx.author.roles:
        await ctx.author.remove_roles(role)
        await ctx.send(f'Unsubscribed from {role.name}')
    else:
        await ctx.author.add_roles(role)
        await ctx.send(f'Subscribed to {role.name}')


@bot.command()
async def about(ctx: commands.context.Context):
    """
    About the bot
    :param ctx: The context object
    """
    await ctx.send(f'Created by: {__author__}\n'
                   f'Github: https://github.com/scj643/monokuma')


@bot.command()
async def quote(ctx: commands.context.Context):
    """
    Gives a random Monokuma quote.
    """
    await ctx.send(random.choice(MONOKUMA_QUOTES))


@bot.command()
async def char(ctx: commands.context.Context, first_name: str):
    """
    Returns a character's info based on there name.
    :param ctx:
    :param first_name: Name to look up. Is lowered before checking
    """
    res = await get_character(first_name)
    if res:
        c = res[0]
        await ctx.send(f"{c['first_name']} {c['last_name']}\n"
                       f"Gender: `{c['gender']}`\n"
                       # f"Height: `{ft} Feet, {i} Inches`\n"
                       # f"Born on: `{c.b_day[0]}-{c.b_day[1]}`\n"
                       f"Talent: `{c['talent']}`\n"
                       f"Kanji: `{c['kanji']}`"
                       # f"Main Game: `{c.main_game}`")
                       )
    else:
        await ctx.send('I have no idea who that is. Phu phu phu.')


@bot.command()
async def media(ctx: commands.context.Context, name: str):
    """
    Returns the media which a character appears in
    :param ctx:
    :param name: Name to look up. Is lowered before checking
    """
    res = await get_character_media(name)
    if res:
        c = res[0]
        await ctx.send(f"{c['first_name']} {c['last_name']}\n"
                       "Primary appearance in:\n"
                       f"`{c['media_name']}`"
                       )
    else:
        await ctx.send('I have no idea who that is. Phu phu phu.')


@bot.command()
async def bday(ctx: commands.context.Context, name: str):
    """
    Get's the remaining days to a character's birthday
    :param ctx:
    :param name: Character name
    """
    res = await get_character_next_bday(name)
    sql_regex = re.compile(' [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6}')
    if res:
        await ctx.send(sql_regex.split(res[0][0])[0])
    else:
        await ctx.send('I have no idea who that is. Phu phu phu.')


@bot.command()
async def lschar(ctx: commands.context.Context):
    """
    List all known characters
    :param ctx:
    :return:
    """
    res = await list_characters()
    if res:
        char_string = ''
        for i in res:
            char_string += f'{i["first_name"]} {i["last_name"]}\n'
        await ctx.send(char_string)


if os.environ.get("DEBUG"):
    @bot.command()
    async def curdb(ctx: commands.context.Context):
        """
        Get the current database
        :param ctx:
        :return:
        """
        res = await get_db()
        await ctx.send(res)
