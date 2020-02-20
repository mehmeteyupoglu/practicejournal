#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:13:11 2020

@author: Sena-2
"""

"""
Exercise 1

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will 
turn 100 years old.

"""
#name = input("What is your name? ")
#age = input("How old are you? ")
#age = int(age)
#b_day = 2020 - age 
#
#print(f'{name}, you will turn 100 in ', b_day+100)



"""
Exercise 2

Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an even / odd 
number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number 
to divide by (check). If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.

"""
#while True:
#    
#    user_input = input('Enter a number to check: ')
#    
#    if user_input == 'exit':
#        break
#
#    user_input = int(user_input)
#    
#    if user_input % 2 == 0:
#        print('It is an even number')
#        
#    elif user_input % 2 == 0 and user_input % 4 == 0:
#        print('It is an even number and it is divided evenly by 4')
#    
#    else:
#        print('It is an odd number')

"""
Exercise 3 

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  
and write a program that prints out all the elements of the list that are less 
than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the 
elements less than 5 from this list in it and print out this new list.

Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from 
the original list a that are smaller than that number given by the user.
"""

"""
Solution 1
"""
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [i for i in set(a) if i < 5]
#print(b)


"""
Solution 2
"""
#num = int(input("Enter a number"))
#
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [i for i in set(a) if i < num]
#print(b)

"""
Create a program that asks the user for a number and then prints out a list of 
all the divisors of that number. (If you don’t know what a divisor is, it is a 
number that divides evenly into another number. For example, 13 is a divisor of 
26 because 26 / 13 has no remainder.)
"""
#user_input = int(input("Enter a number"))
#divs = []
#
#for i in range(1, user_input+1):
#    if user_input % i == 0:
#        divs.append(i)
#
#print(divs)

"""
Exercise 5

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  
and write a program that returns a list that contains only the elements that 
are common between the lists (without duplicates). Make sure your program works 
on two lists of different sizes.
        
"""
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = []
#
#for i in a:
#    if i in b:
#        if i not in c:
#            c.append(i)
#
#print(c)

"""
Exercise 6
Ask the user for a string and print out whether this string is a palindrome or 
not. 
"""

user_input = input('Enter a name to check whether it is a palyndrome')
user_input = user_input.lower()
rvs = user_input[::-1]

if user_input == rvs:
    user_input = user_input.title()
    print('{} is a palyndrome'.format(user_input))
else:
    print('{} is not a palyndrome'.format(user_input))


    


