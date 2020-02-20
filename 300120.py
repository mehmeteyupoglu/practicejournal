#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:34:11 2020

@author: Sena-2
"""

#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#input_text = 'hello'

#output = ''
#for i in input_text:
#    alpha_index = alphabet.find(i)
#    output = output + alphabet[alpha_index+3]
#    print(output)
#
#def shift_amount(i):
#    return i%26
#
##output1 = ''
##
##for char in input_text:
##    alpha_index = alphabet.find(char)
##    output1 = output1 + alphabet[shift_amount(alpha_index+30)]
##print(output1)
#
#def encrypt(text, required_shift):
#    output = ''
#    for i in text:
#        if i not in alphabet:
#            output = output + i
#        else:
#            alpha_index = alphabet.find(i)
#            output = output + alphabet[shift_amount(alpha_index+required_shift)]
#    print(output)
#    
#text = 'The cat sat on the mat.'
#
#print(encrypt(text, 5))

L = [2,5,3,7,4]
#
#for i in L:
#    for x in L:
#        if i + x == 10:
#            print(i, x)

#def two_sum(L, target):
#    
#    for i in L:
#        list_index = L[]
#        if list_index(i) + list_index(i+1) == target:
#            print(i, L[i+1])
#print(two_sum(L, 10))
#d = dict()
#for i in L:
#    d[i] = L.index(i)
#print(d)

#def two_sum(nums, target):
#        d = {}
#        
#           
#        for i in range(len(nums)):    
#            if target - nums[i] in d:
#                print(d)
#                return [d[target-nums[i]],i]
#            
#            d[nums[i]] = i
#            
#        return -1

#def two_sums(nums, target):
#    d = {}
#    
#    for i in range(len(nums)):
#        if target - nums[i] in d:
#            print(d)
#            return [d[target-nums[i]],i]
#        d[nums[i]] = i
#
#print(two_sums(L, 10))

#sample_dictionary = {0: 10, 1: 20}
#
#sample_dictionary[2] = 30
#print(sample_dictionary)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

#dic4 = dic1 + dic2 + dic3
#
#print(dic4)
#dic4 = {}
#for i in (dic1, dic2, dic3):
#    
#    dic4.update(i)
#
#print(dic4)
#
dic4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
#def check(dic, element):
#    
#    if element in dic:
#        print(element, 'is in the dictionary.')
#    else:
#        print(element, 'is not in the dictionary.')

#print(check(dic4,5))
#check(dic4, 5)
#
#for i, x in dic4.items():
#    print(i, '==>', x)

#num = int(input('Enter a number.'))
#dic = {}
#for i in range(1, num+1):
#    dic[i]= int(i**0.5)
#print(dic)

#a = {}
#
#for i in (dic1, dic2):
#    a.update(i)
#
#print(a)

my_dict = {'data1':100,'data2':-54,'data3':247}

#print(sum(my_dict.values()))
#print(sum(my_dict.values()))
#count = 1
#for i in my_dict:
#    
#    count = count * my_dict[i]
#    
#print(count)

#def two_sums(nums, target):
#    d = {}
#    
#    for i in range(len(nums)):
#        if target - nums[i] in d:
#            print(d)
#            return [d[target-nums[i]],i]
#        d[nums[i]] = i 
#    
#    return -1
#
#two_sums(dic4, 10)

#class Card(object):
#    
#    status = 'This is a card.'
#    
#    def __init__(self, value, suit):
#        self.value = value
#        self.suit = suit
#    
#    def get_value(self):
#        return self.value
#    
#    def get_suit(self):
#        return self.suit
#    
#    def __str__(self):
#        
#        my_card = status + str(self.value) + ' of ' + str(self.suit)
#        return my_card
#    
#my_card = Card(1, 'Snake')
#
#print(my_card)

import matplotlib.pyplot as plt
from random import choice

#plt.rc('figure', figsize = (10,4))
#
#values = list(range(0,50,5))
#
##print(values)
#
##plt.plot(values)
##plt.show()
#
#x_axis = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
#
#plt.plot(x_axis, values)
#plt.xlim(0, 1.0)
#plt.ylim(0, 50)
#plt.title('Our plot')
#plt.xlabel('This is the horizontal axis')
#plt.ylabel('This is the vertical axis')
#plt.show()

step_option = [1, -1]
step_choice = choice(step_option)
print(step_choice)






































    
    















































 
        