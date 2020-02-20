#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 12:30:31 2020

@author: Sena-2
"""

#x,y = 0, 1
#x,y = y, x
#print(x,y)

#a = 'Geek for Geeks is a good learning portal'
#
#print('Reverse of \'a\' is', a[::-1])

#a = ['Geek', 'for', 'Geeks']
#
#print(''.join(a))

#b = ['Learn', 'Python', 'everyday', 'until', 'you', 'learn', 'it']
#print('      '.join(b))

#c = ['Python', 'is', 'a', 'good', 'language']
#print(' '.join(c))

#n = 10
#result = 1 < n < 20
#print(result)
#
#result2 = 1>n<20
#print(result2)

#def x():
#    return 1,2,3,4
#
#a,b,c,d = x()
#
#print(a,b,c,d)

#name = str(input('Please enter your name: '))
#age = int(input('Please enter your age: '))
#bday = 2019-age
#
#print(name,',you will turn 100 in', bday+100)

#num = int(input('Enter a number:   '))
#check = int(input('Enter a number to check:  '))
#
#if num % 4 == 0 or num % 2 == 0:
#    print(num, 'is divided evenly by 4 and it is an even number.')
#else:
#    print(num, 'is an odd number')
#
#if num % check == 0:
#    print(num, 'is divided evenly by', check)
#else:
#    print(num, 'is not divided evenly by', check) 

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = []
#c = []
#for i in a:
#    if i < 5:
#        b.append(i)
#print(b)
#
#num = int(input('Please enter a number:   '))
#
#for x in a:
#    if x < num and x is not in c:
#        c.append(x)
#print(c)

#num = int(input('Give me a number:   '))
#div = []
#
#for i in range (1,num+1):
#    if num % i == 0:
#        div.append(i)
#
#print(div)

#a = [11, 23, 67, 45, 34, 78, 9, 3, 345, 123, 456,789, 234, 78]
b = [11, 23, 45, 67, 89, 90, 23, 45, 34, 56, 78,]
#c = []
#
#for i in b:
#    if i in a and i not in c:
#        c.append(i)
#
#print(c)

#wrd = str(input('Please enter a name:   '))
#rvs = wrd[::-1]
#
#if wrd == rvs:
#    print(wrd, 'is palyndrome.')
#else:
#    print(wrd, rvs, 'is not a palyndrome.')

#import random
#
#num = random.randint(1,20)
#guess = 0
#count = 0
#
#while guess != num or guess != 'exit':
#    guess = (input('Please enter a number between 1 and 20:  '))
#    
#    if guess == 'exit':
#        break 
#    
#    guess = int(guess) 
#    count += 1 
#    
#    if guess < num:
#        print('You are too low')
#    elif guess > num:
#        print('You are too high')
#    elif guess == num:
#        print('You got it')
#        print('It took only', count, 'times')

#def list_ends(a_list):
#    return [a_list[0], a_list[-1]]
#
#
#
#print(list_ends(b))

#def mul(*args):
#    z = 1
#    for i in args:
#        z *= i
#    print(z)
#    
#
#print(mul(1,2,4,5,6))
#
#def mul(*args):
#    z = 1
#    for i in args:
#        z *= i
#    print(z)
#    
#mul(3,4,5)
#
##def key_values(**kwargs):
##    for key, value in kwargs.items():
##        print('The value of {} is {}'.format(key, value))
##
##
##key_values(key = 'Mehmet', value = 'Sena')
#
#def some_args(arg_1, arg_2, arg_3):
#    print('arg_1:', arg_1)
#    print('arg_2:', arg_2)
#    print('arg_3:', arg_3)
#
#my_list = [2,3]
#
#some_args(1, *my_list)

#def ismin_ne():
#    isim = input('Enter your name')
#    print(isim)
#    
#liste = [i for i in range(1, 100, 3)]
#print(liste)

#liste2 = [i for i in range(100) if i % 2 != 0]
#
#print(liste2)
#liste3 = [[1, 2, 3],
#[4, 5, 6],
#[7, 8, 9],
#[10, 11, 12]]
#
#liste4 = [z for i in liste3 for z in i]

#kardiz = "istihza"
#
#for i in kardiz:
#    print(i, end = '\n\t')
    
    
#import os
#import sys
#
#os.sys
#print(sys.version)
#
#print(os.name)

age = 0

while age != 'exit':
    age = input('Please enter your age. Type exit to quit\n:>   ')
    bday = 2019-age
    if age == 'exit':
        break
    age ==(int)
    else:
        print('You will return 100 in', bday+100)
    



    
    
    
        

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    