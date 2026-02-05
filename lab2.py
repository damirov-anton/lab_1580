'''
Алгоритм работы:
запрашиваем у пользователя режим работы программы
при неисправности данных сообщаем об этом и просим их переписать
демонстрируем выбранный режим
запрашиваем будет ли повторное использование программы
при неисправности введённых данных сообщаем и просим переписать

Алгоритм работы демонстрационного режима:
генерируем случайный массив из 10 целых чисел в диапазоне от 0 до 99
сортируем данный массив каждым из методов, подсчитывая количество сранений и перестановок в каждом
показываем пользователю таблицу с количеством сравнений и перестановок у каждого метода
выявяем лучший метод и сообщаем это пользователю
предлагаем повторить демонстрацию или завершить её

Алгоритм выявления лучшего метода:
находим метод, у которого сумма количества сравнений и перестановок наименьшая
именуем выявленный метод лучшим для данного массива

Алгоритм работы интерактивного режима:
запарашиваем у пользователя длину первоначального массива
предлагаем пользователю работать с массивом, выданным программой
Даём выбор между четырьмя различными действиями
Предлагаем продолжить работу с массивом или завершить её

Алгоритм работы повторной сортировки:
предлагаем пользователю 4 метода сортировки на выбор, которым будет отсортирован массив
сортируем массив данным методом
показываем исходный и отсортированный массив, а также количество сравнений и перестановок

Алгоритм работы изменения массива:
предлагаем пользователю изменить весь массив, его часть или вообще его не менять
Если пользователь захотел поменять полностью массив, то даём ему возможность его ввести
  при обнаружении факта, что массив не является целочисленным или является пустым, сообщыем пользоватю и просим переписать данные
Иначе если пользователь захотел поменять часть массива, то запрашиваем количество элементов, которые он хочет заменить
  если принятое количество не является натуральным числом, то сообщаем об этом пользователю и просим переписать
  запрашиваем поочерёдно значение и индекс каждого заменяемого элемента
  заменяем элементы на данных индексах на данные значения
Иначе не делаем ничего
сохраняем новый массив

Алгоритм работы сортировки вставками(Insertion sort):
перебираем все элементы начиная со второго
Если данный элемент меньше предыдущего, то меняем его местами

Алгоритм работы сортировки Шелла (Shell sort):
Выбираем некоторый шаг
Сортируем списки, состоящие из элементов, индексы которых отличаются на данный шаг
уменьшаем шаг в 2 раза, пока шаг не будет равен 0

'''


import random
import time


def buble_sort(spis):
    length = len(spis)
    comp = 0
    perm = 0
    for i in range(length - 1):
        for j in range(length - i - 1):
            if spis[j] > spis[j + 1]:
                spis[j], spis[j + 1] = spis[j + 1], spis[j]
                perm += 1
            comp += 1
    return spis, comp, perm

def selection_sort(spis):
    length = len(spis)
    comp = 0
    perm = 0
    for i in range(length):
        min_ind = i
        for j in range(1 + i, length):
            if spis[j] < spis[i]:
                min_ind = j
            comp += 1
        if min_ind != i:
            spis[i], spis[min_ind] = spis[min_ind], spis[i]
            perm += 1
    return spis, comp, perm


def insertion_sort(spis):
    length = len(spis)
    comp = 0
    perm = 0
    for i in range(1, length):
        element = spis[i]
        j = i - 1
        comp += 1
        while j >= 0 and element < spis[j]:
            spis[j + 1], spis[j] = spis[j], spis[j + 1]
            j -= 1
            comp += 1
            perm += 1
    return spis, comp, perm


def Shell_sort(spis):  
    length = len(spis)
    comp = 0
    perm = 0
    dist = length // 2  
    while dist > 0:
        for i in range(dist, length):  
            element = spis[i]  
            j = i
            comp += 1
            while j >= dist and spis[j - dist] > element:  
                spis[j], spis[j - dist] = spis[j - dist], spis[j]
                j -= dist
                comp += 1
                perm += 1
        dist //= 2
    return spis, comp, perm

def create_table(comp_bub, perm_bub, comp_sel, perm_sel, comp_ins, perm_ins, comp_shell, perm_shell):
    table = []
    table.append(['///', 'Buble_sort', 'Selection_sort', 'Insertion_sort', 'Shell_sort'])
    table.append(['Кол-во сравнений', comp_bub, comp_sel, comp_ins, comp_shell])
    table.append(['Кол-во перестановок', perm_bub, perm_sel, perm_ins, perm_shell])
    return table
    


def generation(length):
    spis = [random.randint(0, 99) for _ in range(length)]
    return spis


def win(table):
    bub = table[1][1] + table[2][1]
    sel = table[1][2] + table[2][2]
    ins = table[1][3] + table[2][3]
    shel = table[1][4] + table[2][4]
    minimum = min(bub, sel, ins, shel)
    if minimum == bub:
        return "Buble sort"
    elif minimum == sel:
        return "Selection sort"
    elif minimum == ins:
        return "Insertion sort"
    else:
        return "Shell sort"


def demonstration():
    end = False
    while end == False:
        print("Вы выбрали демонстрацию")
        print("...")
        time.sleep(1)
        print("Что ж...")
        time.sleep(1)
        print("для начала выберем массив, который будем сортировать")
        massive = generation(10)
        mass_bub = massive.copy()
        mass_sel = massive.copy()
        mass_ins = massive.copy()
        print("Пусть будет, к примеру, этот:", massive)
        time.sleep(4)   
        print("...")    
        print("Ого, вам невероятно повезло!")
        print("Шанс того, что вам попадётся  именно этот массив составляет...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("...")
        print("примерно 1 сто квинтиллионная! [10 в минус 20 степени]")
        print("...")
        time.sleep(2)
        print("Ну... Начнём сортировку!")
        sort_massive = Shell_sort(massive)
        time.sleep(2)
        print("отсортированный массив будет выглядеть так:", sort_massive[0])
        print("...")
        time.sleep(2)
        print("Теперь проведём анализ сортировки каждым методом")
        print("Всего их 4:")
        print()
        print("1.'Buble sort'; 2.'Selection sort'; 3.'Insertion sort'; 4.'Shell sort'")
        print("'Shell sort' - это усовершенствованная версия 'Inversion sort'")
        print()
        time.sleep(4)
        print("Наши бойцы справились с поставленной задачей данным успехом:")
        print()
        table = create_table(*buble_sort(mass_bub)[1:], *selection_sort(mass_sel)[1:], *insertion_sort(mass_ins)[1:], *sort_massive[1:])
        columns = len(table)
        lines = len(table[0])
        for i in range(columns):
            for j in range(lines):
                print(str(table[i][j]).rjust(20), end = '')
            print()
        print()
        print("Назовём победителя!")
        time.sleep(2)
        print("И им становиться...")
        time.sleep(4)
        print("...")
        time.sleep(6)
        winner = win(table)
        print(winner)
        time.sleep(1)
        print()
        print("Для данного массива данный метод оказался более эффективным")
        print()
        print("Спасибо, за уделённое время, советую попробовать другой режим работы")
        print("Или ещё раз посмотреть демонстрацию")
        print()
        otvet = input("Если вы хотите повторить демонстрацию напишите 'again', иначе 'stop': ").lower()
        while otvet != "stop" and otvet != "again":
            print()
            print("не надо писать иного, кроме again и stop")
            print()
            otvet = input("Если вы хотите повторить демонстрацию напишите 'again', иначе 'stop': ").lower()
        print()
        if otvet == "stop":
            end = True
        else:
            print("Я знал, что тебе понравиться")


def prov_int_mass(spis):
    for element in spis:
        if not(element.isdigit()):
            return False
    return True


def change(massive, mass):
    print("Массив на данный момент выглядит так: ", mass)
    length = len(massive)
    key = False
    while key == False:
        otvet = input("Хотите ли вы что-нибудь изменить? (nothing/part/all): ").lower()
        print()
        if otvet != "nothing" and otvet != "part" and otvet != "all":
            print("не надо писать иного, кроме nothing, и part, all")                
        else:
            key = True
        print()
    time.sleep(1)
    if otvet == "all":
        key = False
        while key == False:
            massive = input("Тогда введите в строчку через пробел свой массив: ").split()
            if len(massive) == 0:
                print("Не надо вводить пустой массив")
            else:
                if not(prov_int_mass(massive)):
                    print("Все элемента массива должны быть числами!")
                else:
                    key = True
                    massive = list(map(int, massive))
        length = len(massive)
    elif otvet == "part":
        key = False
        while key == False:
            count = input("Введите сколько элементов вы хотите изменить?: ")
            print()
            if not(count.isdigit()):
                print("Введите целое число!")
            else:
                if int(count) > length:
                    print("Вы не можете поменять элементов больше, чем в массиве")
                else:
                    key = True
        key = False
        print("Вевдите", count, "раз(-а-) два числа, значение элемента и его номер в массиве (первый элемент - 1): ")
        count = int(count)
        for i in range(count):
            key = False
            while key == False:
                inform = input("Элемент и индекс: ").split()
                print()
                if len(inform) != 2:
                    print("Введите ровно 2 числа")
                else:
                    znach = inform[0]
                    index = inform[1]
                    if not(znach.isdigit()) or not(index.isdigit()):
                        print("Введите ещё раз, принимаются только целые числа!")
                    else:
                        index = int(index)
                        if index > length:
                            print("индекс не может быть больше, чем ", length, "!", sep = "")
                        else:
                            znach = int(znach)
                            key = True
            del massive[index - 1]
            massive.insert(index - 1, znach)
    else:
        print("Отлично, тогда можно приступить к действиям!")
    return massive


def action(massive, mass):
    length = len(massive)
    key = False
    while key == False:
        otvet = input("Что вы хотите сделать с массивом (return/sort/sort_again/change)?: ").lower()
        print()
        if otvet != "return" and otvet != "sort" and otvet != "sort_again" and otvet != "change" :
            print("не надо писать иного, кроме return, sort, sort_again и change")                
        else:
            key = True
        print()
    if otvet == "return":
        print("Массив:", massive)
    elif otvet == "change":
        massive = change(massive, mass)
        mass = massive.copy()
    elif otvet == "sort":
        massive = mass.copy()
        time.sleep(1)
        if length > 20:
            print("Массив не из маленьких! В этом случае из 4 имеющихся сортировок лучшей будет Shell sort")
            massive = Shell_sort(massive)[0]
        else:
            print("Массив небольшой, здесь отлично подойдёт Insertion sort")
            massive = insertion_sort(massive)[0]
        time.sleep(1)
        print("Массив отсортирован!")
    else:
        massive = mass.copy()
        print("Выберите, каким методом будете сортировать массив (1.Buble sort 2.Selection sort 3.Insertion sort 4.Shell sort) введите только число!")
        time.sleep(1)
        key = False
        while key == False:
            metod = input("Введите метод сортировки: ")
            if metod != "1" and metod != "2" and metod != "3" and metod != "4":
                print("Введите, пожалуйста, только число")
            else:
                key = True
        if metod == "1":
            dan = buble_sort(massive)
        elif metod == "2":
            dan = selection_sort(massive)
        elif metod == "3":
            dan = insertion_sort(massive)
        else:
            dan = Shell_sort(massive)
        print()
        print("Исходный массив:", mass)
        print("Сам массив:", dan[0])
        print("Количество сравнений:", dan[1])
        print("Количество перестановок:", dan[2])
    return massive, mass


def intersctive():
    print("Вы выбрали интерактивный режим")
    print()
    time.sleep(1)
    print("Что ж, видно вы решили серьёзно углубиться в тему сортировки")
    time.sleep(1)
    print("Надо создать первоначальный массив, потом по желанию вы его позже откорректируете")
    print()
    time.sleep(1)
    key = False
    while key == False:
        length = input("какова длина вашего массива?: ")
        print()
        if not(length.isdigit()):
            print("Введите целое число!")
        else:
            length = int(length)
            if length < 1:
                print("Число должно быть натрульным, то есть целым и больше 0")
            else:
                key = True
        print()
    time.sleep(1)
    massive = generation(length)
    print("Первоначальная версия массива: ", massive)
    time.sleep(2)
    mass = massive.copy()
    end = False
    while end == False:
        inform = action(massive, mass)
        time.sleep(2)
        massive = inform[0]
        mass = inform[1]
        print()
        key = False
        while key == False:
            otvet = input("Хотите ли вы продолжить? (yes/no): ").lower()
            if otvet != "yes" and otvet != "no":
                print("Введите только no или yes, ничего иного")
            else:
                key = True
                if otvet == "no":
                    end = True


def main():
    end = False
    while end == False:
        mode = input("Введите режим работы (dem - демонстративный / int - интерактивный): ").lower()
        while mode != "dem" and mode != "int":
            print()
            print("не надо писать иного, кроме dem и int")
            print()
            mode = input("Введите режим работы (dem - демонстративный / int - интерактивный): ").lower()
            print()
        if mode == "int":
            intersctive()
        else:
            demonstration()
        print()
        time.sleep(1)
        solution = input("Продолжите или завершите программу? (continue/stop): ")
        while solution != "continue" and solution != "stop":
            print()
            print("не надо писать иного, кроме continue и stop")
            print()
            solution = input("Продолжите или завершите программу? (continue/stop): ")
            print()
        if solution == "stop":
            end = True 

if __name__ == "__main__":
    main()