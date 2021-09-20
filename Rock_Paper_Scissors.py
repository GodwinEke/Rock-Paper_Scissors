# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 19:19:36 2021

@author: ERIC
"""

import random
import time

def R_P_S_Game ():
    print("Let's play rock, paper, scissors. You have three trials to beat me. \nLet's see how good you are mate.")
    time.sleep(3)
    print("These are the rules: 'r' for rock, 'p' for paper, 's' for scissors'. We play three times. \nThat's all. ")
    time.sleep(3)
    
    
    user_win=[]
    comp_win=[]
    select=('r','p','s')
    
    i=1
    while i<=3:
        
        #Rock, Paper, Scissors Chant!!!
        time.sleep(1)
        print('\nRock')
        time.sleep(1)
        
        print('Paper')
        time.sleep(1)
        
        print('Scissors...')
        time.sleep(1)
        
        #User's choice
        user_input=input("Enter your choice: ")
        choice=random.choice(select)
                
        #S>P, P>R, R>S
        if user_input=='s' and choice=='p' or user_input=='p' and choice=='r' or user_input=='r' and choice=='s':
            print("You win")
            user_win.append('W')
            i+=1
        elif user_input=='p' and choice=='p' or user_input=='r' and choice=='r' or user_input=='s' and choice =='s':
             print("No one won!!")    
        else:
            print("I win!")
            comp_win.append('W')
            i+=1
            
    #Overall Winner
    if len(user_win)>len(comp_win):
        print("COngratulations!! You won me.I won {} times out of three times". format(len(user_win)))
    else:
        print(" \nHa ha ha!! I win!! I won {} times out of three times". format(len(comp_win)))
       
            
R_P_S_Game()


