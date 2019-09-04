import discord
from random import randint
# tokenfile exists as a way of obfuscating the bot token from GitHub
from tokenfile import BOTTOKEN


async def checkForBotCommand(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('!goaway'):
        await client.close()
    if message.content.startswith('!roll ') or message.content.startswith('/roll '):
        try:
            await message.channel.send(commandToRollDice(message))
        except:
            await message.channel.send("That ain't right.")


def commandToRollDice(msg):
    # Initialize variables
    rollresults = ''  # String to hold individual rolls
    attachedcomment = ''  # Roller supplied reason for the roll request, if any
    rollmodifier = 0  # Value by which to modify total of all rolled dice
    totalrolled = 0  # Variable to store the grand total of all rolled dice and modifier
    messagecontent = msg.content[6:]  # Strip leading '!roll ' from message content
    messagecontent = messagecontent.split('!', 1)  # Separate comment from roll request
    messagecontent[0] = str(messagecontent[0]).strip()

    if len(messagecontent) == 2:  # Check for comment, save if exists
        attachedcomment = str(messagecontent[1])

    dicelist = str(messagecontent[0]).split('+')  # Separate all requested dice and modifier
    for dice in dicelist:
        dicerolls = []
        if '-' in str(dice):  # Watch for and catch a negative rollmodifier
            dice = str(dice).split('-')
            rollmodifier += int(dice[1]) * -1
            dice = str(dice[0])
        dice = str(dice).split('d')  # Separate quantity of dice from size of die
        if len(dice) == 1:  # If there was no 'd', then this is actually the rollmodifier
            rollmodifier += int(dice[0])
        else:  # All other members of the dicelist must be dice
            if str(dice[0]) == '':  # Account for assumed 1; ie: '!roll d6' means '!roll 1d6'
                dice[0] = 1
            for dicequantity in range(int(dice[0])):
                roll = randint(1, int(dice[1]))
                dicerolls.append(roll)
                totalrolled += roll
        if len(dicerolls) > 0:
            if rollresults == '':
                rollresults += str(dicerolls)
            else:
                rollresults += ' + ' + str(dicerolls)

    # Apply rollmodifier
    totalrolled += rollmodifier

    # Adjust rollresults string based on sign of rollmodifier.  This is just to help make the return string pretty.
    if rollmodifier > 0:
        rollresults += ' + '
    if rollmodifier < 0:
        rollresults += ' - '

    # Format return message appropriate to the context of the message
    if rollmodifier != 0:
        if attachedcomment != '':  # There exists a modifier and a roll comment
            return (msg.author.name + ' rolls ' + str(messagecontent[0]) + ' because: ' +
                    str(attachedcomment) + '\nResults: ' + rollresults + str(abs(rollmodifier)) +
                    ' = {}'.format(totalrolled))
        else:  # There exists a modifier, but no roll comment
            return (msg.author.name + ' rolls ' + str(messagecontent[0]) + ':' +
                    '\nResults: ' + rollresults + str(abs(rollmodifier)) + ' = {}'.format(totalrolled))
    else:
        if attachedcomment != '':  # There is no modifier, there is a roll comment
            return (msg.author.name + ' rolls ' + str(messagecontent[0]) + ' because: ' +
                    str(attachedcomment) + '\nResults: ' + rollresults + ' = {}'.format(totalrolled))
        else:  # There is neither a modifier nor a roll comment
            return (msg.author.name + ' rolls ' + str(messagecontent[0]) + ':' +
                    '\nResults: ' + rollresults + ' = {}'.format(totalrolled))


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
