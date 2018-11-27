print("Usman Fawad, \n18B-069-CS(A), \nQ-05")

def square(lenght):
    for hor_line in range(lenght):
        print("*",end=' ')
    for ver_line in range(lenght):
        if ver_line==0:
            print('')
        elif ver_line>0 and ver_line<lenght-1:
            print("*"," "*(lenght),"*")
    print("* "*lenght)

def rectangle(lenght,breadth):
    for hor_line in range(breadth):
        print("*",end=' ')
    for ver_line in range(lenght):
        if ver_line==0:
            print('')
        elif ver_line>0 and ver_line<lenght-1:
            if breadth>lenght:
                print("*"," "*(breadth+1),"*")
            elif breadth<lenght:
                print("*"," "*(breadth),"*")
    print("* "*breadth)
        

x=int(input("Enter dimensions of square: "))
print(u"\u25A0 "*x)
square(x)
x1=int(input("Enter lenght of rectangle:  "))
x2=int(input("Enter breadth of rectangle: "))
print(u"\u25A0 "*x2)
rectangle(x1,x2)




