#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:32:36 2020

@author: Sena-2
"""

#num = 1
#
#while num < 5:
#    print('Looping...')
#    num += 1

#dosya = open('mehmet.txt')
#
#result = dosya.read()
#
#print(result)

#with open('mehmet.txt', 'w') as dosya_1:
#    dosya_1.writelines('This is the second line')
#    dosya_1.writelines('This is the third line')
#
#with open('mehmet.txt') as dosya_2:
#    result = dosya_2.readline()
#    result2 = dosya_2.readline()
#    result3 = dosya_2.readlines()

#print(result)
#print(result2)
    
#print(result3)
    
#with open('mehmet.txt') as file1:
#    result = file1.readlines()
#    result2 = file1.read()
#
#print(result, end = '')
#print(result2)

#with open('mehmet2.txt', 'w') as dosya:
#    dosya.write('Hello. This is Mehmet.')
#    dosya.write('\nMy phone number is :\t +905531731991.\nMy adress is:\tAnkara\
#/Turkey')

#import os 
#dir(os)
#
#print(os.name)
#print(os.uname)

#from os import name
#print(name)

#import sys
#path_1 = sys.path
#
#print(path_1)

#class Employee:
#    feature = []
#    title = 'employee'
#    
#print(Employee.feature)
#print(Employee.title) 
#
#import tkinter as tk
#
#window = tk.Tk()
#
#button = tk.Button(text = 'Düğme') 
#label = tk.Label(text = 'etiket')
#
#print(button.pack())
#print(label.pack())

#def write_slogan():
#    print("Tkinter is easy to use!")
#
#root = tk.Tk()
#frame = tk.Frame(root)
#frame.pack()
#
#button = tk.Button(frame, 
#                   text="Çık", 
#                   command=quit)
#button.pack(side=tk.CENTER)
#slogan = tk.Button(frame,
#                   text="Lütfen bekleyiniz...",
#                   command=quit)
#slogan.pack(side=tk.LEFT)
#
#root.mainloop()

import tkinter as tk

interface = tk.Tk()

def cikis():
    
    etiket['text'] = 'Hoşçakal Grafik Arayüz' 
    dügme['text'] = 'Lütfen bekleyin...'
    interface.after(2000, interface.destroy)
    
etiket = tk.Label(text = 'Merhaba Grafik Arayüz')
etiket.pack()

dügme = tk.Button(text = 'Çık', command = cikis)
dügme.pack()

interface.protocol('WM_DELETE_WINDOW',cikis)

interface.mainloop()






























    