import discord
from random import randint
from tokenfile import TOKEN

def rollDice(msg):
    contents = msg.content.split(' ')
    rollrequest = contents[1].split('d')
    dicequant = rollrequest[0]
    dicesize = rollrequest[1]
    rollresults = ''
    x=1
    while x <= int(dicequant):
        rollednum = randint(1, int(dicesize))
        rollresults += '{} '.format(rollednum)
        x+=1
    return rollresults

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!roll'):
        await message.channel.send(message.author.name + " rolled " + rollDice(message))

    if message.content.startswith('!showmewhatyougot'):
        await message.channel.send(message)
        await message.channel.send(message.content)
        await message.channel.send(message.author.name)

client.run(TOKEN)
