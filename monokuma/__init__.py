# noinspection PyPackageRequirements
from discord.ext import commands
import random
from monokuma.assets import *

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
    await ctx.send('Created by: {}\n'
                   'Github: https://github.com/scj643/monokuma'.format(__author__))


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
    res = [x for x in characters if x.first_name.lower() == first_name.lower()]
    if res:
        c = res[0]
        f, i = to_feet(c.height)
        await ctx.send("{first} {last}\n"
                       "Gender: `{gender}`\n"
                       "Height: `{ft} Feet, {inch} Inches`\n"
                       "Born on: `{month}-{day}`\n"
                       "Talent: `{talent}`\n"
                       "Blood Type: `{bt}`\n"
                       "Main Game: `{mg}`".format(first=c.first_name, last=c.last_name, gender=c.gender,
                                                  ft=f, inch=i, month=c.b_day[0],
                                                  day=c.b_day[1], talent=c.talent, bt=c.blood_type, mg=c.main_game))
    else:
        await ctx.send('I have no idea who that is. Phu phu phu.')


if __name__ == '__main__':
    with open('api_token', 'r') as f:
        token = f.read()
    print('starting')
    bot.run(token)
