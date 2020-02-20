#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:43:07 2020

@author: Sena-2
"""

#print(dir(stack))

#stack = []
#
#stack.append(4)
#stack.append(7)
#
#print(stack.pop())
#
#import calendar 
#
#y = int(input('Enter the year you want to see: '))
#m = int(input('Enter the month you want to see: '))
#
#print(calendar.month(y, m))
#
#from datetime import date
#
#f_days = date(2014, 7, 2)
#d_days = date(2014, 7, 11)
#delta = d_days - f_days
#
#print(delta.days)

#def difference(n, b = 17):
#    
#    if n > b:
#        return n - b
#    else:
#        return 2 * (abs(n-b))
#    
#    
#b = difference(12)
#print(b)
    
#x = difference(34)
#
#print(x)
#
#y = difference(9)
#
#print(y)

#def histogram(liste):
#    
#    for n in liste:
#        
#        output = ''
#        times = n
#        while times > 0:
#            output += '*'
#            times = times - 1
#        print(output)
#    
#x = histogram([3,6,2,9])

#def histogram(liste):
#    
#    for n in liste:
#        output = ''
#        times = n
#        while times > 0:
#            output += '*'
#            times = times - 1
#        print(output)
#        
#x = histogram([4,2,7,9])
#
#print(x)

#def histogram(liste):
#    
#    for n in liste:
#        output = ''
#        times = n
#        
#        while times > 0:
#            output += '*'
#            times -= 1
#        print(output)
#        
#a = [4,3,8,1]        
#histogram(a)

#def histogram(liste):
#    
#    for n in liste:
#        output = ''
#        times = n 
#        
#        while times > 0:
#            output += '*'
#            times -= 1
#        
#        print(output)
#        
##histogram([4,8,3,0,11])
#        
#a = [1,2,3,4,5,6,7,8,9,10,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#
#histogram(a)

#def conca(liste1):
#    output = ''
#    
#    for i in liste1:
#        output += str(i) + ' '
#    print(output)
#    
#liste = [4,8,'elements', 'kayseri']
#conca(liste) 

#numbers = [    
#    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#    958,743, 527
#    ]
#
#def even(liste):
#    
#    even_list = []
#    
#    for i in liste:
#        if i == 237:
#            print(i)
#            break
#        elif i % 2 == 0:
#            even_list.append(i)
#    print(even_list)
#
#x = even(numbers)

#color_list_1 = set(["White", "Black", "Red"])
#color_list_2 = set(["Red", "Green"])
#
#x = color_list_1.difference(color_list_2)
#
#print(x)

#def area_triangle(height, base):
#    
#    return 0.5 * (height * base)
#
#area = area_triangle(20, 5)
#
#print(area)

#def gcd(a, b):
#    
#    a_list = []
#    b_list = []
#    c_list = []
#    
#    for i in range(1, a):
#        if a % i == 0:
#            a_list.append(i)
#    
#    for x in range(1, b):
#        if b % x == 0:
#            b_list.append(x)
#    
#    for i in a_list:
#        if i in b_list:
#            if i not in c_list:
#                c_list.append(i)
#    return c_list[-1]
#
#x = gcd(34, 10)
#
#print(x)

#def three_sum(a,b,c):
#    
#    if a == b == c:
#        return 0
#    else:
#        return a+b+c
#    
#a = three_sum(3,6,2)
##print(a)
#
#b = three_sum(4,4,4)
#print(b)
#
#def weird_func(a,b):
#    
#    if a == b or abs(a+b) == 5 or a-b ==5:
#        return True
#    else:
#        return False

#x = weird_func(4,7)
#
#print(x)
        
#y = weird_func(5, 5)
#
#print(y)
        
#z = weird_func(7, 3)
#
#print(z)

#def personal_details():
#    
#    name, age = 'Mehmet', 28
#    adres = 'Ankara, Turkey'
#    
#    print('Name\t: {}\nAge\t: {}\nAdres\t: {}'.format(name, age, adres))
#
#x = personal_details()

#def interest_rate(amount, rate, year):
#    
#    total = amount + (((amount/100)*rate)* year)
#    
#    return ('The amount you will pay for {} in {} years is \
#{}'.format(amount, year, total))
#
#result = interest_rate(1000, 3.5, 7)
#
#print(result)

#import os.path
#
#print(os.path.isfile('mehmet.txt'))
#import os.path

#print(os.path.isfile('mehmet.txt'))

#print(os.path.isfile('clear.txt'))

#import os
#import platform
#
#
#print(platform.system())
#print(platform.release())
#print(os.name)

#import site
#
#print(site.getsitepackages())

#b = set()
#
#c = set([1,6,3,9,10])
#d = []
#
#for i in c:
#    if i % 2 == 0:
#        d.append(i)
#
#print(d)

#for i in range(0, 20, 3):
#    print(i)
#    if i % 4 == 1:
#        print(i)

#'''
#Question 1
#Write code that asks the user to input a number between 1 and 5 inclusive.
#The code will take the integer value and print out the string value. So for
#example if the user inputs 2 the code will print two. Reject any input that
#is not a number in that range
#'''    
#
#user_input = int(input('Lutfen 1 ile 3 arasinda bir sayi gir: '))
#
#if user_input == 0:
#    print('sifir')
#elif user_input == 1:
#    print('bir')
#elif user_input == 2:
#    print('iki')
#elif user_input == 3:
#    print('uc')
#else:
#    print('Hatali komut. Programi tekrar calistirin.')
#user_input = int(input('Lutfen kac tane fib numarasi istediginizi girin'))
#a, b = 0, 1
#fib = []
#
#for i in range(1,user_input+1):
#    a, b = b, a+b
#    fib.append(a)
#    
#print(fib)

#print("I will now count my chickens: ")

#"""
#Birazdan yapacağımız egzersizler yorum içerisinde açıklanacaktır. 
#
#"""
#
#cars = 100
#x = 'tane' 
#
#print('Bizim garajımızda', cars, 'tane arabamiz var')
#print(f'Bizim garajımızda {cars} tane arabamiz var')
#print('Bizim garajımızda {} {} arabamiz var'.format(cars, x))

#v = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#print(v)

#v = "Jan, Feb, Mar, Apr, May, Jun, Jul, Aug"
#b = "aralik, ocak, subat, mart, nisan"
#print("Jan","Feb", "Aug", sep='\t')

#password = input('Lutfen sifre giriniz. Bilmiyorsaniz exit yazin: ==>')
#
#print(password)
#
#while password != 'exit' or password != 8351:
#    
#    if password == 'exit':
#        print('programdan cikiliyor...')
#        break
#
#    elif password == 8351:
#        print('dogru sifre.')
#        break
#    else:
#        password = input('Lutfen sifre giriniz. Bilmiyorsaniz exit yazin: ==>')

#a = 1
#while a == 1:
#    print("bilgisayar çıldırdı!")
#
#tr_harfler = 'abcdserdfa'
#
##print(len(tr_harfler))
#
##print(dir(len))
#a = 1
#
#while a < len(tr_harfler):
#    print(tr_harfler[a], sep="\n")

#print('hello')
        
#
#def sapma():
#    return i % 26

#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
#for i in a:
#    if i % 2 == 0:
#        print(i, end = '/')
#
#print('How are', '\n\tyou', 'today? ')
#
#print('one', 'two')
#
#a = 'string'
#print(a)
#
#a = 2
#b = 3
#
#print(a+b)
#
#yusuf_mehmet = 'yusuf is a friend of mehmet'
#
#yusuf mehmet

#a, b = '4', '6'
#
#c = a + b
#
#print(c)

#a = 'yusuf'
#b = 'merve'
#c = 6

#c = a + ' \n' +b
#
#print(c)

#print(type(a))
#print(type(c))
#isim = input('Isminiz:  ')
#yas = int(input('Yasinizi giriniz:  '))
#yil = 2020
#dogum_tarihi = yil - yas
#
#print(isim,'Oncelikle programimiza hosgeldin. \', dogum_tarihi+100, \'
#yilinda 100 yasina gireceksiniz. Cunku', dogum_tarihi,
#'yilinda dogdun. ')

#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
#for i in a:
#    if i % 9 == 0:
#        print(i)
#    
#    elif i % 3 == 0:
#        print(i, end= ',')


#string = 'ankara'

#birinci_harf = string[0]
#
#print(birinci_harf)

#ikinci_harf = string[1]
#
#print(ikinci_harf)
#
#ank = string[0:3]
#print(ank)

#print(string[::-1])

#user_input = input('Enter your name to check whether it is a palyndrome:  ')
#user_input = user_input.lower()
#rvs = user_input[::-1]
#
#
#
#if user_input == rvs:
#    print('This is palyndrome')
#else:
#    print('This is not a palyndrome')

#print(string[3:]+ string[0:3])

string = 'ankara'
#
#for i in string:
#    print(i.upper(), end = '')

alphabet = 'abcçdefgğhıijklmnoöpqrstuüxvyz'
#print(len(alphabet))

#def bir_sonraki():
#    
#    string = input('Enter a name:  ')
#
#    for i in string:
#        index_num = alphabet.find(i)
#        output = ''
#        output += alphabet[index_num+1]
#        print(output.upper(), end= '')
#    print('\n',string.upper())
#    
#bir_sonraki()

#welcome_statement = 'HESAP MAKİNASINA HOŞ GELDİNİZ!'
#islem = """ 
#Toplama için (1) 
#Çıkarma için (2) """
#
#
#print('*'* len(welcome_statement))
#print(welcome_statement)
#print('*'* len(welcome_statement))
#print()
#print(islem)
#user_input = int(input('Lütfen yapmak istediğiniz işlem için numara giriniz...' ))
#
#if user_input == 1:
#    user_input1 = int(input('Birinci sayıyı giriniz: '))
#    user_input2 = int(input('İkinci sayıyı giriniz: '))
#    print('Sonuç : ',user_input1+user_input2)
#elif user_input == 2:
#    user_input1 = int(input('Birinci sayıyı giriniz: '))
#    user_input2 = int(input('İkinci sayıyı giriniz: '))
#    print('Sonuç : ',user_input1-user_input2)
#else:
#    user_input = int(input('Lütfen yapmak istediğiniz işlem için numara giriniz...' ))


#yildiz = '*'
#for i in range(0, 20, 2):
#    print(yildiz * i)
#
#for i in range(20, 0, -1):
#    print(yildiz * i)

a = [1, 4, 6, 'a', 'b', 'ankara', 'belcika', 4534234]

b = [1, 4, 6, 45, 342, 34]

#print(a[5])

#print(max(b))

#print(max(a))

#c = list()
#
#for i in b:
#    c.append(i ** 2)
#print(c)

#print(c)
#    print(i ** 2)

#import calendar
#
#y = int(input('Lutfen yil giriniz:  '))
#m = int(input('Lutfen ay giriniz: '))
#
#print(calendar.month(y, m))

#import os
#
#print(os.name)
#print(os.__file__)

#import random as r

#from random import randint

#print(r.shuffle(b))

#print(r.randint(1,6))

#d = dict()
#d = {'ankara' : ['baskent', 'soguk', 'memur_kenti'], 'istanbul' : 'ticari_kent'}
#
##print(type(d))
#
##d[ankara] = 'baskent'
##
##print(d)
#
##print(d['ankara'])
#
##print(d.get('istanbul'))
#
#d['Malatya'] = ['dogunun parisi', 'kayisisi meshur', 'eti de super']
#
##print(d)
#
##print(d.get('Malatya'))
#
#m = d.get('Malatya')
#
#print(m)

#for i in range(10):
#    if i % 2 == 0:
#        print(i, end= ',')

#a = [i for i in range(10) if i % 2 == 0]
#print(a)

#a = 'yusuf'
#b = 'abuziddin'
#
##print(len(a))
#
#def change(string):
##    
#    return string[-1]+string[1:(len(string)-1)]+string[0]
##
##b = change(a)
##print(b)
#
#print(change(b))

#f = open('yusuf.txt', 'w')
#
#f.write('Merhaba. Ben ilk defa dosya aciyorum.')
#f.close()
#
#with open('yusuf.txt', 'a') as f:
#    f.write('\nBu da ikinci satirimiz')
#    
##import yusuf.txt
##
##print(yusuf.__name__)
#
##with open('yusuf.txt', 'r') as f:
##    x = f.read()
##    print(x)
#    
#with open('yusuf.txt') as f :
#    x = f.read()
#    print(x)

#with open('mehmet.txt') as m:
#    x = m.read()
#    print(x)

def kare(a,b):
    '''
    Iki sayinin karelerinin ciktisini verir.
    
    '''
    print((a ** 2) - (b ** 2))
#
#kare(2, 3)

#def kare

    


    
















        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        