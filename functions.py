import urllib

import discord
from youtubesearchpython import VideosSearch
SKILLS = ["Total", "Attack", "Defence", "Strength", "Constitution", "Ranged", "Prayer", "Magic",
          "Cooking", "Woodcutting", "Fletching", "Fishing", "Firemaking", "Crafting", "Smithing", "Mining",
          "Herblore", "Agility", "Thieving", "Slayer", "Farming", "Runecrafting", "Hunter", "Construction"]
CATEGORIES = ['ranks', 'levels', 'xp']

def getHiscore(category, names):
    """Gets the hiscore of a category and the respective username"""
    fullname = names[0]
    formatname = names[1]
    try:
        with urllib.request.urlopen(
                "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=" + formatname) as url:
            s = url.read()
    except Exception:
        return "error"
    output = apiOutputToDict(category, s)
    title = "Oldschool Hiscores of " + fullname
    desc = "These are the current "+category+" of " + fullname + ":"
    return dictToEmbed(title, desc, output)


def dictToEmbed(title, description, data, inline=True):
    """Formats a dictionary into a readable Embedded message for discord"""
    embedVar = discord.Embed(title=title, description=description, color=0x00ff00)
    for key,value in data.items():
        embedVar.add_field(name=key, value=value, inline=inline)
    return embedVar

def apiOutputToDict(category, json):
    """Puts the json output into a readable dictionary"""
    position = CATEGORIES.index(category)
    output = {}
    levels = json.decode().split("\n")
    for index, level in enumerate(levels):
        if index > (len(SKILLS) - 1): break
        categories = levels[index].split(",")
        formattednumber = "{:,}".format(int(categories[position]))
        output[SKILLS[index]] = formattednumber
    return output

def defineNames(name):
    """Puts multiple parameters into names that are able to be processed"""
    fullname = ''
    formatname = ''
    for x in name:
        if fullname == '':
            fullname = fullname + x
            formatname = formatname + x
        else:
            fullname = fullname + " " + x
            formatname = formatname + "+" + x
    return [fullname, formatname]

def findYT(quest):
    videosSearch = VideosSearch("slayermusiq1 osrs guide iron man " + quest, limit=1)
    return "https://www.youtube.com/watch?v=" + str(videosSearch.result()["result"][0]['id'])