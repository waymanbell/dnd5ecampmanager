# dnd5ecampmanager

Baby steps!  I've managed to get the bot to connect to my Discord and respond to a limited number of commands.
There is minimal input sterilization, but it does not fall over easily!

Commands that work so far:

!hello - Responds with Hello

!goaway - Disconnects the bot

!roll AdB - Rolls A-quantity of B-sided dice, displays the rolls and the total.

!roll AdB+C - As above, adds C-modifier to total

!roll AdB-C - As above, subtracts C-modifier from total

!roll AdB+CdE+...+Z - Rolls multiple types of die and adds the Z-modifier to the total.

!roll AdB+CdE+...-Z - Rolls multiple types of die and subtracts the Z-modifier from the total. 

The code imports the bot's token from "tokenfile.py" which is not included in this repository.  The sole contents
of "tokenfile.py" is a declaration of BOTTOKEN which stores the bot's token.  I chose to do this so that I could
place the bot on github without necessarily sharing the token itself.
