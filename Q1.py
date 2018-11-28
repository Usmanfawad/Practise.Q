print(u"\u25A0"*28)
print("Time to play a guessing game")
import time
print(u"\u25A0"*20)
time.sleep(2)
print(u"\u25A0"*18)
time.sleep(2)
print(u"\u25A0"*15)
time.sleep(2)
print(u"\u29A0"*10)
import random
x= random.randint(1,100)
guess= int(input("guess a number from 1 to 100: "))
while guess!=x:
    if guess<x:
        print("Too low!")
        guess= int(input("guess a number from 1 to 100: "))
    elif guess>x:
        print("Too hight!")
        guess= int(input("guess a number from 1 to 100: "))
print("You guessed it")

    
    
        
        
    
    


