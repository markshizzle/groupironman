# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv
from functions import *
import random
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='ironman', help="Spams the sentence every iron man spams all day long.")
async def ironman(ctx):
    response = 'Iron Man Btw'
    await ctx.send(response)

@bot.command(name='quit', help="Type this if you want to quit Runescape")
async def quit(ctx):
    response = 'There is no quiting Runescape! Muhahahaha.'
    await ctx.send(response)

@bot.command(name='nice', help="nice")
async def nice(ctx):
    response = 'Nice.'
    await ctx.send(response)

@bot.command(name='leagueoflegends', help="Info about this shitty game")
async def leagueoflegends(ctx):
    response = 'Most toxic and frustrating game in the world, but as addicting as Runescape.'
    await ctx.send(response)

@bot.command(name='hiscore', help="!hiscore ranks/levels/xp username")
async def hiscore(ctx, category, *name):
    if category in CATEGORIES:
        names = defineNames(name)
        hiscore = getHiscore(category, names)
        if hiscore == 'error':
            await ctx.send("The player: **" + names[0] + "** can't be found in the hiscores.")
        else:
            await ctx.send(embed=hiscore)
    else:
        await ctx.send("Incorrect format. Choose between xp, levels or rank. Example: '!hiscore levels zezima' ")

@bot.command(name='guide', help="!guide (questname)")
async def guide(ctx, *quest):
    quest_name = defineNames(quest)
    ytlink = findYT(quest_name[0])
    await ctx.send(ytlink)

@bot.command(name="joke", help="Randomly tells a joke, try it!")
async def joke(ctx):
    await ctx.send(random.choice(JOKES))

bot.run(TOKEN)
