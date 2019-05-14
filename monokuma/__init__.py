# noinspection PyPackageRequirements
from discord.ext import commands
import random
from .assets import *
from .postgres import get_character, get_character_media
import logging

logger = logging.getLogger(__name__)

__author__ = "Charles Surett"

bot = commands.Bot(command_prefix="$")


@bot.command()
async def hello(ctx: commands.context.Context):
    """Say hello"""
    await ctx.send('I am Monokuma')


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
        await ctx.send(f"{c['first']} {c['last']}\n"
                       f"Gender: `{c['gender']}`\n"
                       # f"Height: `{ft} Feet, {i} Inches`\n"
                       # f"Born on: `{c.b_day[0]}-{c.b_day[1]}`\n"
                       f"Talent: `{c['talent']}`\n"
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
        await ctx.send(f"{c['first']} {c['last']}\n"
                       "Primary appearance in:\n"
                       f"`{c['media_name']}`"
                       )
    else:
        await ctx.send('I have no idea who that is. Phu phu phu.')


@bot.command()
async def bday(ctx: commands.context.Context, first_name: str):
    """
    Get's the remaining days to a character's birthday
    :param ctx:
    :param first_name: Character name
    """
    res = [x for x in characters if x.first_name.lower() == first_name.lower()]
    if res:
        c = res[0]
        await ctx.send(f'{c.first_name} {c.last_name} birthday is in {(c.next_birthday - date.today())}')
    else:
        await ctx.send('I have no idea who that is. Phu phu phu.')
