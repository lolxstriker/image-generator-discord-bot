import requests
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents)



@bot.event
async def on_ready():
    print("Bot is online!")
    await bot.change_presence(activity=discord.Game(name="Images")) #change it to any name activity

@bot.command()
async def dog(ctx):
    r = requests.get("https://dog.ceo/api/breeds/image/random")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['message'])
    await ctx.send(embed=em)

@bot.command()
async def fox(ctx):
    r = requests.get("https://randomfox.ca/floof")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['image'])
    await ctx.send(embed=em)

@bot.command()
async def yesorno(ctx):
    r = requests.get("https://api.truthordarebot.xyz/v1/truth")
    res = r.json()
    await ctx.send(res['question'])

bot.run("UR BOT TOKEN")