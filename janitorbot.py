import discord
import os
import re

client = discord.Client()

# tells you that the connection has been made and bot logged in

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# deletes message if the message has 'badword1, badword2, etc.' in it 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.lower() 
    badWords = ('badword1', 'badword2') # <-- list of bad words you can choose to include
    if any(badWords in msg for badWords in badWords):
        await message.delete()
        await message.channel.send('Your message was deleted for containing a banned word.')





client.run('DISCORD BOT TOKEN NUMBER GOES HERE')
