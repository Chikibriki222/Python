x = open("file.txt")
strok = 0
zn = 0
zap = 0
voskl = 0
tire = 0
tochka = 0
zn2 = [',', '!', '.', '-']

for line in x.readlines(): # readlines() - идёт по строкам
    strok += 1
    for i in line:
        if i == ',':
            zn += 1
            zap += 1
        elif i == '!':
            zn += 1
            voskl += 1
        elif i == '-':
            zn += 1
            tire += 1
        elif i == '.':
            zn += 1
            tochka += 1

print('\nКоличество строк ' + str(strok) + '\nсумма знаков ' + str(zn) + '\nзапятых ' + str(zap) + '\nвосклицательных знаков ' + str(voskl) + '\nтире ' + str(tire) + '\nточек ' + str(tochka))
x.close()
