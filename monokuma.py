from discord.ext import commands
import random

__author__ = "Charles Surett"

MONOKUMA_QUOTES = ["It's the Monokuma File!", "I am Monokuma!"]

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


if __name__ == '__main__':
    with open('api_token', 'r') as f:
        token = f.read()
    print('starting')
    bot.run(token)
