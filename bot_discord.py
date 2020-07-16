import discord
#required to the library asyncio
import asyncio

#Your bot's token
#create a .txt file with your bot's token, and place it together where the .py file is
#the token is purchased from the Discord developer portal
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()

#Event that will occur when the user writes in the chat
@client.event
async def on_message(message):
    if message.content.find("Question") != -1:
        #bot response
        await message.channel.send("Answer")
     
client.run(token)
