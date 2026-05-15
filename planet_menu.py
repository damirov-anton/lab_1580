import time
import random
import Planet


def instruction():
    print("Здесь всё легко: имеется база данных планет")
    time.sleep(1)
    print()
    print("У каждой планеты есть 7 характерисик:")
    time.sleep(1)
    print("Название")
    time.sleep(1)
    print("Радиус (в километрах)")
    time.sleep(1)
    print("Масса (в петатоннах [10^18 кг])")
    time.sleep(1)
    print("Плотность (в кг/м^3)")
    time.sleep(1)
    print("Расстояние от Солнца (в миллионах километрах)")
    time.sleep(1)
    print("Тип планеты (Землеподобная, Газовый гигант, Ледяной гигант, Каменная)")
    time.sleep(1)
    print("Уникальный ID")
    print()
    time.sleep(1)
    print("inf - значит прочитать данные о планете из базы данных")
    print()
    time.sleep(2)
    print("write - значит добавить данные о планете в базу данных")
    print()
    time.sleep(2)
    print("delete - значит удалить данные о планете")
    print()
    time.sleep(2)
    print("sort - значит отсортировать данные в базе данных, по одному из критериев:")
    time.sleep(2)
    print("название, тип, плотность, радиус, масса, дистанция от Солнца, ID")
    time.sleep(2)
    print("Также нужно указать в каком порядке будет проходить сортировка:")
    time.sleep(1)
    print("directly - по возрастанию, reverse - по убыванию")
    print()
    time.sleep(2)
    print("edit - значит найти и поменять данные о планете в базе данных")
    print()
    time.sleep(2)
    print("print - значит вывести всю базу данных")
    print()
    time.sleep(2)
    print("discharge - значит выгрузить всю базу данных в локальную")
    print()
    time.sleep(2)
    print("save - значит сохранить локальную базу данных в общую")
    print()
    time.sleep(2)
    print("stop - значит, закончить работу программы")
    print()
    time.sleep(2)


def vivod():
    for planet in Planet.spisok:
        print(planet)
        time.sleep(1)
    print()
    time.sleep(2)


def prov(soo):
    flag = False
    while not flag:
        a = input(soo)
        per = a.isdigit()
        if per:
            a = int(a)
            if a > 0:
                flag = True
            else:
                print("Значение не может быть равно 0!")
        else:
            print("Значение должно быть натуральным числом! ")
    return a


def prov_ima(ima):
    if ima == "":
        return False, "Имя не может состоять из 0 символов!"
    elif " " in ima:
        return False, "В имени планеты не должно содержаться пробелов, заменяйте их на символ '_'! "
    return True, "Прекрасное имя для планеты!"


def newPlanet():
    mode = input('Создадите свою планету или сгенерируем? (create/generate)?: ').lower()
    print()
    time.sleep(2)
    flag = True
    while flag:
        if mode == "create":
            flag = False
            flag_vl = False
            while not flag_vl:
                ima = input("Придумайте название планеты: ")
                print()
                time.sleep(2)
                zn = prov_ima(ima)
                flag_vl = zn[0]
                print(zn[1])
                print()
                time.sleep(2)
            rad = prov("Каков будет радиус?: ")
            time.sleep(2)
            weig = prov("Масса?: ")
            time.sleep(2)
            dist = prov("А как насёт дистанции от солнца?: ")
            time.sleep(2)
        elif mode == "generate":
            flag = False
            flag_vl = False
            while not flag_vl:
                ima = input("Придумайте название планеты: ")
                print()
                time.sleep(2)
                zn = prov_ima(ima)
                flag_vl = zn[0]
                print(zn[1])
            typ_opr = random.random()
            if typ_opr < 0.3:
                weig = random.randint(5700, 41500)
                rad = random.randint(
                    int(((3 * weig * 10 ** 9) / 17584) ** (1 / 3)),
                    int(((3 * weig * 10 ** 9) / 25.12) ** (1 / 3))
                )
                dist = random.randint(58, 6000)
            elif typ_opr < 0.4:
                weig = random.randint(5700, 59260)
                rad = random.randint(
                    int(((3 * weig * 10 ** 9) / 25120) ** (1 / 3)),
                    int(((3 * weig * 10 ** 9) / 25.12) ** (1 / 3))
                )
                dist = random.randint(58, 2500)
            elif typ_opr < 0.8:
                weig = random.randint(59260, 23 * 10 ** 9)
                rad = random.randint(
                    int(((3 * weig * 10 ** 9) / 75360) ** (1 / 3)),
                    int(((3 * weig * 10 ** 9) / 25120) ** (1 / 3))
                )
                dist = random.randint(58, 6000)
            elif typ_opr < 0.99:
                weig = random.randint(41500, 59260)
                rad = random.randint(
                    int(((3 * weig * 10 ** 9) / 25120) ** (1 / 3)),
                    int(((3 * weig * 10 ** 9) / 17584) ** (1 / 3))
                )
                dist = random.randint(2500, 6000)
            else:
                weig = random.randint(1800000, 30000000)
                rad = random.randint (
                    int(((weig * 10 ** 8) / 2512) ** (1 / 3)),
                    int(((weig * 10 ** 8) / 1884) ** (1 / 3))
                )
                dist = random.randint(120, 180)
        else:
            mode = input('Введите "create" или "generate", другого вводить не надо!: ').lower()
            print()
            time.sleep(2)
    return f'{ima} {rad} {weig} {dist}'


def add_planet():
    data = newPlanet()
    obj = Planet.add_in_bd(data)
    print()
    time.sleep(2)
    print("Ваша планета готова!")
    print()
    time.sleep(2)
    print(f'Название - {obj.title}')
    time.sleep(2)
    print(f'Радиус - {obj.radius}')
    time.sleep(2)
    print(f'Масса - {obj.weight}')
    time.sleep(2)
    print(f'Плотность - {obj.get_plotn()}')
    time.sleep(2)
    print(f'Расстояние от Солнца - {obj.distance}')
    time.sleep(2)
    print(f'Тип планеты - {obj.get_typ()}')
    time.sleep(2)
    print(f'ID - {obj.get_id()}')
    print()
    time.sleep(2)    


def look_for():
    zapros = input("Какое ID у искомой планеты?: ")
    print()
    time.sleep(2)
    zn = Planet.poisk_with_id(zapros)
    if zn[0]:
        obj = zn[1]
        print(f'Название - {obj.title}')
        time.sleep(2)
        print(f'Радиус - {obj.radius}')
        time.sleep(2)
        print(f'Масса - {obj.weight}')
        time.sleep(2)
        print(f'Плотность - {obj.get_plotn()}')
        time.sleep(2)
        print(f'Расстояние от Солнца - {obj.distance}')
        time.sleep(2)
        print(f'Тип планеты - {obj.get_typ()}')
        time.sleep(2)
        print(f'ID - {obj.get_id()}')        
        print()
        time.sleep(2)
    else:
        print("Планеты с таким ID нет!")
        print()
        time.sleep(2)


def del_planet():
    zapros = input("Какое ID у искомой планеты?: ")
    print()
    time.sleep(2)
    Planet.del_with_id(zapros)
    print()
    time.sleep(2)


def change():
    zapros = input("Какое ID у искомой планеты?: ")
    print()
    time.sleep(2)
    zn = Planet.poisk_with_id(zapros)
    if zn[0]:
        flag = True
        while flag:
            attribute = input("Что именно вы хотите изменить(title, radius, weight, distance)?: ").lower()
            print()
            time.sleep(2)
            if attribute == "title":
                flag = False
                flag_2 = True
                while flag_2:
                    res = input("Придумайте новое имя планете: ")
                    dan = prov_ima(res)
                    print(dan[1])
                    if dan[0]:
                        flag_2 = False
            elif attribute in ['radius', 'weight', 'distance']:
                flag = False
                res = prov("На что меняете?: ")
            else:
                print("Пишите лишь то, что указано в скобках!")
        print()
        time.sleep(2)
        obj = zn[1]
        if attribute == 'title':
            obj.title = res
        elif attribute == 'radius':
            obj.radius = res
        elif attribute == 'weight':
            obj.weight = res
        elif attribute == 'distance':
            obj.distance = res
        data = f'{obj.title} {obj.radius} {obj.weight} {obj.distance}'
        obj = Planet.add_in_bd(data)
        Planet.del_with_id(zapros)
        print()
        time.sleep(2)
        return [True, obj, int(zapros)]
    else:
        print("Планеты с таким ID нет!")
        print()
        time.sleep(2)
        return [False, None, None]


def sort_base_data():
    flag = True
    while flag:
        attribute = input("По какому полю сортировать(title, radius, weight, density, distance, type, ID)?: ").lower()
        print()
        time.sleep(2)
        if attribute in ('title', 'radius', 'weight', 'density', 'distance', 'type', 'id'):
            flag = False
            flag_02 = True
            while flag_02:
                direction = input("В каком порядке сортировать(directly/reverse)?: ").lower()
                print()
                time.sleep(2)
                if direction in ('directly', 'reverse'):
                    flag_02 = False
                else:
                    print("Пишите то, что в скобках!")
                    print()
                    time.sleep(1)
        else:
            print("Пишите то, что в скобках!")
            print()
            time.sleep(1)
    Planet.sorty(attribute, direction)


def upload():
    with open("BD_planet.txt", 'r', encoding = 'utf-8') as file:
        for stroc in file:
            prom = (stroc.strip()).split(', ')
            obj = Planet.Planet.from_string(f'{prom[0]} {prom[1]} {prom[2]} {prom[4]}')
            Planet.Planet.poln_planets -= 1
            obj.change_id(int(prom[6]))


def save():
    Planet.save_lokal_base()
    sp = []
    spid = []
    with open("BD_planet.txt", 'r', encoding = 'utf-8') as file:
        for stroc in file:
            sp.append((stroc.strip()).split(', '))
    with open("BD_planet.txt", 'w', encoding = 'utf-8') as out:
        it =[]
        for i in range(len(sp) - 1, -1, -1):
            if sp[i][-1] not in spid:
                spid.append(sp[i][-1])
                stroc = f'{sp[i][0]}, {sp[i][1]}, {sp[i][2]}, {sp[i][3]}, {sp[i][4]}, {sp[i][5]}, {sp[i][6]}'
                it.append(stroc)
        it = it[::-1]
        for stroc in it:
            print(stroc, file = out)




def menu():
    usl = True
    while usl:
        flag = True
        while flag:
            rech = input("Что будем делать? (inf, write, delete, sort, edit, print, discharge, save, help, stop): ").lower()
            print()
            time.sleep(1)
            if rech == "help":
                instruction()
                flag = False
            elif rech == "stop":
                flag = False
                usl = False
                save()
                Planet.spisok = []
            elif rech == "print":
                vivod()
                flag = False
            elif rech == "write":
                add_planet()
                flag = False
            elif rech == "delete":
                del_planet()
                flag = False
            elif rech == "inf":
                look_for()
                flag = False
            elif rech == "edit":
                zn = change()
                time.sleep(2)
                if zn[0]:
                    zn[1].change_id(zn[2])
                    print()
                    zn = []
                flag = False                
            elif rech == "sort":
                sort_base_data()
                flag = False
            elif rech == "discharge":
                upload()
                flag = False
            elif rech == "save":
                save()
                flag = False
            else:
                print("Пишите лишь то, что указано в скобках!")
                print()
                time.sleep(2)