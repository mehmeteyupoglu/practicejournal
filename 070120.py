#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:15:17 2020

@author: Sena-2
"""
#print('-'*40)
intro ="""

Welcome to the Calculator 2.3! You have 6 options:
    
|  Press 1 to do collection             |\n
|  Press 2 to do extraction             |\n
|  Press 3 to do Multiplication         |\n
|  Press 4 to do Division               |\n
|  Press 5 to do Square                 |\n
|  Press 6 to do Square Root            |\n
|  Press 7 to exit                      |\n

"""
    
#print(intro)
#
#print('-'*40)
#    
#while True:
#    user_input = input('Press a number to continue. 7 for exit:  ')
#    if user_input == '7':
#        break
#        print('Take care!')
#    
#    elif user_input == '1':
#        num1 = int(input('Enter the first number:  '))
#        num2 = int(input('Enter the second number:  '))
#        print('Result:', num1+num2)
#    elif user_input == '2':
#        num3 = int(input('Enter the first number:  '))
#        num4 = int(input('Enter the second number:  '))
#        print('Result:', num3-num4)
#    elif user_input == '3':
#        num5= int(input('Enter the first number:  '))
#        num6 = int(input('Enter the second number:  '))
#        print('Result:', num5*num6)
#    elif user_input == '4':
#        num7= int(input('Enter the first number:  '))
#        num8= int(input('Enter the second number:  '))
#        print('Result:', num7/num8)
#    elif user_input == '5':
#        num9= int(input('Enter the number:  '))
#        print('Result:', pow(num9,2))
#    elif user_input == '6':
#        num10= int(input('Enter the number:  '))
#        print('Result:', num10**0.5) 
#    else:
#        print('Please choose one:  ', intro)

#print(*intro, sep = '')

#object2 = 'Mehmet'
#
#for i in range(6):
#    print(object2[i])

#name = input('Enter your name:   ')
#
#for i in range(len(name)):
#    if i == '':
#        continue
#    print('The {}. letter of your name is {}'.format(i+1, name[i]))

ata1 = "Akıllı bizi arayıp sormaz deli bacadan akar!"
ata2 = "Ağa güçlü olunca kul suçlu olur!"
ata3 = "Avcı ne kadar hile bilirse ayı da o kadar yol bilir!"
ata4 = "Lafla pilav pişse deniz kadar yağ benden!"
ata5 = "Zenginin gönlü oluncaya kadar fukaranın canı çıkar!"

#for i in ata1, ata2, ata3, ata4, ata5:
#    print(i[0:-1] + '.')

#print(ata1[0:5])
#print(ata1[:15])
#print(ata1[15:])
#print(ata1[4:16])

#print(ata1[::2])

#for i in reversed(ata1):
#    print(i)

#print(*reversed(ata1), sep = '')
#print(sorted('kitap'))
#
#print(*sorted('kitap'))

#for i in sorted('kitap'):
#    print(i, end='')
#
#fruits = 'Apple'
##print(id(fruits))
##print('a' + fruits[1:])
#
##fruits = 'a' + fruits[1:]
##print(id(fruits))
##print(fruits)
#
#print(fruits[:2]+'PL'+fruits[4:])

#for i in dir(''):
#    if '_' not in i[0]:
#        print(i)

#count = 0
#list2 = []
#
#for i in dir(''):
#    if '_' not in i[0]:
##        count += 1
##print(count)
#        list2.append(i)
#count1 = len(list2)
##print(len(list2), *list2, sep = ',')
#
#print('{} method exist that we want to see!'.format(count1))

#word = 'Mehmet'
#count = 0
#for i in enumerate(word):
#    count += 1
#    print(i,count)

#kardiz = 'memleket'
##print(kardiz.replace('ket', 'KET'))
#
#print(kardiz.replace('e', '', 2))

#mit = 'Masschacusets Institute of Technology'
#
##for i in mit.split():
##    print(i[0], sep = '.')
#    
#b = [i[0] for i in mit.split()]
#
#print(b)

#kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"
#kardiz = kardiz.split(',')
#
#for i in kardiz:
#    print(i, end = '')

#data = input('Please enter a name:   ')
#
#while True:
#    if not data.islower():
#        print('Data cannot contain capital letters.')
#    elif data == 'quit':
#        break
#    else:
#        print('Congrats! You managed to enter data.')

#d1 = "python.ogg"
#d2 = "tkinter.mp3"
#d3 = "pygtk.ogg"
#d4 = "movie.avi"
#d5 = "sarki.mp3"
#d6 = "filanca.ogg"
#d7 = "falanca.mp3"
#d8 = "dosya.avi"
#d9 = "perl.ogg"
#d10 = "c.avi"
#d11 = "c++.mp3"
#
#for i in d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11:
#    if i.endswith('mp3'):
#        print(i)

#metin = """
#> Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından
#> 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python
#> olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını düşünür.
#> Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez.
#> Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi
#> grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır.
#> Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
#> bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır diyebiliriz.
#"""
#
#for i in metin.split():
#    print(i.strip('> '), end = ' ')

#kardiz = "adana"
#for i in range(len(kardiz)):
#    print(kardiz.index("a", i))

#print('{} ve {} iyi bir ikilidir!'.format('Django', 'Python'))

#user_input = input('What is your name:    ')
#print('Hello {} !'.format(user_input))

#departure           = input('Place of departure: ')
#arrival             = input('Destiny: ')
#name_surname        = input('Your name and surname: ')
#number_of_tickets   = input('How many tickets would you like to buy: ')
#
#print('From {} to {}, {} tickets are reserved for {} at 2.30 trip!'.format(departure, 
#      arrival, 
#      number_of_tickets,
#      name_surname))

liste = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6]

for i in liste:
    print('{}\'s class type is {}'.format(i, type(i)))















































    