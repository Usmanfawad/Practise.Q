print("Usman Fawad, \n18B-069-CS(A), \nQ-05")
#ONLY OPERATING WHEN DIMENSIONS=5*5
#TO BE CONTINUED
def shape():
    for hor_line in range(6):
        print("*",end=' ')
    for m in range(6):
        if m==0:
            print('')

    for b in range(6):
        m=4
        n=2

        if b>1 and b<3:
            print("* "+ "+ "*m+"*")
        elif b >=3 and b<5:
            print("* + "+" "*n+"  + *")
        elif b==5:
            print("* "+ "+ "*m+"*")
    for h in range(6):
        print("*",end=' ')

'''shape_user= input("Enter your desired shape i.e 's' if square and 'r' if rectangle: ")

if shape_user== 's':
    dim_sq= int(input("Please enter the dimension of Square: "))
    x= dim_sq
    shape(x)
elif shape_user=='S':
    shape_user.lower()
    dim_sq=int(input("Please enter the dimension of Square: "))
    x= dim_sq'''
shape()




