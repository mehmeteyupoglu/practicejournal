#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:39:28 2020

@author: Sena-2
"""
#
#string = 'Mehmet'
#
#print(len(string))

#def string_num(string):
#    count = 0
#    for i in string:
#        count += 1
#    return i
#
#import calendar
#
#m = int(input('Hangi ay olsun?'))
#y = int(input('Hangi yıl olsun?'))
#
#print(calendar.month(y, m))

#import calendar
#y = int(input("Input the year : "))
#m = int(input("Input the month : "))
#print(calendar.month(y, m))
#
#import datetime
#
#now = datetime.datetime.now()
#
#print('Current date and time:  ')
#print(now.strftime('%Y/%m/%d %H:%M:%S'))
#
#import calendar
#
#y = int(input('Input the year: '))
#m = int(input('Input the month: '))
#
#print(calendar.month(y,m))

#name = input('Give me a name:  ')
#name = str(name)
#nums = input('Enter numbers, separated by a comma: ')
#liste1 = nums.split(',')
#tuple1 = tuple(nums)
#
#print('List: {}'.format(liste1))
#print('Tuple: {}'.format(tuple1))

#a = int(input('Enter a num: '))
#
#n1 = int('%s' % a )
#n2 = int('%s%s' % (a,a) )
#n3 = int('%s%s%s' % (a,a,a) )
#
#print(n1+n2+n3)

#print(print.__doc__)
#
#import datetime
#
#date1 = datetime.date(2017, 7, 2)
#date2 = datetime.date(2017, 7, 11)
#delta = date2 - date1
#
#print('There are {} days between the two dates.'.format(delta.days))

#import sys
#
#print(sys.version)

#import calendar
#
#y = int(input('Enter the year: '))
#m = int(input('Enter the month: '))
#
#print(calendar.month(y,m))

#import datetime
#
#now = datetime.datetime.now()
#
#print(now.strftime('%Y-%m-%d %H:%M:%S'))

#def sum_three(a,b,c):
#    if a == b == c:
#        return (a+b+c)*2
#    else:
#        return (a+b+c)
#print(sum_three(55,55,55))

#num = int(input('Enter a number: '))
#fib = []
#a = 0
#b = 1
#for i in range(1,num+1):
#    a, b = b, a+b
#    fib.append(a)
#print(fib)

#numbers = [    
#    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#    958,743, 527
#    ]
#
#list_of_even = []
#i = 0
#
#while i < 237:
#    for i in numbers:
#        
#        if i % 2 == 0:
#            list_of_even.append(i)
#
#print(list_of_even)

a_list = [3,55,23,4,56,4]
#
#def finder(a_list):
#    count = 0
#    for i in a_list:
#        if i == 4:
#            count = count + 1
#    return count
#
#print(finder(a_list))

#def contanate(a_list):
#    result = ''
#    for i in a_list:
#        result += str(i)
#    return result.split(',')
#print(contanate(a_list))

#color_list_1 = set(["White", "Black", "Red"])
#color_list_2 = set(["Red", "Green"])
#
#print(color_list_1.difference(color_list_2))

#ui = int(input('Give me an integer:  '))
#ui2 = int(input('Give me another integer: '))
#
#if ui

#'''
#Question 3
#Ask the user for a number between 1 and 12 and then display a times
#table for that number.
#'''
#num = int(input('Enter an integer: '))
#print('WELCOME TO {} TIMES TABLE'.format(num))
#for i in range(0, 12):
#    print(f'{i} x {num} = {i*num}')

#'''
#Question 4
#Can you amend the solution to question 3 so that it just prints out all
#times tables between 1 and 12? (no  need to ask user for input)
#'''
#
#for i in range(1, 13):
#    print('---'*10)
#    print('WELCOME TO {} TIMES TABLE'.format(i))
#    print('---'*10)
#    for x in range(1,13):
#        print(f'{i} x {x} is {i*x}')
#    print('#'*10)
#    print('{} times table finished'.format(i))
#    print()
#    


#'''
#Question 5
#Ask the user to input a sequence of numbers. Then calculate the mean
#and print the result
#'''
#
#user_input = input('Enter a number: ')
#numbers = []
#
#while user_input.lower() != 'exit':
#    while not user_input.isdigit():
#        print('This is not an integer. Please enter one: ')
#        user_input = input('Please enter a number: ')
#    numbers.append(int(user_input))
#    user_input = input('Enter the next number: ')
#
#total = 0
#
#for i in numbers :
#    total += i
#
#print(f'The mean of {numbers} is {total//len(numbers)}')
#n = 15
#fact = 1
#for i in range(1,n+1):
#    fact = fact * i 
#
#print(fact)
    
'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''

#fib_nums = []
#a = 0
#b = 1
#for i in range(1,21):
#    a,b = b, a+b
#    fib_nums.append(a)
#
#print(fib_nums)    

#def fib_gen():
#    user_input = int(input('Enter a number:'))
#    i = 1
#    
#    if user_input == 0:
#        fib_num = []
#    
#    elif user_input == 1:
#        fib_num = [1]
#    
#    elif user_input == 2:
#        fib_num = [1,1]
#    
#    elif user_input > 2:
#        fib_num = [1,1]
#        while i < (user_input-1):
#            fib_num.append(fib_num[i]+fib_num[i-1])
#            i += 1
#    return fib_num
#
#
#    
#def gen_fib():
#    count = int(input("How many fibonacci numbers would you like to generate? "))
#    i = 1
#    if count == 0:
#        fib = []
#    elif count == 1:
#        fib = [1]
#    elif count == 2:
#        fib = [1,1]
#    elif count > 2:
#        fib = [1,1]
#        while i < (count - 1):
#            fib.append(fib[i] + fib[i-1])
#            i += 1
#
#    return fib
#
#gen_fib()

#star = '*'
#
#for i in range(1,7):
#    for j in range(1,6):
#        if i == 1 and j < 6:
#            print(star, end = '')
#        elif i == 2 and j == 1:
#            print()
#            print(star)
#        elif i == 3 and j < 5:
#            print(star, end = '')
#        elif i == 4 and j == 1:
#            print()
#            print(star)
#        elif i == 5 and j == 1:
#            print(star)
#        elif i == 6 and j == 1:
#            print(star)

#star = '*'
#
#for i in range(1,7):
#    for j in range(1,6):
#        if i == 1 and j < 6:
#            print(star,end='')
#        elif i == 2 and j == 1:
#            print()
#            print(star)
#        elif i == 3 and j < 5:
#            print(star,end='')
#        elif i == 4 and j == 1:
#            print()
#            print(star)  
#        elif i == 5 and j == 1:
#            print(star)
#        elif i == 6 and j == 1:
#            print(star)  

#'''
#Question 1
#Can you remember how to check if a key exists in a dictionary?
#Using the capitals dictionary below write some code to ask the user to input
#a country, then check to see if that country is in the dictionary and if it is
#print the capital. If not tell the user it's not there.
#'''
#
#capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
#            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
#            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
#            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
#            }
#
#user_input = input('Enter the country you would like to check: ')

'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''
#d = {}
#a = 0
#b = 1
#
#for i in range(1,12):
#    a, b = b, a+b
#    d[i] = a
#print(d)

'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''
#price_type = ['open', 'high', 'low', 'close']
#companies = ['Python DS', 'PythonSoft', 'Pythazon','Pybook']
#data = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
#[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]
#
#d_1 = {}
#
#for i in range(len(companies)):
#    d_1[companies[i]] = dict(zip(price_type,data[i]))
#print(d_1)
    

#companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
#key_names = ['Open','High','Low','Close']
#prices = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
#[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]
#
#d_1 = {}
#
#for i in range(len(key_names)):
#    d_1[companies[i]] = dict(zip(key_names,prices[i]))
#        
#print(d_1) 

#'''
#Question 4
#Go to the python module web page and find a module that you like. Play with it, 
#read the documentation and try to implement it.
#'''
#import datetime
#
#today = datetime.date.today()
#holiday = datetime.date(2020, 4, 22)
#delta = holiday - today
#
#print('There are {} days until the holiday.'.format(delta.days))

#'''
#Question 5
#Create a dictoinary containing as keys the letters from A-Z, the values should
#be random numbers created from the random module. Can you draw a bar graph of
#the results?
#'''
#import random
#
#keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#d = {}
#for i in keys:
#    d[i] = random.randint(1, 100)
#
#import matplotlib.pyplot as plt
#
#x, y = zip(*d.items())
#
#print(plt.bar(x,y))

#'''
#Question 6
#Create a dictionary containing 4 suits of 13 cards 
#['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
#'''
#
#suits = ['Spades','Clubs','Hearts','Diamonds']
#rank = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
#
#d = {}
#for i in suits:
#    d[i] = rank
#
#print(d)

import sys

heading = 'WELCOME TO ROCK, SCISSORS, GAME'

print('-'*len(heading))
print(heading)
print('-'*len(heading))

player1 = input('Enter your name: ')
player2 = input('Enter your name: ')

user_input1 = input('{}, choose one: rock, paper, scissors. '.format(player1))
user_input2 = input('{}, choose one: rock, paper, scissors. '.format(player2))

def compare(user_input1, user_input2):
    if user_input1 == user_input2:
        return ('It is a tie')
    
    elif user_input1 == 'rock':
        if user_input2 == 'scissors':
            return ('rock wins!')
        else:
            return ('paper win')
    
    elif user_input1 == 'paper':
        if user_input2 == 'scissors':
            return ('scissors win!')
        else:
            return ('paper wins')
        
    elif user_input1 == 'scissors':
        if user_input2 == 'paper':
            return ('scissors win!')
        else:
            return ('paper wins')
            
    else:
        return ('Do you want to play it again? ')
        sys.exit()

print(compare(user_input1, user_input2)

import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer``




    
















