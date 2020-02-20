#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 09:00:39 2020

@author: Sena-2
"""
#
#quit()
#import sys
#sys.exit

#'Mehmet_eyupoglu_2'
#
#len('Mehmet_eyupoglu_2')
#
#print(type(len('Mehmet_Eyupoglu_2')))
#
#import keyword
#print(len(keyword.kwlist))

#calisma_gun = 22
#gidis = 1.5 
#donus = 1.4 
#aylik_yol_masr = (gidis+donus)*calisma_gun
#
#print(aylik_yol_masr)
#
#3 ** 3
#
#ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31
#nisan = haziran = eylül = kasım = 30
#şubat = 28
#
#print(mayıs)

#print('Mehmet', 'Eyupoglu', 'Kayseri')

#print('Mehmet', 'Eyupoglu', sep= '-')

#print('bir', 'iki', 'üç', 'dört', 'ondört', sep = ' mumdur. ' )
#dosya = open('dosya.txt', 'w')
#print('Bunu dosyaya yaz', file = dosya)
#
#import os
#print(os.getcwd())

#print(*'Linux', sep = '.')
#print(*'Galatasaray')

#print(len(range(1,100)))
#
#print('\'Ahmet, \"I am going to Adana\", dedi.\'')
#print('Ahmet said he will come only after \a')

#print("\a" * 10)
#
#print("Ahmet said he'll be going to the us")

#day = 22
#commuting1 = 1.5
#commuting2 = 1.4
#
#cost = day * (commuting1+commuting2)
#
#print('MONTHLY COST OF TRAVELLING')
#print(' ')
#print('-'*40)
#print('Day at Work\t\t\t:', day)
#print('The cost of arriving at work\t:', commuting1)
#print('The cost of turning back\t:', commuting2)
#print('-'*40)
#
#print('The monthly travel cost\t\t:', cost)

#isim = "Fırat"
#soyisim = "Özgül"
#işsis = "Ubuntu"
#şehir = "İstanbul"
#
#
#print("isim             : ", isim, "\n",
#      "soyisim          : ", soyisim, "\n",
#      "işletim sistemi  : ", işsis, "\n",
#      "şehir            : ", şehir, "\n",
#      sep="")

#print(len(str(123456789)))

#Her bir ayın kaç çektiğini aşağıda tanımlıyoruz.
#ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31
#nisan = haziran = eylül = kasım = 30
#şubat = 28
#
##Doğalgazın vergiler dahil m3 fiyatı
#birimFiyat = 0.79
#
##Kullanıcı ayda ne kadar doğalgaz tüketmiş?
#aylıksarfiyat = input('Aylık doğalgaz sarfiyatınızı giriniz: ')
#
##Kullanıcı hangi aya ait faturasını öğrenmek istiyor
#dönem = input('Lütfen hangi döneme ait borcunuzu öğrenmek \
#istediğinizi giriniz:  ')
#
#ay = eval(dönem)
#
#günlükSarfiyat = int(aylıksarfiyat) / ay
#
#fatura = birimFiyat * günlükSarfiyat * ay
#
#print("günlük sarfiyatınız: \t", günlükSarfiyat, " metreküp\n",
#"tahmini fatura tutarı: \t", fatura, " TL", sep="")

#d1 = """
#Python'da ekrana çıktı verebilmek için print() adlı bir
#fonksiyondan yararlanıyoruz. Bu fonksiyonu şöyle kullanabilirsiniz:
#>>> print("Merhaba Dünya")
#Şimdi de aynı kodu siz yazın!
#>>> """
#girdi = input(d1)
#exec(girdi)
#
#d2 = """
#Gördüğünüz gibi print() fonksiyonu, kendisine
#parametre olarak verilen değerleri ekrana basıyor.
#Böylece ilk dersimizi tamamlamış olduk. Şimdi bir
#sonraki dersimize geçebiliriz."""
#print(d2)
#
#num = int(input('Enter a number:   '))
#div = int(input('Enter another number:   '))
#
#scheme = '{} divides {}'.format(div, num)
#
#if num % div == 0:
#    print(scheme, 'evenly!')
#else:
#    print(scheme, 'not evenly')
#
#print(round(3.7))


#print(round(2.65, 1))
#
#print(round(3.453234, 2))

#user_name = input('Enter a user name:    ')
#if bool(user_name) == False:
#    print('A user name must be set')
#else:
#    print('Thanks!')

#while True:
#    question = input('How are you today?    ')
#    if question == 'q':
#        break 

#count = 0
#
#while count < 5:
#    user_input = input('How are you today? Put \'q\'to quit:    ')
#    count += 1
#    if user_input == 'q':
#        break
#print('It took you', count, 'times!')

#sayılar = "123456789"
#for i in sayılar:
#    if int(i) > 3:
#        print(i)

#while True:
#    password = input('Enter a password:   ')
#    
#    if not password:
#        print('Password cannot be blank')
#    elif len(password) > 8 or len(password) < 3:
#        print('Password should be between 3 and 8 characters')
#    else:
#        print('Your password is', password)
#        break


#izinli_karakterler = "0123456789+-/*= "
#
#print("""
#Basit bir hesap makinesi uygulaması.
#İşleçler:
#+ toplama
#- çıkarma
#* çarpma
#/ bölme
#Yapmak istediğiniz işlemi yazıp ENTER
#tuşuna basın. (Örneğin 23 ve 46 sayılarını
#çarpmak için 23 * 46 yazdıktan sonra
#ENTER tuşuna basın.)
#""")
#
##while True:
##    data = input('What do you want to do:   ')
##    if data == 'q':
##        print('Quiting...')
##        break
##    for s in data:
##        if s not in izinli_karakterler:
##            print('What are you after:   ')
##            quit()
##    count = eval(data)
##    
##    print(data)
#
#
#while True:
#    veri = input("İşleminiz: ")
#    if veri == "q":
#        print("çıkılıyor...")
#        break
#    for s in veri:
#        if s not in izinli_karakterler:
#            print("Neyin peşindesin?!")
#            quit()
#    hesap = eval(veri)
#    print(hesap)

#for i in range(10,1, -1):
#    print(i)

#while True:
#     num = int(input('Please enter a number between 1 and 10:   '))
#     
#     if num == 0:
#         break
#     elif num < 0:
#         pass
#     else:
#         print(num)
#     

#while True:
#    num = input('Enter a number:  ')
#    
#    if num == 'cancel':
#        break
#    if len(num) <= 3:
#        continue
#    
#    print('You can only enter numbers less than 3 figures')

#ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
#ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
#fark = ''
#
#for i in ilk_metin:
#    if i in ikinci_metin and i not in fark:
#        fark += i
#
#print(fark)
#
#metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
#tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
#isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
#yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
#adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
#Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
#gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
#da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
#edilmesi neredeyse bir gelenek halini almıştır."""
#
#
#user_input = input('Enter the letter you want to check:   ')
#metin = metin.lower()
#list1 = []
#
#for i in metin:
#    if user_input == i:
#        list1 += i
#print(len(list1))    

#file = open('For Loops Practice.py', encoding='utf-8')
#letter = input('Please enter a letter.')
#mutual = ''
#for i in file:
#    if letter == i:
#        mutual += i
#print(len(mutual))
#       
#file.close() 

print(input("""Welcome to the Calculator 2.3! You have 6 options:
    Press 1 to do +, 
    Press 2 to do -,
    Press 3 to do x, 
    Press 4 to do /, 
    Press 5 to do **, 
    Press 5 to do **0.5, ))
    


























































    











































