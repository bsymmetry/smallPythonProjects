# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 06:25:54 2023

@author: merri
"""

import random

def intro():
    print("Bagels, a deductive logic game.")
    print("By Al Sweigart")
    print("")
    print("I am thinking of a 3-digit number.  Try to guess what it is.")
    print("Here are some clues:")
    print("When I say:   That means:")
    print("  Pico         One digit is correct but in the wrong position")
    print("  Fermi        One digit is correct and in the right position")
    print("  Bagels       No digit is correct")
    print("I have thought up a number.")
    print("You have 10 guesses to get it.")

def number_to_guess():
    
    digits = []
    
    num = str(random.randint(100, 999))
    
    for x in num:
        digits.append(x)
        
    
    return digits

def game_flow(digits):
    
    guess_counter = 1
    
    while guess_counter <= 10:
        guess = input("Guess #" + str(guess_counter) + ": ")
        
        for char in guess:
            
            if str(char) not in digits:
                print("Bagel")
            elif str(char) in digits and str(guess[0]) != digits[0] and str(guess[1]) != digits[1] and str(guess[2]) != digits[2]:
                print("Pico")
            elif str(char) in digits and str(guess[0]) == digits[0] or str(guess[1]) == digits[1] or str(guess[2]) == digits[2]:
                print("Fermi")
        
        guess_counter += 1
            

def main():
    
    play_again = True
    
    while (play_again == True):
        
        intro()
        
        num_to_guess = number_to_guess()
        
        game_flow(num_to_guess)
        
        another_game = input("Do you want to play again? (y or n)")
        
        if another_game == "n":
            play_again = False
        

if __name__ == '__main__':
    main()