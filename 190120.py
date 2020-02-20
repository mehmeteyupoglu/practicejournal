#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:17:45 2020

@author: Sena-2
"""

'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
#string = 'Mehmet'
#rvs = ''
#for i in string:
#    rvs = i + rvs
#
#print(rvs)

'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''
#u_i = int(input('Please enter a number: '))
#times_table = (f'Welcome to {u_i} Times Table')
#print('-'*len(times_table))
#print(times_table)
#print('-'*len(times_table))
#
#for i in range(1,12):
#    print(f'{i} x {u_i} = {i*u_i}')

'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''

#u_i = int(input('Please enter a number: '))
#times_table = ('Welcome to Times Table')
#print('-'*len(times_table))
#print(times_table)
#print('-'*len(times_table))
#
#for i in range(1,13):
#    print('-'*len(times_table))
#    print('Welcome to {i} Times Table')
#    print('-'*len(times_table))
#    
#    for x in range(1,13):
#        print(f'{x} x {i} = {x*i}')
#    print('#'*len(times_table))

'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''
#
#total = 0
#user_input = input('Enter a number: ')
#numbers = []
#while user_input.lower() != 'exit':
#    while not user_input.isdigit():
#        print('Enter a number: ')
#        user_input = input('Enter a number: ')
#    numbers.append(int(user_input))
#    user_input = input('Enter the next number:  ')    
#    
#    
#
#for i in numbers:
#    total += i

#print('The mean of {} is {}'.format(numbers, total/len(numbers)))
#
#user_input = input('Please enter a number type exit to stop:> ')
#numbers = []
#while user_input.lower() != 'exit':
#    while not user_input.isdigit():
#        print('That is not a number! Numbers only please:> ')
#        user_input = input('Try again:> ')
#    numbers.append(int(user_input))
#    user_input = input('Please enter next number:> ')
#total = 0
#for number in numbers:
#    total += number
#
#print(f'Mean is {total/len(numbers)}')    
#print(sum(numbers)/len(numbers))    

'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''
#fact = 1
#for i in range(1, 16):
#    fact = fact * i
#print(fact)


'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''
#num = 20
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
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''




'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''

#star = '*'
#for i in range(1,7):
#    for j in range(1,6):
#        
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
          


'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''
#a = 0
#b = 1
#fib = {}
#for i in range(1,13):
#    fib[i] = a
#    a, b = b, a+b
#    
#print(fib)

'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''
#companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
#data_type = ['open', 'high', 'low', 'close']
#data_sets = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
#[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]
#d = {}
#for i in companies:
#    d[i] = dict(zip(data_type,data_sets[i]))
#print(d)

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
'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''

#import datetime
#
#today = datetime.date.today()
#
#holiday = datetime.date(2020, 7, 22)
#
#delta = holiday-today
#
#print('There are {} days to your holiday.'.format(delta.days))

#import datetime
#
#today = datetime.date.today()
#holiday = datetime.date(2020, 7, 12)
#delta = holiday-today
#
#print('There are {} days to your holiday.'.format(delta.days))

'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''
#import random
#alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
#d = {}
#for i in alphabet:
#    d[i] = random.randint(1,100)
#
#print(d)
#
#import matplotlib.pyplot as plt
#
#x, y = zip(*d.items())
#
#print(plt.bar(x,y))

'''
Question 6
Write a function that will copy the contents of one file to a new file.
'''
#def copy_file(infile, outfile):
#    
#    with open(infile) as file1:
#        with open(outfile, 'w') as file2:
#            file2.write(file1.read())

 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
