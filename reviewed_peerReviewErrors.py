# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''                                   #Eckert: You must use either tabs or spaces, not mix both.
    while cave != '1' and cave != '2':          #Eckert: Nice use of a while loop to ensure user enters 1 or 2.
		print('Which cave will you go into? (1 or 2)') #Eckert: If you want you can put the string in the input brackets to save some time
		cave = input()

	return caves      #Eckert: This will error out because "caves" is not a variable. Should be "cave".

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')  
	#sleep for 2 seconds           
	time.sleep(3)          #Eckert: You must've meant to put '2' in the time.sleep() call.
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):    #Eckert: Design issue, not code issue - It's up to chance. If the user decided to play again and choose the OTHER cave, there's a chance they will still get eaten. 
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!'

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y':
	displayIntro()
	caveNumber = choosecave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing")   #Eckert: Just a spelling error. "Playing" is what should be here. 

