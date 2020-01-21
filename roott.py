import discord
import asyncio
from parserr import parsing

client = discord.Client()
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
@client.event
async def on_message(message):
    msg = message.content.split(" ")
    if message.content.startswith('!test'):
        await message.channel.send('test!!!!')
 
    elif msg[0] == "#boj":
        try:
            await message.channel.send("https://www.acmicpc.net/problem/" + str(msg[1]))
            await message.channel.send(parsing(msg[1]))
        except:
            await message.channel.send("Error!!!")
            
 
client.run('NjY4NzM5NTMwODY1NTA4MzYy.XiZePw.tLM1a_6QnKRgH3z2D2ePqYw-Tq8')
