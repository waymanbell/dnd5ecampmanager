import discord
from random import randint
from tokenfile import BOTTOKEN

def formatForDiscordModded(msg, reqRoll, resultString, modifier):
    splitString = resultString.split(' ')
    newString = msg.author.name + " rolled " + reqRoll + " with a result of:\n["
    totalRoll = 0

    for roll in splitString:
        newString += str(roll) + ", "
        if roll != '':
            totalRoll += int(roll)
    totalRoll += int(modifier)
    completedString = newString[:-4]
    completedString += "]\nTotal: {}".format(totalRoll)

    return completedString

def formatForDiscordNoMod(msg, reqRoll, resultString):
    splitString = resultString.split(' ')
    newString = msg.author.name + " rolled " + reqRoll + " with a result of:\n["
    totalRoll = 0

    for roll in splitString:
        newString += str(roll) + ", "
        if roll != '':
            totalRoll += int(roll)
    completedString = newString[:-4]
    completedString += "]\nTotal: {}".format(totalRoll)

    return completedString


def rollDice(msg):
    contents = msg.content.split(' ')
    rollrequest = contents[1].split('d')
    modNum = 0
    dicequant = rollrequest[0]
    dicesize = rollrequest[1]
    modifier = ' '

    if '+' in rollrequest[1]:
        modifier = rollrequest[1].split('+')
        modNum = int(modifier[1])
        dicesize=modifier[0]
    if '-' in rollrequest[1]:
        modifier = rollrequest[1].split('-')
        modNum = -1 * int(modifier[1])
        dicesize=modifier[0]

    rollresults = ''

    x=1
    while x <= int(dicequant):
        rollednum = randint(1, int(dicesize))
        rollresults += '{} '.format(rollednum)
        x+=1

    if len(modifier) == 1:
        return formatForDiscordNoMod(msg, contents[1], rollresults)
    if len(modifier) == 2:
        return formatForDiscordModded(msg, contents[1], rollresults, modNum)

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
        await message.channel.send(rollDice(message))

    if message.content.startswith('!goaway'):
        client.close()

    if message.content.startswith('!showmewhatyougot'):
        await message.channel.send(message)
        await message.channel.send(message.content)
        await message.channel.send(message.author.name)

client.run(BOTTOKEN)
