a=input("input zadachu")
tpl=a.find("+",0)
tmin=a.find("-",0)
tdiv=a.find(":",0)
tdiv2=a.find("/",0)
tum=a.find("*",0)
if(a[tpl] =="+" ):
    print(int(a[0:tpl])+int(a[tpl+1:]))
elif(a[tmin]=="-"):
    print(int(a[0:tmin])-int(a[tpmin+1:]))
elif(a[tum]=="*"):
    print(int(a[0:tum])*int(a[tum+1:]))
elif(a[tdiv]==":"):
    if(int(a[tdiv+1:])==0):
        print("you can't divide by zero!")
    else:
        print(int(a[0:tdiv])/int(a[tdiv+1:]))
elif(a[tdiv2]=="/"):
    if(int(a[tdiv2+1:])==0):
        print("you can't divide by zero!")
    else:
        print(int(a[0:tdiv2])/int(a[tdiv2+1:]))
