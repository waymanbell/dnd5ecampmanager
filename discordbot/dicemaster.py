import discord
from random import randint
#tokenfile exists as a way of obfuscating the bot token from GitHub
from tokenfile import BOTTOKEN


#Okay, the two functions below can easily be sorted out with a kwargs, I'm sure.
#I'm just not familiar enough with it, yet. So I've implemented the functions to
#work for now with an eye toward refactoring later.

def formatForDiscordModded(msg, reqRoll, resultString, modifier):
    #Separate the dice rolls
    splitString = resultString.split(' ')
    newString = msg.author.name + " rolled " + reqRoll + " with a result of:\n["
    totalRoll = 0

    #Format rolls output
    for roll in splitString:
        newString += str(roll) + ", "
        if roll != '':
            totalRoll += int(roll)

    totalRoll += int(modifier)
    completedString = newString[:-4] #Remove tailing ", , "
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
    #Separate "!roll" from the target "XdX+/-X"
    contents = msg.content.split(' ')

    #Further separate dice quantity from sides of die
    rollrequest = contents[1].split('d')

    modNum = 0
    dicequant = rollrequest[0]
    dicesize = rollrequest[1] #Initialized here for the case of having no +/- modifier
    modifier = ' ' #Initialized here as such to promote correct behavior in the event of no modifier

    #If the modifier is a positive
    if '+' in rollrequest[1]:
        modifier = rollrequest[1].split('+')
        modNum = int(modifier[1])
        dicesize=modifier[0]

    #If the modifier is a negative
    if '-' in rollrequest[1]:
        modifier = rollrequest[1].split('-')
        modNum = -1 * int(modifier[1])
        dicesize=modifier[0]

    rollresults = ''

    #I know there is a better way to iterate, but I'm not familiar with it, yet.
    #Generate the requested number of random ints within the requested range
    x=1
    while x <= int(dicequant):
        rollednum = randint(1, int(dicesize))
        rollresults += '{} '.format(rollednum)
        x+=1

    #If there is NO modifier
    if len(modifier) == 1:
        return formatForDiscordNoMod(msg, contents[1], rollresults)
    #If there exists a modifier
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

#BOTTOKEN is located in tokenfile.py, excluded from GitHub for security reasons
client.run(BOTTOKEN)
