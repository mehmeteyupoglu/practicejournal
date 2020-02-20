#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:41:16 2020

@author: Sena-2
"""

#def prime(num):
#    
#    if num == 1:
#        prime = False
#    elif num == 2:
#        prime = True
#    
#    else:
#        prime = True
#        for i in range(2, (num//2)+1):
#            if num % i == 0:
#                prime = False
#                break
#    return prime
#
#print(prime(34))
#print(prime(17))

#def prime(num):
#    
#    if num == 1:
#        prime = False
#    elif num == 2:
#        prime = True
#    else:
#        prime = True
#        
#        for i in range(2, int(num/2)+1):
#            if num % i == 0:
#                prime = False
#                break
#            
#    return prime
#print(prime(34))
#print(prime(13))
#print(prime(92))
#print(prime(27))

#import random
#
#def compare_numbers(num, user_guess):
#    
#    cowbull = [0,0]
#    
#    for i in range(len(num)):
#        if num[i] == user_guess[i]:
#            cowbull[0] += 1
#        else:
#            cowbull[1] += 1
#    return cowbull
#
#if __name__ == '__main__':
#    
#    playing = True
#    guesses = 0
#    num = str(random.randint(1000, 9999+1))
#    
#    while playing:
#        
#        user_guess = input('Give me your best guess: ')
#        
#        if user_guess == 'exit':
#            break
#        elif len(user_guess) != 4:
#            user_guess = input('Try a 4 digit number: ')
#        
#        cowbullcount = compare_numbers(num, user_guess)
#        print(cowbullcount)
#        guesses += 1
#
#    print('You have {} cows and {} bulls. '.format(cowbullcount[0], cowbullcount[1]))
#    
#    if cowbullcount[0] == 4:
#        playing = False
#        print('You win. It took you {} guesses.'.format(guesses))
#    else:
#        print('Your guess is not quite right. Please try again. ')

#import random 
#
#def compare_numbers(number, user_guess):
#    
#    cowbull = [0,0]
#    
#    while number.isdigit and user_guess.isdigit:
#    
#        for i in len(number):
#            if number[i] == user_guess[i]:
#                cowbull[0] += 1
#            else:
#                cowbull[1] += 1
#        return cowbull 
#
#if __name__ == '__main__':
#
#    playing = True
#    number = str(random.randint(1000, 9999))
#    guesses = 0
#    
#    while playing:
#        
#        user_guess = input('Give me your best guess: ')
#        
#        if user_guess == 'exit':
#            break
#        
#        elif len(user_guess) != 4:
#            user_guess = input('You have to input a 4-digit number. ')
#        
#        elif not user_guess.isdigit:
#            user_guess = input('You have to input a 4-digit number. ')
#    
#        cowbullcount = compare_numbers(number, user_guess)
#        guesses += 1
#        
#        print('You have {} cows and {} bulls.'.format(cowbullcount[0], cowbullcount[1]))
#        
#        if cowbullcount[0] == 4:
#            print('You won. It took you {} guesses.'.format(guesses))
#        else:
#            print("Your guess isn't quite right. Try again")

#import numpy.random
#
#get_number = numpy.random.randint(1000, 9999)
#num_str = str(get_number)
#c_b = [0,0]
#
#while c_b[0] < 4:
#    guess = str(input('Enter a 4-digit guess. '))
#    
#    if int(guess) < 1000 and int(guess) > 9999:
#        print('This is not a 4-digit number. ')
#        
#    else:
#        for i in range(4):
#            if num_str[i] == guess[i]:
#                c_b[0] += 1
#    
#        for j in range(4):
#            if guess[j] in num_str:
#                c_b[1] += 1
#        print('You have {} cows and {} bulls. '.format(c_b[0], c_b[1]))

#import random
#
#Minimum = 0
#Maximum = 100
#Number = random.randint(Minimum, Maximum)
#Try = 0
#Running = True
#Answer = None
#
#while Running:
#    
#    print('Is it {}'.format(Number))
#    Answer = input()
#    if 'no' in Answer.lower() and 'lower' in Answer.lower():
#        Number -= random.randint(1, 4)
#    
#    elif 'no' in Answer.lower() and 'higher' in Answer.lower():
#        Number += random.randint(1,4)
#    
#    elif Answer.lower() == 'no':
#        print('Higher or lower?')
#        Answer = input()
#        if Answer.lower() == 'lower':
#            Number -= random.randint(1,4)
#        elif Answer.lower() == 'higher': 
#            Number += random.randint(1,4)
#    elif Answer.lower() == 'yes': 
#        Running = False
#        if Try < 2:
#            print('Yes. It took me {} tries. '.format(Try))
#        elif Try > 2 and Try < 10:
#            print('That is not bad for a robot.')
#        else:
#            print('It is so bad. ')
#    Try += 1

#import random 
#
#Minimum = 0
#Maximum = 100
#Number = random.randint(Minimum, Maximum)
#Try = 0
#Running = True
#Answer = None
#
#while Running:
#    
#    print('Is it {}'.format(Number))
#    Answer = input()
#    if 'no' in Answer.lower() and 'lower' in Answer.lower():
#        Number += random.randint(1,6)
#    
#    elif 'no' in Answer.lower() and 'higher' in Answer.lower():
#        Number -= random.randint(1, 6)
#    
#    elif Answer.lower() == 'no': 
#        print('Higher or lower?')
#        Answer = input()
#        
#        if Answer.lower() == 'lower':
#            Number -= random.randint(1,6)
#        
#        elif Answer.lower() == 'higher':
#            Number += random.randint(1,6)
#        
#    elif Answer.lower() == 'yes':
#        Running = False
#        
#        if Try < 2:
#            print('It is a great performance for a robot')
#        
#        elif Try > 2 and Try < 10:
#            print('It is not bad. ')
#        
#        else:
#            print('Shame on you. It took you {} times to find it. '.format(Try))
#    
#    Try += 1

#import random
#
#minimum = 0
#maximum = 100
#number = random.randint(minimum, maximum)
#running = True
#answer = None
#Try = 0
#
#while running:
#    
#    print('Is it {}\n'.format(number))
#    answer = input()
#    
#    if 'no' in answer.lower() and 'lower' in answer.lower():
#        number -= random.randint(1,4)
#    
#    elif 'no' in answer.lower() and 'higher' in answer.lower():
#        number += random.randint(1,4)
#    
#    elif answer.lower() == 'no':  
#        print('Higher or lower?\n')
#        
#        if answer.lower() == 'higher':
#            number += random.randint(1,4)
#        elif answer.lower() == 'lower':
#            number -= random.randint(1,4)
#
#    elif answer.lower() == 'yes':
#        running = False
#        
#        if Try < 2:
#            print('That is a nice performance for a robot. Congrats...')
#        
#        elif Try <10 and Try > 2:
#            print('Not bad')
#        
#        else:
#            print('Shame on you. It took you {} times to find it'.format(Try))
#        
#    Try += 1
#
#print('Thanks for the game')

#import random
#
## Awroken
#
#MINIMUM = 0
#MAXIMUM = 100
#NUMBER = random.randint(MINIMUM, MAXIMUM)
#TRY = 0
#RUNNING = True
#ANSWER = None
#
#while RUNNING:
#    print "Is it %s?" % str(NUMBER)
#    ANSWER = raw_input()
#    if "no" in ANSWER.lower() and "lower" in ANSWER.lower():
#        NUMBER -= random.randint(1, 4)
#    elif "no" in ANSWER.lower() and "higher" in ANSWER.lower():
#        NUMBER += random.randint(1, 4)
#    elif ANSWER.lower() == "no":
#        print "Higher or lower?"
#        ANSWER = raw_input()
#        if ANSWER.lower() == "higher":
#            NUMBER += random.randint(1, 4)
#        elif ANSWER.lower() == "lower":
#            NUMBER -= random.randint(1, 4)
#    elif ANSWER.lower() == "yes":
#        if TRY < 2:
#            print "Yes! It only took me %s try!" % str(TRY)
#        elif TRY < 2 and TRY < 10:
#            print "Pretty well for a robot, %s tries." % str(TRY)
#        else:
#            print "That's so bad, %s tries." % str(TRY)
#        RUNNING = False
#    TRY += 1
#    
#print "Thanks for the game!"
    
#import random
#
#minimum = 0
#maximum = 100
#number = random.randint(minimum, maximum)
#answer = None
#running = True
#Try= 0
#
#while running:
#    
#    answer = input('Is it {}'.format(number))
#    
#    if 'no' in answer.lower() and 'lower' in answer.lower():
#        number -= random.randint(1,4)
#    elif 'no' in answer.lower() and 'higher' in answer.lower():
#        number += random.randint(1,4)
#    
#    elif 'no' in answer.lower():
#        answer = input('Higher or lower?')
#        
#        if answer == 'higher':
#            number += random.randint(1,4)
#        elif answer == 'lower':
#            number -= random.randint(1,4)
#    
#    elif 'yes' in answer.lower():
#        running = False
#        
#        if Try < 2:
#            print('Perfect. It took you only {} times to find the number'.format(Try))
#        elif Try > 2 and Try < 10:
#            print('It is not bad')
#        else:
#            print('That is so bad')
#        
#    Try += 1
#
#print('Thanks for the game')
#
#import random
#maximum = 100
#minimum = 0
#number = random.randint(minimum, maximum)
#running = True
#answer = None
#Try = 0
#
#while running:
#    
#    answer = input('Is it {}\n==>'.format(number))
#    
#    if 'no' in answer.lower() and 'higher' in answer.lower():
#        number += random.randint(1,4)
#    elif 'no' in answer.lower() and 'lower' in answer.lower():
#        number -= random.randint(1,4)
#    
#    elif answer.lower() == 'no': 
#        answer = input('Higher or lower?\n==>')
#        if answer.lower() == 'higher':
#            number += random.randint(1,4)
#        elif answer.lower() == 'lower':
#            number -= random.randint(1,4)
#    
#    elif answer.lower() == 'yes':
#        running = False
#        
#        if Try < 3:
#            print('You win. It took you only {} times.'.format(Try))
#        elif Try > 2 and Try < 10:
#            print('That is not bad. It took you {} times to find the number.'.format(Try))
#        
#        else:
#            print('It took you {} times. It is really bad for a robot...'.format(Try))
##    
#    Try += 1

#import requests
#from bs4 import BeautifulSoup
#
#base_url = 'http://www.nytimes.com'
#r = requests.get(base_url)
#soup = BeautifulSoup(r.text, 'lxml')
#
#for story_heading in soup.find_all(class_='story-heading'):
#    if story_heading.a:
#        print(story_heading.a.text.replace('\n', '').strip())
#    else:
#        print(story_heading.contents[0].strip())

#import random
#
#s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#passlen = int(input('Enter the lenght of your password:  '))
#password = ''.join(random.sample(s, passlen))
#
#print('Your password is:  {}'.format(password))

#import random
#
#s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#passlen = int(input('Enter the lenght of your password:  '))
#password = ''.join(random.sample(s, passlen))
#
#print('Your password:  {}'.format(password))

#def drawboard(number):
#    
#    number = int(number)
#    i = 0
#    ho = ' ---'
#    ve = '|   '
#    ho = ho * number
#    ve = ve * (number + 1)
#    
#    while i < (number+1):
#        print(ho) 
#        if i != number:
#            print(ve)
#        i += 1
#
#drawboard(5)

#def drawboard(number):
#    number = int(number)
#    i = 0
#    ho = ' ---'
#    ve = '|   '
#    ho = ho * (number)
#    ve = ve * (number+1)
#    
#    while i < (number+1):
#        print(ho)
#        if i != number:
#            print(ve)
#        i += 1
#
#drawboard(7)

#def drawboard(num):
#    
#    num = int(num)
#    i = 0
#    ho = ' ---'
#    ve = '|   '
#    ho = ho * (num)
#    ve = ve * (num + 1)
#    
#    while i < (num + 1):
#        print(ho)
#        if i < num:
#            print(ve)
#        i += 1
#        
#drawboard(5)

#def drawboard(num):
#    num = int(num)
#    i = 0
#    ho = ' ---'
#    ve = '|   '
#    ho = ho * num
#    ve = ve * (num+1)
#    
#    while i < (num+1):
#        print(ho)
#        if i != num:
#            print(ve)
#        i += 1
#drawboard(3)
            
    
    


    
        
        
    
        
            
        
    
