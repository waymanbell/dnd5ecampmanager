import discord
from random import randint
# tokenfile exists as a way of obfuscating the bot token from GitHub
from tokenfile import BOTTOKEN


async def checkForBotCommand(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('!goaway'):
        await client.close()
    if message.content.startswith('!roll '):
        try:
            await message.channel.send(commandToRollDice(message))
        except:
            await message.channel.send("That ain't right.")


def commandToRollDice(msg):
    #TODO handle negative modifiers
    #Initialize variables
    rollresults = [] #List to hold individual rolls
    attachedcomment = '' #Roller supplied reason for the roll request, if any
    rollmodifier = 0 #Value by which to modify total of all rolled dice
    messagecontent = msg.content[6:] #Strip leading '!roll ' from message content
    messagecontent = messagecontent.split('!', 1) #Separate comment from roll request
    messagecontent[0] = str(messagecontent[0]).strip()

    if len(messagecontent) == 2: #Check for comment, save if exists
        attachedcomment = str(messagecontent[1])

    if '-' not in str(messagecontent[0]): #Note the todo
        dicelist = str(messagecontent[0]).split('+') #Separate all requested dice and modifier
        for dice in dicelist:
            dice = str(dice).split('d') #Separate quantity of dice from size of die
            if len(dice) == 1: #If there was no 'd', then this is actually the rollmodifier
                rollmodifier = int(dice[0])
            else: #All other members of the dicelist must be dice
                if str(dice[0]) == '': #Account for assumed 1; ie: '!roll d6' means '!roll 1d6'
                    rollresults.append(randint(1, int(dice[1])))
                else:
                    for dicequantity in range(int(dice[0])):
                        rollresults.append(randint(1, int(dice[1])))

    totalrolled = rollmodifier
    for result in rollresults:
        totalrolled += int(result)

    return (msg.author.name + ' requested ' + str(messagecontent[0]) + ' to be rolled because: ' +
            str(attachedcomment) + '\nResults: ' + str(rollresults) + '\nTotal: {}'.format(totalrolled))


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        await checkForBotCommand(message)


# BOTTOKEN is located in tokenfile.py, excluded from GitHub for security reasons
client.run(BOTTOKEN)
