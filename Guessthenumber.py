import random2 as ran

def getdata():
    return list(int(x) for x in input("Enter your Guessing Number: "))
j=0
comp= list(ran.randint(0,9) for x in range(4))
mod =comp.copy()
user=getdata()
num = ['X','X','X','X']

while True:
    i = 0
    while i<4:
        if comp[i]==user[i]:
            num[i]='C'
            mod[i]='X'
        elif user[i] in mod:
            num[i]='P'
        else:
            num[i]='X'

        i+=1
    if 'P' in num:
        if j>0:
            j=0
        else:
            j+=1
            continue
    print(*user)
    print(*num)
    if all(element == 'C' for element in num):
        break
    else:
        user =getdata()
        mod =comp.copy()
print(" !!!Congradulation , You Win the game !!! \n you did it")
print(*user)

        
    
    
