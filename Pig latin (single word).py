import time
print("Loading!")
for bbb in range(5):
    print(u"\u25A0",str(bbb+1),end='')
    time.sleep(1)
print("\nWelcome to pig latin translator!")
print(u"\u25A0"*33)
#phase1
def word(y):
    for char in y:
        if char not in 'aeiouAEIOU':
            print(char)
        else:
            break
lstV=[]
lstC=[]
#Phase2
def word2(x):
    ccc= 'ay'
    y=0
    for char in x:
        if char not in 'aeiouAEIOU':
            lstC.append(char)
            y=y+1
        else:
            break
    join1 = ''.join(map(str, lstC))
    for char in x[y:]:
        lstV.append(char)
    join2 = ''.join(map(str, lstV))
    print(join2+join1+ccc)
                    
q= input("\nEnter word: ")
z= input("\nEnter word: ")
word(q)
word2(z)

    

            
      
    
    
        

                
        
            

   

        


    

