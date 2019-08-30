# dnd5ecampmanager

Baby steps!  I've managed to get the bot to connect to my Discord and respond to a limited number of commands.
There is virtually no input sterilization, and it falls over at a slight breeze, but it works so long as 
participants understand and adhere to its limitations.

Commands that work so far:

!hello - Responds with Hello

!showmewhatyougot - Displays the raw message data

!goaway - Disconnects the bot

!roll AdB - Rolls A-quanity of B-sided dice, displays the rolls and the total.

!roll AdB-C - As above, subtracts C-modifier from total

!roll AdB+C - As above, adds C-modifier to total

The code imports the bot's token from "tokenfile.py" which is not included in this repository.  The sole contents
of "tokenfile.py" is a declaration of BOTTOKEN which stores the bot's token.  I chose to do this so that I could
place the bot on github without necessarily sharing the token itself.