#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:41:16 2020

@author: Sena-2
"""

#user_input = 'java.txt'
#x = user_input.split('.')
#print(x)

#def four(liste):
#    count = 0
#    
#    for i in liste:
#        if i == 4:
#            count += 1
#    print(count)
#
#liste = [1,45,3,8,4,90,6,5,4,1,3,4]    
#    
#four(liste)

#def ncharacter(string):
#    
#    return 2 * (string[:2])
#
#m = 'Mehmet'
#x = ncharacter(m)
#
#print(x)

#def vowel():
#    
#    vowel = ['a', 'e', 'i', 'o', 'u']
#    user_input = input('Give a letter to check: ')
#    user_input = user_input.lower()
#    
#    for i in vowel:
#        if user_input == i:
#            return True
#    return False
#
#print(vowel())

#def histo(liste):
#    
#    for i in liste:
#        print('*' * i)
#    print('\n')
#a = [1,5,3,6,8]
#histo(a)

#def conca(liste):
#    
#    result = ''
#    
#    for i in liste:
#        i = str(i)
#        result += i + ' '
#    return result 
#
#x = [1,45,'ed', 'Mehmet', 'was', 'here']
#print(conca(x))

#def stop(liste):
#    even = []
#    
#    for i in liste:
#        if i == 237:
#            break 
#        if i % 2 == 0:
#            even.append(i)
#    return even   
#numbers = [    
#    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#    958,743, 527
#    ]
#
#print(stop(numbers))
#   
def gcd(x,y):

    gcd = 1
    
    for i in range(int(y/2), 0, -1):
        if x % i == 0 and y % i == 0:
            gcd = i
            break
    return gcd
#
#print(gcd(20, 30))

#def gcd(x,y):
#    gcd = 1
#    
#    for i in range(int(y/2), 0, -1):
#        if x % i == 0 and y % i == 0:
#            gcd = i
#            break 
#    return gcd
#
#print(gcd(45, 81))

#def lcm(x,y):
#    
#    if x > y:
#        z = x
#    else:
#        z = y
#    
#    while True:
#        if z % x == 0 and z % y == 0:
#            lcm = z
#            break
#        z += 1
#    return lcm
#
#print(lcm(3,11))

#def lcm(x,y):
#    
#    if x > y:
#        z = x
#    else:
#        z = y
#    
#    while True:
#        if z % x == 0 and z % y == 0:
#            lcm = z
#            break
#        z += 1
#    
#    return lcm
#
#print(lcm(3, 12))
#print(lcm(4, 31))

#def gcd(x,y):
#    
#    gcd = 1
#    
#    for i in range(int(y/2), 0, -1):
#        if x % i == 0 and y % i == 0:
#            gcd = i
#            break
#        
#    return gcd

#print(gcd(17, 4))
#print(gcd(24, 4))
    
#def lcm(x,y):
#    
#    if x > y:
#        z = x
#    else:
#        z = x
#    
#    while True:
#        
#        if z % x == 0 and z % y == 0:
#            lcm = z
#            break
#        z += 1
#    return lcm
#
#print(lcm(4, 5))
    
#def integer(x,y):
#    
#    if not (isinstance(x, int)) and (isinstance(y, int)):
#        raise TypeError('Input must be integers: ')
#    return x + y
#
#print(integer(5, 4))
#print(integer(45, 'giles'))
    
#print('Mehmet Eyüpoğlu\n28\nAnkara/Turkey')

#amt = 10000
#int_rate = 3.5
#years = 7
#
#result = (amt * (1 + (int_rate * years))) - amt
#
#print(round(result, 2))
    
#import os.path
#
#print(os.path.isfile('mehmet.txt'))
#print(os.path.isfile('sena.txt'))
    
#import struct
#
#print(struct.calcsize('P')*8)
    
#import platform
#import os
#
#print(os.name)
#print(platform.system())
#print(platform.version())      
##
#print(platform.system()__doc__)  
    
#import site
#
#print(site.getsitepackages())
    
#from subprocess import call
#call(['ls', '-l'])

#import os
#print('Current file name: ', os.path.realpath(__file__))

#n = '234.456'
#print(float(n))
#print(int(float(n)))

#from os import listdir
#from os.path import isfile, join
#files_list = [f for f in listdir('/Users/mehmet-2') if isfile(join('/Users/mehmet-2', f))]
#print(files_list)
    
#for i in range(0, 10):
#    print('*', end = '')
    
import getpass
print(getpass.getuser())


























         

