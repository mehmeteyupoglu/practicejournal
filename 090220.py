#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:41:16 2020

@author: Sena-2
"""

#def check(number):
#    
#    
#    if number == 1:
#        prime = False
#    
#    elif number == 2:
#        prime = True
#    
#    else:
#        prime = True
#        
#        for i in range(2, (number//2)+1):
#            if number % i == 0:
#                prime = False
#                break
#    return prime
#
#x = check(23)
#
#print(x)
#
#print('''
#      Let's play a game of Cowbull! 
#      Let's play a game of Cowbull! 
#      Let's play a game of Cowbull! 
#      Let's play a game of Cowbull! 
#      Let's play a game of Cowbull! 
#      '''
#      )

import random

def compare_numbers(number, user_guess):
    
    cowbull = [0, 0]
    
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[0] += 1
        else:
            cowbull[1] += 1
            
    return cowbull


if __name__ == '__main__':
    playing = True  