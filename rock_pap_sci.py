# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 23:51:34 2023

@author: 91913
"""

import random

running=True

while running==True:
    options = ("rock","paper","scissor")
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("enter choice")

    print(f"player:{player}")
    print(f"computer:{computer}")

    if player==computer:
        print("it is a tie")
        
    if player=="scissor" and computer=="paper":
        print("you win")
    elif player=="paper" and computer=="rock":
        print("you win")
    elif player=="rock" and computer=="scissor":
        print("you win")
    else:
        print("you lose")
        
    playAgain=input("play again(y/n)")
    if playAgain=="y":
        running=True
    else:
        running=False
    


