list = ['1', '2', '4', '3']
k = ''
j = 0
while 1:
    print('1 - добавление элемента в конец списка\n2 - Добавление эелмента на опрдлённую позицию\n'
          '3 - удаление элемента по индексу и по ключу\n4 - размер списка\n5 - сортировка по убыванию и '
          'возрастанию\n6 - вывод на экран элементов списка\n0 - выход из программы')

    oper = input('Выберите операцию:')

    if oper =='1':
        list.append(input('Введите значение'))
    if oper =='2':
        list.insert(int(input('Позиция:'))-1, int(input('Значние:')))
    if oper =='3':
        print('Удалить по индексу - 1')
        print('Удалить по ключу - 2')
        if input('выберите действие') == '1':
            index_del = int(input('Введите индекс:'))
            if len(list) > index_del:
                del list[index_del]
            else:
                print('Вы вышли за пределы списка\n')
        else:
            k = input('введите ключ:')
            for i in list:
                if i == k:
                    del list[j]
                j += 1

    if oper == '4':
        print('Длина списка = ' + str(len(list)))
    if oper == '5':
        print('Сортировка по убыванию и возрастанию:')
        print('1 - по возрастанию')
        print('2 - по убыванию')
        if input() == '1':
            str(list.sort())
            print('OK')
        else:
            str(list.sort(reverse=True))
            print('OK')
    if oper =='6':
        print('Список:')
        print(list, '\n')
    if oper =='0':
        print("Досвидания!")
        break
