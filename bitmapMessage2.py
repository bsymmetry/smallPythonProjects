# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:35:21 2023

@author: merri
"""

bitmap = """
........................................
                  ***                   
                *******
              *****  ****
              ****    ***
               ****  ***
                *******
                  ***
........................................"""


print("Enter the message to display with the bitmap.")
message = input()

print()

counter = 0
    
while message == '':
    print("Need to enter something!")
    message = input()


for line in bitmap.splitlines():
    
    for char in line:
        
        if counter == len(message):
            counter = 0
        
        if char == ' ':
            print(' ', end='')
            counter += 1
        else:
            print(message[counter], end='')
            counter += 1
    
    print()
    
            