a=int(input("first number"))
c=input("input action")
b=int(input("second number"))
if(c =="+" ):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    print(a*b)
elif(c==":" or "/"):
    if(b==0):
        print("you can't divide by zero!")
    else:
        print(a/b)

