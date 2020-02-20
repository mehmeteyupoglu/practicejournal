#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:28:15 2020

@author: Sena-2
"""

#def string_length(string):
#    
#    count = 0
#    
#    for i in string:
#        count += 1
#    return count
#
#string = 'string'
#
#print(string_length(string))

#def string_slicing(str1):
#    
#    if len(str1) < 2:
#        return ''
#    
#    return str1[0:2] + str1[-2:]
#
#print(string_slicing(string))

#def char_mix(a,b):
#    
#    new_a = b[:2] + a[2:]
#    new_b = a[:2] + b[2:]
#    
#    return new_a + ' ' + new_b
#
#print(char_mix('abc', 'xyz'))

#def adding(a):
#    
#    if len(a) < 3:
#        return a
#    else:
#        if a[-3:] == 'ing':
#            return a + 'ly'
#        else:
#            return a + 'ing'
#        
#print(adding(a = 'getting'))
#
#print(adding(a = 'hair'))
#
#print(adding(a = 'er'))

#def chara(string, n):
#    first = string[:n]
#    second = string[n+1:]
#    
#    return first + second
#
#print(chara('Python', 3))
#
#
#def exchange(string):
#    
#    string[]
#string = 'string'
#
#def stringa(string):
#    return string[-1] + string[1:-1] + string [0]
##
#print(stringa(string))
#
#print(string[1:-1])
#def odd_values_string(str):
#  result = "" 
#  for i in range(len(str)):
#    if i % 2 == 0:
#      result = result + str[i]
#  return result
#
#print(odd_values_string('abcdef'))
#print(odd_values_string('python'))

#
#def add_value(string):
#    
#    result = ''
#    for i in range(len(string)):
#        if i % 2 == 0:
#            result += string[i]
#    return result
#
#print(add_value('Classify'))

#def hesap_mak():
#
#    giris = 'Hesap Makinesi Uygulamasına Hoş Geldiniz'
#
#    print(len(giris)*'-')
#    print(giris)
#    print(len(giris)*'-')
#
#    giris2 = '''
#    (1) topla
#    (2) çıkar
#    (3) çarp
#    (4) böl
#    (5) karesini hesapla 
#    (6) karekök hesapla '''
#
#    print(giris2)
#    
#    user_input = int(input('Yukarıdaki sayılardan birini seçin!'))
#    
#    if user_input == 1:
#        sayı1 = int(input('Sayı girin.'))
#        sayı2 = int(input('Sayı girin.'))
#        
#        return sayı1 + sayı2 
#    
#    elif user_input == 2:
#        sayı1 = int(input('Sayı girin.'))
#        sayı2 = int(input('Sayı girin.'))
#        
#        return sayı1 - sayı2 
#    
#    elif user_input == 3:
#        sayı1 = int(input('Sayı girin.'))
#        sayı2 = int(input('Sayı girin.'))
#        
#        return sayı1 * sayı2
#    
#    elif user_input == 4:
#        sayı1 = int(input('Sayı girin.'))
#        sayı2 = int(input('Sayı girin.'))
#        
#        return sayı1 / sayı2
#    
#    elif user_input == 5:
#        sayı1 = int(input('Sayı girin.'))
#        
#        return sayı1 * sayı1
#    
#    elif user_input == 6:
#        sayı1 = int(input('Sayı girin.'))
#        
#        return sayı1 ** 0.5
#    
#    else:
#        user_input = int(input('Enter a number to continue!'))
#        
#print(hesap_mak())

#def fibonacci():
#    user_input = int(input('How many numbers would you like to generate? '))
#    a = 0 
#    b = 1
#    fib = []
#
#    for i in range(1, user_input+1):
#        a, b = b, a+b
#        fib.append(a)
#
#    print(fib)
#    
#fibonacci() 
#import random
#
#def guessing_game():
#    
#    user_input = 0
#    number = random.randint(1,9) 
#    count = 0
#    
#    while user_input != 'exit' and user_input != number:
#        
#        user_input = input('Enter a number between 1 and 9')
#        
#        if user_input == 'exit':
#            break
#        
#        user_input = int(user_input)
#        count += 1
#    
#        if user_input > number:
#            print('You are higher!')
#    
#        elif user_input < number:
#            print('You are lower!')
#        
#        else:
#            print('You got it. It took you {} times.'.format(count))
#
#guessing_game()

#string = 'My name is Mehmet'
#
#def rvs(string):
#    return ' '.join(string.split()[::-1])
#    
#print(rvs(string))

#def check(liste1, k):
#    
#    for i in liste1:
#        if i == k:
#            return True
#    
#    return False
#
#
#a = [1,4,7,'k',9,10]
#
#print(check(a, 7))
#print(check(a, 'k'))
#print(check(a, 34))

#def drawboard(kamal):
#    kamal = int(kamal)
#    i = 0
#    ho = "--- "
#    ve = "|   "
#    ho = ho * kamal
#    ve = ve * (kamal+1)
#    while i < kamal+1:
#        print ho
#        if not (i == kamal):
#            print ve
#        i += 1

#def drawboard(num):
#    
#    num = int(num)
#    i = 0
#    
#    ve = '|  '
#    ho = '--'
#    
#    ve = ve * num
#    ho = ho * (num+1)
#    
#    while i < (num+1):
#        print(ho)
#        if not (i == num):
#            print(ve)
#        i += 1
#
#drawboard(4)

#def max_3(a,b,c):
#    
#    a = int(a)
#    b = int(b)
#    c = int(c)
#    
#    
#    if a > b:
#        if a > c:
#            return a
#    
#    elif b > a:
#        if b > c:
#            return b
#    
#    elif c > a:
#        if c > b:
#            return c
#    
#
#print(max_3(44,'32', 5))
#print(max_3('35', 5, 7))

#def bday_finder():
#    
#    bdays = {'Mehmet': '22.10.1991', 
#             'Sena': '27.11.1992',
#             'Ebik' : '08.08.2000'}
#    welcome_statement = '''Welcome to the birthday dictionary. We have \
#the birthday information of Mehmet, Sena and Ebik. '''
#
#    print(welcome_statement)
#    user_input = input('Who would you like to know? ')
#    user_input = user_input.title()
#    
#    return 'The birthday of {} is : '.format(user_input) + bdays[user_input]
#
#print(bday_finder())








    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


        



        


    

