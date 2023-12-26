# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 09:46:54 2023

@author: merri
"""

"""
Birthday Paradox, by Al Sweigart
"""

import datetime, random

def getBirthdays(numberOfBirthdays):
    MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    monthToChoose = random.randint(0, 11)
    
    ChooseDay = 
        
    

def getMatch(birthdays):
    
    
    
def main():
    print("Birthday Paradox, by Al Sweigart")
    print("""The Birthday Paradox show sus that in a group of N people, the odds 
          that two of them have matching birthdays is surprisingly large.  
          This program does a Monte Carlo simulation (that is, repeaded random
          simulations) to explore this concept. (It's not actually a paradox,
            it's just a surprising result)""")
    
    numberOfBirthdays = input("How many birthdays shall I generate? (Max 100)")
    
    listOfBirthdays = getBirthdays(numberOfBirthdays)

if __name__ == '__main__':
    main()