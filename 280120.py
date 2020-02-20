#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:00:35 2020

@author: Sena-2
"""

#def max_two(a, b):
#    
#    if a > b:
#        return a
#    return b
#
#def max_three(x, y, z):
#    
#    return max_two(x, max_two(y,z))

#print(max_two(45, 34))
#print(max_three(5, 67, 34))

#def sum_list(a):
#    
#    count = 0
#    
#    for i in a:
#        count += i 
#    return count
#
#a = [4,9,23,0,6]
#
#print(sum_list(a))

#list1 = [8, 2, 3, -1, 7]
#
#def mult(a_list):
#    count = 1
#    
#    for i in list1:
#        count *= i 
#    return count
#
#print(mult(a))

#String_1 = "1234abcd"
#
#def rvs(string):
#    
#    rvs1 = ''
#    index = len(string)
#    
#    while index > 0:
#        rvs1 = rvs1 + string[index - 1]
#        index = index - 1
#    return rvs1
#
#print(rvs(String_1))

#string1 = '1234abcd'
#
#def rvs(string):
#    
#    rvs = ''
#    index = len(string)
#    
#    while index > 0:
#        rvs += string[index - 1]
#        index = index - 1
#    return rvs
#
#print(rvs(string1))

#def fact(num):
#    
#    if num == 0:
#        return 1
#    else:
#        return (num * factorial(num-1))
#
#print(fact(9))

#def test_range(num):
#    
#    if num in range(1,10):
#        print('The number ({})you entered is within the range'.format(num))
#    else:
#        print('The number({}) you entered is out of range'.format(num))
#
#print(test_range(11)) 

#string1 = 'The quick Brow Fox'   
#
#def calc(string):
#    count_low = 1
#    count_high = 1
#    
#    for i in string:
#        if i.islower():
#            count_low += 1
#        elif i.isupper():
#            count_high += 1
#        else:
#            pass
#    
#    return ('The number of upper letters: {}\
#            \nThe number of lower letters: {}'.format(count_high, count_low))
#
#print(calc(string1))

#a = [1,2,3,3,3,3,4,5]
#
#def unique_elements(a_list):
#    
#    b_list = []
#    
#    for i in a_list:
#        if i not in b_list:
#            b_list.append(i)
#    
#    return b_list
#
#print(unique_elements(a))

#def prime(n):
#    
#    if n == 1:
#        return False
#    
#    elif n == 2:
#        return True 
#    
#    else:
#        for i in range(2,n):
#            if n % i == 0:
#                return False
#            else:
#                return True
#print(prime(31))

#Liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#def even_numbers(a_list):
#    even_numbers = []
#    for i in a_list:
#        if i % 2 == 0:
#            even_numbers.append(i)
#    print('The even numbers from {} is {}'.format(a_list, even_numbers))
#
#even_numbers(Liste)

#def palyndrome(string):
#    
#    string = str(string)
#    string = string.lower()
#    rvs = string[::-1]
#    
#    if string == rvs:
#        return ('{} you entered is a palyndrome. '.format(string.))
#    else:
#        return ('{} you entered is not a palyndrome. '.format(string))
#
#a = 'Mehmet'    
#print(palyndrome(a))   


#import datetime

#now = datetime.datetime.now()
#
#print(now)

#today = datetime.datetime.today()
#
#print(today)

#year = datetime.datetime.year()
#
#print(year)

#print('Current year: ', datetime.date.today().strftime('%Y'))
#print('Current week: ', datetime.date.today().strftime('%B'))
#print('Week number of the year: ', datetime.date.today().strftime('%W'))
#print('Weekday of the week: ', datetime.date.today().strftime('%w')) 
#print('Day of the year: ', datetime.date.today().strftime('%j'))
#print('Day of the month: ', datetime.date.today().strftime('%d'))
#print('Day of week: ', datetime.date.today().strftime('%A'))  

#from datetime import datetime
#
#date = 'Jan 1 2014 2:43PM'
#    
#date_object = datetime.strptime('Jan 1 2014 2:43PM', '%b %d %Y %I:%M%p')
#print(date_object)
    
#r = lambda a : a+10
#
#print(r(10))

#a = [1,5,3,8,2,0,45,7]
#
#def test_data(a):
#    if len(a) == len(set(a)):
#        return True
#    else:
#        return False
#
#print(test_data(a))

#import random
#
#char_list = ['a', 'e', 'i', 'o', 'u']
#
#random.shuffle(char_list)
#print(''.join(char_list))

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = []
#for i in a:
#    if i in b:
#        if i not in c:
#            c.append(i)
#print(c)

#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
#b = [i for i in a if i % 2 == 0]
#
#print(b)

#intro = 'WELCOME TO ROCK, PAPER, SCISSORS'
#print('-'*len(intro))
#print(intro)
#print('-'*len(intro))
#
#name1 = input('What is your name: ')
#name2 = input('What is your name: ')
#
#
#
#user_input1 = input('Choose one: Rock, Paper Scissors')
#user_input2 = input('Choose one: Rock, Paper Scissors')
#def compare(u1, u2):
#
#
#    
#    u1 = u1.lower()
#    u2 = u2.lower()
#    
#    if u1 == u2:
#        return ('It is a tie')
#    
#    elif u1 == 'rock':
#        if u2 == 'scissors':
#            return ('Rock wins')
#        else:
#            return ('Paper wins')
#    
#    elif u1 == 'paper':
#        if u2 == 'scissors':
#            return ('Scissors win')
#        else:
#            return ('Paper wins')
#    
#    elif u1 == 'scissors':
#        if u2 == 'rock':
#            return ('Rock wins')
#        else:
#            return ('Scissors win')
#    
#    else:
#        return ('Invalid input. You have not entered rock, paper, scissors. \
#                Try again!')
#    
#    print()
#
#print(compare(user_input1, user_input2))

#import random 
#
#num = random.randint(1,9)
#guess = 0
#count = 0
#while guess != num and guess != 'exit':
#    
#    guess = input('Enter a number between 1 and 9')
#    
#    if guess == 'exit':
#        break
#    
#    guess = int(guess)
#    count += 1
#    
#    if guess > num:
#        print('You are high')
#    
#    elif guess < num:
#        print('You are low')
#    
#    else:
#        print('You got it')
#        print('It took you {} times to find it. '.format(count))

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]    
#
##c = [i for i in set(a) if i in set(b)]
##print(c)
#
#d = [i for i in a if i in b]
#print(d)
 
    
    
    
    
    
    
    
    
    
    





























    