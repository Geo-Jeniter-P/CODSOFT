import random
print("welcome password generator.")
a=eval(input("enter the length of the  password"))
c=""
for i in range(0,a):
    b=(random.randint(0,1))
    if b==1:
        x="QWERT@YU#I!OP%A&SDFG*HJKLZXCVBNMqwertyuiopasdfghjklmnbvcxz"
        d=random.choice(x)
        c=c+d
    elif b==0:
        d=random.randint(0,9)
        c=c+str(d)
print("generated Password:",c)
