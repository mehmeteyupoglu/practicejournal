#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:56:20 2020

@author: Sena-2
"""


#liste1 = [1,4,6,3,7,9, 4, 9, 6, 4]
#
##print(dir(list))
#
#for i in liste1:
#    liste1.remove(i)
#    print(i)
#    print(liste1)
##
##print(liste1)
#
##for i in liste1:
##    liste1.pop(i)
#
##print(liste1.sort())
#
##print(liste1.index(7))
#
#print(liste1.count(4))
#
#liste1.clear()
#print(liste1)

#print(bin(4))

#print(hex(866))
    
#sayi = 888
#
#print(sayi.bit_length())

#dictionary = {'i' : '1', 'b' : '2', 'c' : '3', 'd' : '4'}
#
#d = {i for i, x in dictionary}
#
#print(d)

#for i, x in dictionary.items():
#    print(i, '===>', x)

#print(set(dictionary))

#set1 = {'i', 'b', 'c', 'd'}
#set2 = {'2', '3', '4', 'b'}
#
###print(set1.difference(set2))
##set1.update(set2)
##
###print(set2)
###print(set1)
###
###print(set1.isdisjoint(set2))
##print(set2.issubset(set1))
#
#list1 = [1,5,8,3,6,2,0]
#list2 = ['a', 'b', 'c', 'd']
#
#print(*zip(list1, list2))

#num = lambda num: num % 2 == 0
#
#print(num(3))


#def calc_mean(first, *remainder):
#    '''
#    This calculates the successive numbers
#    
#    ''' 
#    mean = (first + sum(remainder)) / (1+len(remainder))
#    
#    return mean 
#
#print(calc_mean(1,56, 3, 8, 399, 0, 0, 3))

#class Patient(object):
#    '''Medical centre patient'''
#    
#    def __init__(self, name, age):
#        
#        self.name = name
#        self.age = age
#    
#mehmet = Patient('Mehmet Eyupoglu', 28)
#sena = Patient('Sena Eyupoglu', 27)
#
#print   

#class Patient(object):
#    '''Medical centre patient'''
#    
#    status = 'patient'
#    
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#        self.conditions = []
#    
#    def get_details(self):
#        print(f'Patient record: {self.name}, {self.age} years old.'\
#              f'Current information: {self.conditions}. ')
#    
#    def add_info(self):
#        self.conditions.append(information)
#
#mehmet = Patient('Mehmet Eyupoglu', 28)
#sena = Patient('Sena Eyupoglu', 27)

#class BankAccount(object):
#    '''Docstring to go here'''
#    
#    def __init__(self, balance=0.0):
#        self.balance = balance
#    
#    def display_balance(self):
#        print(f'Your balance is {self.balance}')
#    
#    def make_deposit(self):
#        amount = float(input('How much would you like to deposit? :> '))
#        self.balance += amount
#        print(f'Balance is now {self.balance}. ')
#    
#    def make_withdrawal(self):
#        amount = float(input('How much woul you like to deposit? :> '))
#        if amount > self.balance:
#            print(f'You do not have sufficient funds, your balance is \
#                  {self.balance}. ')
#        else:
#            self.balance -= amount
#            print(f'Withdrawal successful: balance is now {self.balance}. ')

#import math
#
#class Circle(object):
#    '''Represents a circle with radius. Calculates area. '''
#    
#    def __init__(self, radius):
#        self.radius = radius
#        
#    def calc_area(self):
#        area = math.pi * (self.radius)**2
#        return area
#
#my_circ = Circle(8)
#
#print(my_circ.calc_area())

#tuplex = 5,7,0,2,6
#print(tuplex)
#print(type(tuplex))
#
#tuplex2 = 5,
#print(type(tuplex2))

#tuplex = 5,2,7
#
#n1, n2, n3 = tuplex
#
#print(n1+n2+n3)

#a = 0
#b = 1
#fib = []
#for i in range(1,11):
#    a, b = b, a+b
#    fib.append(a)
#
#print(fib)

#tuplex = 5,7,3,9
#tuplex = tuplex + (88,22,)
#
#print(tuplex)
#
#tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e')
#
#string = ''.join(tup)
#
#print(string)

#tuple1 = ('M', 'e', 'h', 'm', 'e', 't')
#
#def convert(tuple1):
#    
#    string = ''.join(tuple1)
#    return string
#
#print(convert(tuple1))

#fib = []
#a = 0
#b = 1
#
#for i in range(1,10):
#    a, b = b, a+b
#    fib.append(a)
#    print(fib)
#
#import random 
#
#n = random.randint(1,10)
#
#user_input = int(input('Sayı gir'))
#
#guess = 0
#count = 0
#
#while user_input != 'exit' and user_input != guess:
#    
#    guess = input('Numara gir')
#    
#    if guess == 'exit':
#        return

#tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
#
#item = tuplex[3]
#item2 = tuplex[-4]
#
#print(item, item2)

#create a tuple
#tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7 
#
#print(tuplex.count(4))

#tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
#
##print('r' in tuplex)
##print('a' in tuplex)
#
##liste = [1,5,8,'k', 'b', '5']
##tuplex = tuple(liste)
##
##print(tuplex)
##tuple2 = tuplex[:2] + tuplex[4:]
##
##print(tuple2)
#
##print(tuplex[:5])
##print(tuplex[:-3])
##print(tuplex.index('o'))
#print(len(tuplex))

#set1 = set()

#set1 = {1,7,3,9,5}
#set2 = {'e', 'b', 5, 7, 3}
#set3 = {7,9}
#set4 = {'e', 5, 3, 7, 'b', 'd', 'h', 77}
#
##for i in set1:
##    print(i, end= ',')
#
#set1.add(5)
#set1.add('e')
#
#print(set1)

#set1.remove(7)
#
#print(set1)

#set1.discard(6)
#print(set1)

#print(set1.intersection(set2))

#print(set1.union(set2))

#print(set1.difference(set2))

#print(set1.issubset(set2))
#print(set4.issubset(set2))
#print(set4.issuperset(set2))

#print(set1.clear())
#print(set1)

#def maximum(set1):
#    
#    maximum = 
#    
#    for i in set1:
#        
#print(max(set1))
#print(min(set3))
    
#div = []
#    
#for i in range(1500, 2701):
#    if i % 7 == 0 and i % 5 == 0:
#        div.append(i)
#
#print(div)
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#*

#star = '*'
#n = 5
#
#for i in range(n):
#    for j in range(i):
#        print('*', end = ' ')
#    print('') 
#
#for i in range(n, 0, -1):
#    for j in range(i):
#        print('*', end = ' ')
#    print('')
#user_input = input('Enter a word:  ')
#rvs = user_input[::-1]
#
#print(rvs)

#a = [1,6,3,0,4,22,6,4,7,1,9]
#
#count_even = 0
#count_odd = 0
#
#for i in a:
#    if i % 2 == 0:
#        count_even += 1
#    else:
#        count_odd += 1
#print(f'The number of even numbers: {count_even}\
#      \nthe number of odd numbers: {count_odd}')

#datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], \
#            {"class":'V', "section":'A'}]
#
#for i in datalist:
#    x = type(i)
#    print(f'{i} ==> {x}')

#for i in range(6):
#    if i == 3 or i == 6:
#        continue
#    print(i, end='')

#x, y = 0, 1
#
#while y<50:
#    print(y, end=',')
#    x,y = y, x+y
#string = 'Python 3.2'


#def calc(string):
#    
#    alpha1 = 0
#    num1 = 0
#
#    for i in string:
#        if i.isalpha():
#            alpha1 += 1
#        
#        elif i.isdigit():
#            num1 += 1
#        
#        else:
#            pass
#    return (f'The number of letters: {alpha1}\
#            \nThe number of digits: {num1}')
#print(calc(string))
        





    


        


        
        


































