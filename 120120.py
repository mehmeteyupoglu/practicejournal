#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 10:26:26 2020

@author: Sena-2
"""

#import keyword
#print(keyword.kwlist)

#osman = 're_de'
#mehmet = 'pro'
#
#osman, mehmet = mehmet, osman
#print(mehmet)

#print(*'Turkey', sep= ',')

#print(round(3.34234098, 4))

#nesne = '0123456789'

#print(nesne[:4])
#print(nesne[4:])
#print(nesne[7:4:-1])
#print(nesne[0:5])
#print(nesne[1:6:2])
#print(nesne[::3])

#for i in reversed(nesne):
#    print(i, end = '')

#b = [i for i in reversed(nesne)]
#print(b)
#
#c = 'adlkjha qpoew afjdha lakdj h'
##print(*sorted(c))
##
##d = '123847618375193846192'
##print(*sorted(d))
#
##nesne.replace('0','3')
##
##print(nesne)
##print(nesne.split('3','6',3))
#
##print(c.upper())
##print(c.capitalize())
#
#
#b = 'Manchester United'
##b.join('Manchester United')
##print(b)
##print(b.count('a'))
##print(b.count('e'))
#
##print(b.count('e',10))
#
##print(b.index('M'))
##print(b.index('e'))
##print(b.center())
##print(b.isalpha())
##print(b.isalnum())
##print(b.isprintable())
##
##
##print(*range(1,10,3))
#
#liste = [1,2,3,4,'a','b','c','d']
##
##del liste[1]
#
#print(liste)
#liste[1] : '2'
#
#print(liste)
#
#del liste
#print(liste)

#print(tuple(b))
#
#list(b)

#a1 = [1,2,3,4,5,]
#print(dir(list))

#list_2 = ['é','34', '56', 'Sena', 'Mehmet']
#
#liste = liste+list_2
##print(liste)
##for i in range(len(list_2)):
##    if i not in liste:
###        liste += i
###print(liste)
##
####list_3 = [i for i in list_2 if i in list_2 liste.append(i)]
####print(liste)
###
####print(liste.sort())
###print(liste.count(1))
##print(liste.clear())
#
##print(bin(23))
#
#liste4 = [3,4,5,2,5]
#
#print(sum(liste4))


#f = open('dosya_practice.txt', 'w')
#
#f.write('This is the first thing I write this file. I really love \nwhat I do \
#\nTherefore, I think I can complete eveything I undertake as a duty')
#
#f.close()
#
#f = open('dosya_practice.txt')
#print(f)
#f.close()
#
#f = open('dosya_practice.txt', 'r')
#
#print(f.readlines())

#f.close()

#f = open('dosya_practice.txt', 'r')
#
#print(f.readline())
#print(f.readline())
#print(f.readline())
#f.close()

#f = open('dosya_practice.txt', 'a')
#
#f.write('\nThis is the added line. Let\'s see if it works')
#f.close()
#
#f = open('dosya_practice.txt')
#print(f.read())
#f.close

#words = {'book' : 'kitap', 'write' : 'yazmak'}
#
##print(words)
#
##print(words[i])
#
#words['food'] = 'yemek'

#print(words)
#print(words.keys())
#print(words.values())
##print(words.items())
#words.popitem()
#
#print(words)
#
#words.popitem()
#
##print(words)
#liste = list(range(1,100,3))
#
#sets = {i for i in liste if i < 100}
#print(sets)
#
#sets.add('d')
#
#print(sets)
#
#sets.

#s1 = {1,2,3,4,5,66,7,8,5,4,3,3,}
#s2 = {4,5,7,8,8,3,2,5,1,2,3,}
#
##print(s1.difference(s2))
##print(s2.difference_update(s1))
##print(*s2)
##print(s1.intersection(s2))
##s1.discard(2)
##print(s1)
#
##print(s1.isdisjoint(s2))
#print(s1.union(s2))
#
#even_num = lambda num : num % 2 == 0
#print(even_num(33))

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
#b = [i for i in a if i<5]
#print(b)

#num = int(input('Please enter a num:  '))
#c = []
#
#for i in a:
#    if i < num and i not in c:
#        c.append(i)
#print(c)

#b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#b = [1,3,3,3,3,3,3,3,3,3,3,3]
#a = [1, 2, 3, 4, 5, 6, 7, 8, 21]
#c = []

##d = [i for i in a if i in b and i not in c c.append(i)]
#
#
#for i in a:
#    if i in b and i not in c:
#        c.append(i)
#print(c)

#def mutual(x,y,z):
#    for i in x:
#        if i in y and i not in z:
#            z.append(i)
#
#mutual(b,a,c)
#print(c)

#word = input('Give me a name:  ')
#word = str(word)
#word = word.lower()
#rvs = word[::-1]
#print(rvs)
#
#
#if word == rvs:
#    print('{} is a palyndrome.'.format(word))
#else:
#    print('{} is not a palyndrome.'.format(word))
#"""
#Make a two-player Rock-Paper-Scissors game. 
#(Hint: Ask for player plays (using input), 
#compare them, print out a message of congratulations to the winner, 
#and ask if the players want to start a new game)
#
#Remember the rules:
#
#Rock beats scissors
#Scissors beats paper
#Paper beats rock
#
#"""
#import sys

#print('-'*30)
#
#print("WELCOME TO ROCK, PAPER, SCISSORS GAME" )
#
#print('-'*30)
#
#p1 = input('What is your name: ')
#p2 = input('What is your name: ')
#
#u1 = input('{}, what do you want to choose: Rock, paper, scissors?'.format(p1))
#u2 = input('{}, what do you want to choose: Rock, paper, scissors?'.format(p2))
#
#u1 = u1.lower()
#u2 = u2.lower()
#def compare(u1,u2):
#    
#    if u1 == u2:
#        return ('It is a tie:')
#    
#    elif u1 == 'rock':
#        if u2 == 'paper':
#            return ('Paper wins. Congratulations {}'.format(p2))
#        else:
#            return ('Rock wins. Conratulations {}'.format(p1))
#        
#    elif u1 == 'paper':
#        if u2 == 'scissors':
#            return ('Scissors wins. Congratulations {}'.format(p2))
#        else:
#            return ('Paper wins. Conratulations {}'.format(p1))
#        
#    elif u1 == 'scissors':
#        if u2 == 'rock':
#            return ('Rock wins. Congratulations {}'.format(p2))
#        else:
#            return ('Scissors wins. Conratulations {}'.format(p1)) 
#    else:
#        return ('It is invalid. Please give a valid answer.')
#        sys.exit()
#
#print(compare(u1,u2))
#import random
#
#print(' '*15, '-'*30)
#
#print(' '*15,"WELCOME TO GUESSING GAME" )
#
#print(' '*15,"Put \'quit\' to exit! " )
#
#print(' '*15, '-'*30)
#
#num = random.randint(1,15)
#count = 0
#
#while u1 != 'quit' and u1 != num:
#    u1 = input('Guess a the number between 1 and 15:  ')
#    
#    if u1 == 'quit':
#        break 
#    
#    u1 = int(u1)
#    count += 1
#    
#    if u1 < num:
#        print('You are low')
#    elif u1 > num:
#        print('You are high')
#    elif u1 == num:
#        print('You got it. It took you {} times.'.format(count))

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = []


#a = random.sample(range(1,30), 12)
#print(a)

#import random
#
#a = random.sample(range(1,30),14)
#b = random.sample(range(1,30),18)
#
##c = [i for i in set(a) if i in b]
##print(c)
#
#
#def list_overlap(a,b):
#    for i in set(a):
#        if i in b:
#            a = set(a)
#            b = set(b)
#            c = a.intersection(b)
#            return c
#        
#print(list_overlap(a,b))
#
#def find_prime(x):
#    if x %
#b = [1,4,6,'d',3,8]
#def list_ends(a):
#    return [a[0], a[len(a)-1]]
#
#print(list_ends(b))

#def gen_fib():
#    
#    num = int(input('How many fibonacci nums would you like to create:  '))
#    
#    i = 1
#    
#    fib_num = []
#    
#    if num == 0:
#        fib_num = []
#    
#    elif num == 1:
#        fib_num = [1]
#    
#    elif num == 2:
#        fib_num = [1,1]
#    
#    elif num > 2:
#        fib_num = [1,1]
#        while i < (num-1):
#            fib_num.append(fib_num[i]+fib_num[i-1])
#            i += 1
#    return fib_num
#
#print(gen_fib())


#a = [1,4,5,8,9,2,1,4,7,5,2,2,6,8,9,7,4,34,5,7,8,9,4,345,6,9,7]
#
#def remove_dup(a):
#    y = []
#    
#    for i in a:
#        if i not in y:
#            y.append(i)
#    return y
#
#def remove_dup2(a):
#    return list(set(a)) 
#
##print(remove_dup(a))
#print(remove_dup2(a))

#string1 = 'My name is Mehmet!'
##
#
#def rvs_ord(a):
#    b = ' '.join(a.split()[::-1])
#    return b
#    
#print(rvs_ord(string1))
#
#board_size = int(input('What size of game board would you like?  '))
#
#print('---'*board_size)
#print('|'*board_size+1)

#print(__name__)

#size = int(input('What size of your board?  '))

#def hor_size(size):
#    print(' --- ' * (size+1))
#
#def ver_size(size):
#    print('|   ' * size)
#    
#if __name__ == '__main__':
#    
#    size = int(input('What size of your board?  '))
#    
#    for index in range(size):
#        hor_size(size)
#        ver_size(size)
#    print(hor_size)

def maks(a,b,c):
    a = int(input('Give a number: '))
    b = int(input('Give a number: '))
    c = int(input('Give a number: '))
    d = list(a,b,c)   
    



    
    
    


    
    

    




































































