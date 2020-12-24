import discord
from discord.ext import commands
from asyncio import sleep
client = commands.Bot(command_prefix='-', help_command=None)


async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='𝙇𝙄𝙏𝙀-𝙢𝙚𝙢𝙗𝙚𝙧𝙨'))
        await sleep(1)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='LITE-members'))
        await sleep(1)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='𝙇𝙄𝙏𝙀-𝙢𝙚𝙢𝙗𝙚𝙧𝙨'))
        await sleep(1)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='LITE-members'))
        await sleep(1)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='𝙇𝙄𝙏𝙀-𝙢𝙚𝙢𝙗𝙚𝙧𝙨'))
        await sleep(1)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='LITE-members'))
        await sleep(1)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='𝙇𝙄𝙏𝙀-𝙢𝙚𝙢𝙗𝙚𝙧𝙨'))
        await sleep(1)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='LITE-members'))
        await sleep(1)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='𝙇𝙄𝙏𝙀-𝙢𝙚𝙢𝙗𝙚𝙧𝙨'))
        await sleep(1)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='LITE-members'))
        await sleep(1)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='𝙇𝙄𝙏𝙀-𝙢𝙚𝙢𝙗𝙚𝙧𝙨'))
        await sleep(1)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='LITE-members'))
        await sleep(1)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='𝙇𝙄𝙏𝙀-𝙢𝙚𝙢𝙗𝙚𝙧𝙨'))
        await sleep(1)
@client.event
async def on_ready():
    print(f'{client.user} has Awoken!')
    await client.loop.create_task(status())


import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)
client.run('NzkxNTQ1MjAxOTYwOTQzNjg2.X-Qt6g.-BcbDNMgWptoSMgwLa0yqRJdKTY')
bot.run('NzkxNTQ1MjAxOTYwOTQzNjg2.X-Qt6g.-BcbDNMgWptoSMgwLa0yqRJdKTY')
