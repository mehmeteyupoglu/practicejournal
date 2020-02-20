#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:31:08 2020

@author: Sena-2
"""

#print(id(pow(3,3)))
#print(id(27))
#print()

#print(*range(10), sep = ' /\\ ')

#b = [i for i in dir(int) if not i.starswith ('_')]
#print(b

#for i in dir(int):
#    if not i.startswith('_'):
#        print(i)

#num = 4
#print(num.bit_length())
#
#num = 5.2
#print(num.as_integer_ratio())
#
#num = 6.0
#
#print(num.as_integer_ratio())

file = open('mehmet\'s_file.txt', 'w')
file.write('Hello. This is Mehmet. I live in Turkey and am programming \
software currently')
file.close()

f = open('✍️ How I learned web development, software engineering, \
& ML _ Jason Benn.pdf', 'rb')
