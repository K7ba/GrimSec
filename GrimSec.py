import socket
import discord
import requests
import urllib
import os
import asyncio
import json

from asyncio import sleep
from socket import socket
from discord.ext import commands

current_file_path = os.path.dirname(os.path.abspath(__file__))

with open('config.json') as f:
    config = json.load(f)
    prefix = config.get('Prefix')
    token = config.get('Token')
    status = config.get('Status')
    staff = config.get('Staff-Role')

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

blacklist = [
    "Emails To Be Blacklisted Here",
    "example@example.com"
]


@bot.event
async def on_ready():
    activity = discord.Game(name="Netflix", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")

@bot.command()
async def plshelp(ctx):
    plshelp = discord.Embed(title="Help", color=0xe61010)
    plshelp.add_field(
        name=".lookup",
        value=
        "▸ Search Databases For The Target Email Address",
        inline=False)
    plshelp.add_field(
        name=".ulookup",
        value=
        "▸ Search Databases For The Target Username",
        inline=False)
    plshelp.add_field(
        name=".nlookup",
        value=
        "▸ Search Databases For The Target Phone Number",
        inline=False)
    await ctx.send(embed=plshelp) 

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='.plshelp'))
    
@commands.has_role("Access")
@bot.command(pass_context=True)
async def lookup(ctx, email):
    request = urllib. request. urlopen('https://example.com/api?key=API KEY HERE&check=' + email + '&type=email')
    data = json. load(request)
    with open("result.txt", "w") as file:
      file.write(f"{data}")
    with open("result.txt", "rb") as file:
      await ctx.send(file = discord.File(file, "result.txt"))
    await ctx.send(embed=embed)
    
@commands.has_role("Access")
@bot.command(pass_context=True)
async def ulookup(ctx, username):
    request = urllib. request. urlopen('https://example.com/api?key=API KEY HERE&check=' + username + '&type=username')
    data = json. load(request)
    with open("result.txt", "w") as file:
      file.write(f"{data}")
    with open("result.txt", "rb") as file:
      await ctx.send(file = discord.File(file, "root/result.txt"))
    await ctx.send(embed=embed)
    
@commands.has_role("Access")
@bot.command(pass_context=True)
async def nlookup(ctx, phone):
    request = urllib. request. urlopen('https://example.com/api?key=API KEY HERE&check=' + phone + '&type=phone')
    data = json. load(request)
    with open("result.txt", "w") as file:
      file.write(f"{data}")
    with open("result.txt", "rb") as file:
      await ctx.send(file = discord.File(file, "root/result.txt"))
    await ctx.send(embed=embed)   

bot.run('Discord Bot Token Here')
