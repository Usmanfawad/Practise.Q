from random import randint
print("Loading!")
import time
for char in range(5):
    print(u"\u25A0"*2,str(char+1),end=' ')
    time.sleep(1)

print("\nWelcome to Rock, Paper, Scissors!")
time.sleep(1)
print("Sit back,relax and please dont break your screen xD")
time.sleep(1)

user_name= input("Please enter your name: ")
user_rounds= int(input("Enter the number of rounds for winning: "))
print(u"\u21A0"*10)
RPS= ['r','p','s']
computer= RPS[randint(0,2)]
comp=0
user=0
aw= 'AWWWWWWWWW'



print("Hello",user_name,"!")


while comp!=user_rounds and user!=user_rounds:
    computer= RPS[randint(0,2)]
    rps= input("\nEnter Rock(r), Paper(p}, or Scissor(s):")
    rps= rps.lower()
    if rps not in RPS:
        print("Chose (r) or (p) or (s) you ***!")
    if computer==RPS[0]and rps=='p':
        print("\nComputer chose Rock! You Win!")
        user+=1
    if computer==RPS[0] and rps=='s':
        print("\nComputer chose Rock! You Lose!")
        for i in aw:
            print(i,end='   ')
            time.sleep(0.5)
        comp+=1
    if computer==RPS[0] and rps=='r':
        print("\nComputer chose Rock! It's a draw!")
    if computer==RPS[1] and rps=='r':
        print("\nComputer chose Paper! You Lose!")
        for i in aw:
            print(i,end='   ')
            time.sleep(0.5)
        comp+=1
    if computer==RPS[1] and rps=='s':
        print("\nComputer chose Paper! You Win!")
        user+=1
    if computer==RPS[1] and rps=='p':
        print("\nComputer chose Paper! Its a Draw!")
    if computer==RPS[2] and rps=='r':
        print("\nComputer chose Scissor! You Win!")
        user+=1
    if computer==RPS[2] and rps=='p':
        print("\nComputer chose Scissor! You Lose!")
        for i in aw:
            print(i,end='   ')
            time.sleep(0.5)
        comp+=1
    if computer==RPS[2] and rps=='s':
        print("\nComputer chose Scissor! Its a Draw!")
print(u"\u25A0"*24)
print(user_name, user, "   ","Computer", comp,u"\u25A0")
print(u"\u25A0"*24)
if  comp>user:
    print("Computer Wins!")
else:
    print("You Win!")
        



    

