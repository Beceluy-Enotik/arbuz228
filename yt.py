import discord
from discord.ext import commands
from discord.ext.commands import Bot, guild_only
import random
import string
import os
import time

    #info
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
token = "MTA2OTE4ODU0MTgxMDIyMTA5Nw.Gb_sDa.Tqs1uo5maGC6SABvvSVtThEI9VPWza14RG8DxY"


    #ready
@bot.event
async def on_ready():
    print("Started")
        
@bot.command()
async def start(ctx):
    await ctx.send('Укажите число генераций в консоле!')
    a = int(input("Укажите число генераций: "))
    os.system("cls")
    await ctx.send('Данные успешно получены')
    i = 0
    while i < a:
        i += 1
        letters_and_digits = string.ascii_letters + string.digits
        rand_string = ''.join(random.sample(letters_and_digits, 16))

        print(f"[{i}] - https://discord.com/gifts/{rand_string}")
        time.sleep(0.01);
        await ctx.send(f"[{i}] - https://discord.com/gifts/{rand_string}")

bot.run(token)