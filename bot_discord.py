import discord
import asyncio

#Your bot's token
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()

#Event that will occur
@client.event
async def on_message(message):
    if message.content.find("Pergunta") != -1:
        await message.channel.send("Resposta")
     
client.run(token)
