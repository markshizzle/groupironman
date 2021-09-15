import urllib

import discord
from youtubesearchpython import VideosSearch
SKILLS = ["Total", "Attack", "Defence", "Strength", "Constitution", "Ranged", "Prayer", "Magic",
          "Cooking", "Woodcutting", "Fletching", "Fishing", "Firemaking", "Crafting", "Smithing", "Mining",
          "Herblore", "Agility", "Thieving", "Slayer", "Farming", "Runecrafting", "Hunter", "Construction"]
CATEGORIES = ['ranks', 'levels', 'xp']
JOKES = [
    "I saw someone killing red spiders a few years ago and reported him for bug abuse.",
    "Your momma's so fat she's got enough chins for 99 range",
    "One time I typed runescape into Microsoft word and it told me to change it to 'run escape' 5 years later... 300 days of game play..I should have listened.",
    "Instead of water boarding, the US government should make the terrorists catch hell rats with a kitten.",
    "Yo momma so fat a Dragon Halbert spec hits her three times",
    "Yo momma is like the Al Kharid gate, only 10 gp to enter",
    "Q: How many runescape players does it take to change a light bulb? A: 50, 1 to change it and the rest to complain about how the old one was better.",
    "Hey girl, are u 99 Farming because ur making me grow.",
    "Hey baby, you turn my dds into a dlong",
    "Aye baby, you get 99 herblore? Cause you took all my money.",
    "Yo momma so fat she takes up her own inventory spaces.",
    "Yo' momma's so fat that it takes 10 nature runes to alch her.",
    "How hard is it to get a champion's scroll? I dunno, but its pretty imp-possible.",
    "why did the noob cross the road? Because he couldn't teleport",
    "Q: How do you know you have played enough Runescape? A: When someone dies (IRL) and you ask what they dropped",
    "How many drunken dwarf randoms does it take to change a lightbulb? 1 to hold the lightbulb and 10 to drink until the room spins.",
]

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