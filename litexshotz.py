import discord
from discord.ext import commands
import asyncio
import random
import os
import praw
import json


client = commands.Bot(command_prefix = '.') 

@client.event
async def on_ready():
     #Setting `playing ` status
     await client.change_presence(activity=discord.Game(name=f"on {len(client.guilds)} servers | Developer HenG"))
     #Setting `Streaming ` status
     await client.change_presence(activity=discord.Streaming(name="xvideo.com", url=https://www.xvideos.com/))
     #Setting `Listening ` status
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.Listening, name="LITE manager"))
     #Setting `Watching ` status
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Hengz developer><"))

     print("Ready")


     async def ch_pr():
     	   await client.wait_until_ready()

     	   statuses = ["a game", f"on {len(client.guilds)} servers | e!help", "discord.py"]

     	   while not client.is_closed():

     	   	status = random.choice(statuses)

     	   	await client.change_presence(activity=discord.Game(name=status))

     	   	await asyncio.sleep(10)

    client.loop.create_task(ch_pr())
    client.run()