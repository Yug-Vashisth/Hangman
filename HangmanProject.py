
import time

import random
#below are the pictures that output when you get a letter wrong
HANGMAN_PICS =['''
     +---+
     O   |
    /|\  |
    / \  |
        ===''','''
     +---+
     O   |
    /|\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\  |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
         |
         |
       ===''', '''
     +---+
         |
         |
         |
        ===''']



name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

print (" ")

#amount of paused time
time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)
WORDS = ("python", "difficult", "answer",  "xylophone" , 'banana', 'Hello', 'lebronjames', 'ability' , 'about')
word = random.choice(WORDS)


guesses = ''

#you get 7 turns in this game
turns = 7



while turns > 0:         


    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char)    

        else:
    
        # if not found, print a dash
            print ("_"),
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("You won")  

    # exit the script
        break              

    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 5)
        turns -= 1        
 
    # print wrong
        print ("Wrong")
        print(HANGMAN_PICS[turns + 0])
 
    # how many turns are left
        print ("You have", + turns, 'more guesses') 
 
    # if the turns are equal to zero
        if turns == 0:

            print('You lose')
            print(word)
            
