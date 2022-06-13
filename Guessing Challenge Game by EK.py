#Guessing Game Challenge By EK

#RULES

#Let's use while loops to create a guessing game.

#The Challenge:

#Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

#If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
#On a player's first turn, if their guess is
#within 10 of the number, return "WARM!"
#further than 10 away from the number, return "COLD!"
#On all subsequent turns, if a guess is
#closer to the number than the previous guess return "WARMER!"
#farther from the number than the previous guess, return "COLDER!"
#When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
#You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!

#break: Breaks out of the current closest enclosing loop.
#continue: Goes to the top of the closest enclosing loop.
#pass: Does nothing at all.


#CODE

from random import randint
hidden_number=randint(1,100)
#print(hidden_number)

guesses=[]
print("\nWelcome to the Guessing Game Challenge by Erik Kiladis")
user_name=input("\nPlease write your name and press the 'enter' button:  ")

decision="restart"

while decision.lower()=="restart":
   
    print(f"\ngood luck {user_name}, hope you enjoy")

    first_guess=int(input(f"\nOK, let's start playing {user_name}!! :) Now please make your FIRST GUESS:  "))

    while first_guess<1 or first_guess>100:
        first_guess=int(input(f"\nOOPS...OUT OF BOUNDS... Consentrate {user_name}.. \nGive me a number between 1 and 100:  "))
    else:    

        if first_guess==hidden_number:
            print(f"\nPERFECT GUESS {user_name}\n THE END")
        else:
            if abs(first_guess-hidden_number)<=10:
                print("\nWARM")
                pass
            else: 
                print("\nCOLD")
                pass
            
            guesses.append(first_guess)
            guesses.append(input("\nGuess a number:  "))
            guesses[-1]=int(guesses[-1])

            while guesses[-1]!=hidden_number:
                if guesses[-1]>100 or guesses[-1]<1 :
                    guesses[-1]=int(input("\nGuess an number between 1 and 100:  "))
                    continue

                elif abs(guesses[-1]-hidden_number)>=abs(guesses[-2]-hidden_number):
                    print("\nCOLDER")
                    guesses.append(input("\nGuess a number:  "))
                    guesses[-1]=int(guesses[-1])

                else :
                    print("\nWARMER")
                    guesses.append(input("Guess a number:  "))
                    guesses[-1]=int(guesses[-1])
            else:

                print(f"\nCONGRATS {user_name}! You guessed the hidden number after {len(guesses)} valid attemps")

                decision=input("If you want to play again, press 'restart', if you want to close the game press any button ")


           