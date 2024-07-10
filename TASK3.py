import random
print("Rock vs Scissors vs Paper")
hum=0
com=0
c=['rock','scissors','paper'] 
for i in range(0,5):
    a=input("Rock Paper Scissors:")
    b=random.choice(c)
    print("you pick:",a,"computer pick:",b)
    if a==b:
        print("Both  are same")
    elif a=="rock":
        if b=="scissors" :
            hum+=1
            print("you win")
        else:
            com+=1
            print("computer win")
    elif a=="scissors":
        if b=="paper":
            hum+=1
            print("you win")
        else:
            com+=1
            print("computer win")
    elif a=='paper':
        if  b =='rock':
            hum+=1
            print("you win")
        else:
            com+=1
            print("computer win")
if a>b:
    print("you are final winner")
else:
    print("computer finally wins")
