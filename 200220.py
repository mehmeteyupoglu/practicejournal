#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:33:03 2019

@author: Mehmet
"""

# 1 Ask the user for the radius of a circle and then print the area
#import math
#radius = int(input('Enter the radius'))
#pi = math.pi
#area = pi * (radius ** 2)
#
#print('The area is : {}'.format(area))


# 3 Obtain the sum of two integers

#a = 4
#b = 5
#sum_of_two = a + b
#print('The sum of a and b: {}'.format(sum_of_two))

# 4 Obtain the product of two integers

#num1 = int(input('Enter a number: '))
#num2 = int(input('Enter another number: '))
#product = num1 * num2
#print('The product of {} and {} is : {}.'.format(num1, num2, product))

'''
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
'''
#user_input = int(input('Enter a number: '))
#
#if user_input == 1:
#    print('one')
#elif user_input == 2:
#    print('two')
#elif user_input == 3:
#    print('three')
#elif user_input == 4:
#    print('four')
#elif user_input == 5:
#    print('five')
#else:
#    print('Invalid input. Please try again.')

'''
Repeat the previous task but this time the user will input a string and the
code will ouput the integer value. Convert the string to lowercase first.
'''
#user_input = input('Enter an number between one and five:  ')
#user_input = user_input.lower()

#if user_input == 'one':
#    print('1')
#elif user_input == 'two':
#    print('2')
#elif user_input == 'three': 
#    print('3')
#elif user_input == 'four':
#    print('4')
#elif user_input == 'five': 
#    print('5')
#else:
#    print('Invalid input. Please enter a string between one and five...')
#    

'''
Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the number. If they guess too high or too low, tell them they
have not won. Tell them they win if they guess the correct number.
'''
#user_guess = int(input('Please enter a digit between 1 and 10:  '))
#num = 6
#
#while user_guess != num:
#
#    if user_guess == num:
#        print('You won')
#    
#    elif user_guess < num:
#        print('You are low')
#        user_guess = int(input('Please enter a digit between 1 and 10:  '))
#        
#    elif user_guess > num:
#        print('You are high')
#        user_guess = int(input('Please enter a digit between 1 and 10:  '))
#
#    else:
#        user_guess = int(input('Invalid input. Please enter a digit between 1 and 10:  '))

'''
Ask the user to input their name. Check the length of the name. If it is
greater than 5 charactelrs long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
'''
#name = input('Enter your name: ')
#
#if len(name) > 5:
#    print('Your name has {} characters.'.format(len(name)))
#else:
#    print('The length of your name is a secret. ')

'''
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero
'''
#num1 = int(input('Enter an integer'))
#num2 = int(input('Enter another integer'))
#
#if num1 > 15 and num2 > 15:
#    print('The product of num1 and num2 is {}'.format((num1 * num2)))
#elif num1 > 15 or num2 > 15:
#    print('The sum of num1 and num2 is {}'.format((num1 + num2)))
#elif num1 < 15 and num2 < 15:
#    print('{}'.format(0))
#else:
#    print('Invalid input. Run the program again to get the result. ')

'''
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
'''
#var_1 = 5
#var_2 = 8
#
#var_1, var_2 = var_2, var_1
#print('Originally var_1 was {} and now it is {}'.format(var_2, var_1))
#print('Originally var_2 was {} and now it is {}'.format(var_1, var_2))

'''
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
#num1 = int(input('Enter a number between 1 and 100:  '))
#num2 = int(input('Enter a number between 1 and 100:  '))
#
#while num1 < 0 or num2 < 0 or num1 > 100 or num2 > 100 or num1 == num2:
#    print('Numbers must be different values between 1 and 100.')
#    num1 = int(input('Enter a number between 1 and 100:  '))
#    num2 = int(input('Enter a number between 1 and 100:  '))
#    
#if num1 < num2: 
#    for i in range(num1, num2+1):
#        print(i, end = ',')
#else:
#    for i in range(num2, num1+1):
#        print(i, end = ',')

'''
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
#user_input = str(input('Give me a name to reverse:  '))
#rvs = ''
#
#for i in user_input:
#    rvs = i + rvs
#
#print(rvs.title())


'''
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''
#num = int(input('Give me a number. It must be an integer: \n'))
#
#for i in range(1, num+1):
#    print('{} x {} = {}'.format(i, num, (i*num)))
#print('####### End of the time table.')

'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''
#for i in range(1,13):
#    print('Welcome to {} times table'.format(i))
#    for j in range(1, 13):
#        print('{} x {} = {}'.format(i, j, i*j))
#    print('\n\n')

'''
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''
#user_input = input('Enter a number: ')
#numbers = []
#
#while user_input.lower() != 'exit':
#    while not user_input.isdigit():
#        print('Invalid input. ')
#        user_input = input('Enter a number: ')
#    numbers.append(int(user_input))
#    user_input = input('Enter another number. ')
#    
#total = 0
#
#for i in numbers:
#    total += i
#    
#print('Total of the numbers: {}. Even of the numbers: {}'.format(total, total/len(numbers)))


'''
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''
#n = 15
#fact = 1
#
#for i in range(1, n+1):
#    fact *= i
#
#print(fact)

'''
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''
#num = int(input('How many fib nums would you like to see'))
#fib = []
#a = 0
#b = 1
#
#for i in range(1, num+1):
#    a, b = b, a+b
#    fib.append(a)
#
#print(fib)



'''
     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''
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
        
         
'''

Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
#
#even = []
#odd = []
#
#for i in range(1, 100):
#    if i % 2 == 0:
#        even.append(i)
#    else:
#        odd.append(i)
#print('The even numbers: ', even)
#print('The odd numbers : ', odd )

'''
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''

capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
            }
#user_input = input('Which country would you like to check:  ')
#user_input = user_input.lower()
#
#while ('united kingdom' not in user_input and not user_input.isalpha()):
#    if 'united states' == user_input:
#        break
#    print('You must enter strings')
#    user_input = input('Which country would you like to check: ')
#
#user_input = user_input.title()
#
#if user_input in capitals:
#    print('{}\'s capital is {}'.format(user_input, capitals[user_input]))
#else:
#    print('No data available')


'''
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''
#a = 0
#b = 1
#fib = {}
#
#for i in range(1,13):
#    fib[i] = a
#    a, b = b, a+b
#    
#print(fib)

'''
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''
#data_types = ['open', 'high', 'low', 'close']
#companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
#data = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
#[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]
#dictionary = {}
#
#for i in range(len(companies)):
#    dictionary[companies[i]] = dict(zip(data_types, data[i]))
#    
#print(dictionary)


'''
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''

#import random 
#keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#dictionary = {}
#
#for i in keys:
#    dictionary[i] = random.randint(1,100)
#
#import matplotlib.pyplot as plt
#x,y = zip(*dictionary.items())
#
#print(plt.bar(x,y))





