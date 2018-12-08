print("Mid term exam Question")
print(u"\u25A0"*22)
#FISH BURGER=RS180
import time

fish_burger= 180
notes_bill=[]
print("\n\n")
print(u"\u25A0"*20)
time.sleep(0.5)
print(u"\u25A0"*2,"ABC BURGER LTD",u"\u25A0"*2)
time.sleep(1)
print(u"\u25A0"*20)
time.sleep(0.5)
user_choice= input("Do you want to purchase a fish burger? Y/N:  ")
user_choice.capitalize()
if user_choice=='Y':
    quantity_burger= int(input("Enter the quantity of burgers you want: "))
    total_bill= fish_burger*quantity_burger
    print("Your total amount is: $",total_bill)
    paid_bill= int(input("Enter the amount given:  $"))
    return_bill= paid_bill-total_bill
    x=return_bill
while x!=0:
    if x%5000==0:
        notes_bill.append(5000)
        x-=5000
    elif x%1000==0:
        notes_bill.append(1000)
        x-=1000
    elif x%500==0:
        notes_bill.append(500)
        x-=500
    elif x%100==0:
        notes_bill.append(100)
        x-=100
    elif x%50==0:
        notes_bill.append(50)
        x-=50
    elif x%20==0:
        notes_bill.append(20)
        x-=20
    elif x%10==0:
        notes_bill.append(10)
        x-=10
    elif x%5==0:
        notes_bill.append(5)
        x-=5

print("The total amount returned is $",return_bill,"And in terms of notes is",notes_bill)
            
            
