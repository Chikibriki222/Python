p = input("123")
fd = 0
sd = 0
first = 0
second = 0
temp = 0
pl = int(p.find("+"))
mi = int(p.find("-"))
di = int(p.find("/"))
um = int(p.find("*"))
fs = int(p.find("("))
ss = int(p.find(")"))
test = str(second)
# определяем порядок знаков
if p.rfind("+") > pl:
    first = pl
    second = p.rfind("+")
elif pl > 0:
    second = pl
if p.rfind("-") > mi:
    first = mi
    second = p.rfind("-")
elif mi >= 0 and second < mi:
    temp = second
    second = mi
    first = temp
elif 0 <= mi < second:
    first = mi
if p.rfind("/") > di:
    first = di
    second = p.rfind("/")
elif di >= 0 and second < di:
    temp = second
    second = di
    first = temp
elif 0 <= di < second:
    first = di
if p.rfind("*") > um:
    first = um
    second = p.rfind("*")
elif um >= 0 and second < um:
    temp = second
    second = um
    first = temp
elif 0 <= um < second:
    first = um
# вычисляем со скобками
if fs < first < ss:
    if p[first] == "+":
        fd = (int(p[fs+1:first])) + (int(p[first + 1:ss]))
    elif p[first] == "-":
        fd = (int(p[fs+1:first])) - (int(p[first + 1:ss]))
    elif p[first] == "*":
        fd = (int(p[fs+1:first])) * (int(p[first + 1:ss]))
    elif p[first] == "/":
        fd = (int(p[fs+1:first])) / (int(p[first + 1:ss]))
    if p[second] == "+":
        print(fd + (int(p[second + 1:])))
    elif p[second] == "-":
        print(fd - (int(p[second + 1:])))
    elif p[second] == "*":
        print(fd * (int(p[second + 1:])))
    elif p[second] == "/":
        print(fd / (int(p[second + 1:])))
elif fs < second < ss:
    if p[second] == "+":
        fd = (int(p[fs:second])) + (int(p[second + 1:ss]))
    elif p[second] == "-":
        fd = (int(p[fs:second])) - (int(p[second + 1:ss]))
    elif p[second] == "*":
        fd = (int(p[fs:second])) * (int(p[second + 1:ss]))
    elif p[second] == "/":
        fd = (int(p[fs:second])) / (int(p[second + 1:ss]))
    if p[first] == "+":
        sd = (int(p[:first])) + fd
    elif p[first] == "-":
        sd = (int(p[:first])) - fd
    elif p[first] == "*":
        sd = (int(p[:first])) * fd
    elif p[first] == "/":
        sd = (int(p[:first])) / fd
    print(sd)
# вычисляем без скобок
else:
    if p[second] == "*" or p[second] == "/":
        if p[second] == "*":
            fd = (int(p[first + 1:second]) * int(p[second + 1:]))
        elif p[second] == "/":
            fd = (int(p[first + 1:second]) / int(p[second + 1:]))
        if p[first] == "+":
            sd = (int(p[:first])) + fd
        elif p[first] == "-":
            sd = (int(p[:first])) - fd
        elif p[first] == "*":
            sd = (int(p[:first])) * fd
        elif p[first] == "/":
            sd = (int(p[:first])) / fd
        print(sd)
    if p[first] == "+":
        fd = (int(p[:first])) + (int(p[first + 1:second]))
    elif p[first] == "-":
        fd = (int(p[:first])) - (int(p[first + 1:second]))
    elif p[first] == "*":
        fd = (int(p[:first])) * (int(p[first + 1:second]))
    elif p[first] == "/":
        fd = (int(p[:first])) / (int(p[first + 1:second]))
    if p[second] == "+":
        print(fd + (int(p[second + 1:])))
    elif p[second] == "-":
        print(fd - (int(p[second + 1:])))
    elif p[second] == "*" and sd == 0:
        print(fd * (int(p[second + 1:])))
    elif p[second] == "/" and sd == 0:
        print(fd / (int(p[second + 1:])))
