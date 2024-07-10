class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def mod(self):
        return self.a%self.b
t=1
while t==True:
        print("Menu")
        print("\n 1.addition \n 2. sutraction,\n 3.multiplication \n 4.division \n 5.modulus")
        n=eval(input("enter the choice:"))
        f=int(input("enter a number :"))
        s=int(input("enter a number:"))
        c=calculator(f,s)
        
        if n==1 or n=="addition":
            print("addition of two number:",c.add())
        elif n==2 or n=="subtraction":
            print("addition of two number:",c.sub())
        elif n==3 or n=="multiplication":
            print("addition of two number:",c.mul())
        elif n==4 or n=="division":
            print("addition of two number:",c.div())
        elif n==5 or n=="modulus ":
            print("addition of two number:",c.mod())
        else:
            t=input("do you want to continue ? yes/no")
            if t=="yes":
                t=1
            else:
                t=0
