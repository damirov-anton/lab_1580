import time
import random
import Item


def instruction():
    print("Здесь всё легко: имеется база данных товаров")
    time.sleep(1)
    print()
    print("У каждого товара есть 7 характерисик:")
    time.sleep(1)
    print("Название")
    time.sleep(1)
    print("Категория")
    time.sleep(1)
    print("Цена (в рублях)")
    time.sleep(1)
    print("Тип цены (насколько дорого)")
    time.sleep(1)
    print("Количество")
    time.sleep(1)
    print("Поставщик")
    time.sleep(1)
    print("Уникальный ID")
    print()
    time.sleep(1)
    print("inf - значит прочитать данные о товаре из базы данных")
    print()
    time.sleep(2)
    print("write - значит добавить данные о товаре в базу данных")
    print()
    time.sleep(2)
    print("delete - значит удалить данные о товаре")
    print()
    time.sleep(2)
    print("sort - значит отсортировать данные в базе данных, по одному из критериев:")
    time.sleep(2)
    print("название, категория, цена, тип цены, количество, поставщик, ID")
    time.sleep(2)
    print("Также нужно указать в каком порядке будет проходить сортировка:")
    time.sleep(1)
    print("directly - по возрастанию, reverse - по убыванию")
    print()
    time.sleep(2)
    print("edit - значит найти и поменять данные о товаре в базе данных")
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
    for item in Item.spisok:
        print(item)
        time.sleep(1)
    print()
    time.sleep(2)


def prov(soo):
    flag = False
    while not flag:
        a = input(soo)
        flag = a.isdigit()
        if not flag:
            print("Значение должно быть натуральным числом! ")
    return int(a)


def prov_ima(ima, attr):
    if ima == "":
        return False, f"Имя {attr} не может состоять из 0 символов!"
    elif " " in ima:
        return False, f"В имени {attr} не должно содержаться пробелов, заменяйте их на символ '_'! "
    if attr == "товара":
        return True, f"Прекрасное имя для товара!"
    elif attr == "категории":
        return True, f"Прекрасная категория товара!"
    elif attr == "поставщика":
        return True, f"Прекрасный поставщик товара!"    


def newItem():
    flag = False
    while not flag:
        ima = input("Придумайте название товара: ")
        print()
        time.sleep(2)
        zn = prov_ima(ima, "товара")
        flag = zn[0]
        print(zn[1])
        print()
        time.sleep(2)
    flag = False
    while not flag:
        cat = input("Придумайте название категории товара: ")
        print()
        time.sleep(2)
        zn = prov_ima(ima, "категории")
        flag = zn[0]
        print(zn[1])
        print()
        time.sleep(2)
    flag = False
    while not flag:
        sup = input("Придумайте имя поставщика товара: ")
        print()
        time.sleep(2)
        zn = prov_ima(ima, "поставщика")
        flag = zn[0]
        print(zn[1])
        print()
        time.sleep(2)
    price = prov("Сколько стоит товар?: ")
    print()
    time.sleep(2)
    amount = prov("Сколько всего товара?: ")
    print()
    time.sleep(2)
    return f'{ima} {cat} {price} {amount} {sup}'


def add_item():
    data = newItem()
    obj = Item.add_in_bd(data)
    print()
    time.sleep(2)
    print("Ваш товар готов!")
    print()
    time.sleep(2)
    print(f'Название - {obj.title}')
    time.sleep(2)
    print(f'Категория - {obj.category}')
    time.sleep(2)
    print(f'Цена - {obj.price}')
    time.sleep(2)
    print(f'Тип цены - {obj.get_price_type()}')
    time.sleep(2)
    print(f'Количество - {obj.amount}')
    time.sleep(2)
    print(f'Поставщик - {obj.supplier}')
    time.sleep(2)
    print(f'ID - {obj.get_id()}')        
    print()
    time.sleep(2)      


def look_for():
    zapros = input("Какое ID у искомого товара?: ")
    print()
    time.sleep(2)
    zn = Item.poisk_with_id(zapros)
    if zn[0]:
        obj = zn[1]
        print(f'Название - {obj.title}')
        time.sleep(2)
        print(f'Категория - {obj.category}')
        time.sleep(2)
        print(f'Цена - {obj.price}')
        time.sleep(2)
        print(f'Тип цены - {obj.get_price_type()}')
        time.sleep(2)
        print(f'Количество - {obj.amount}')
        time.sleep(2)
        print(f'Поставщик - {obj.supplier}')
        time.sleep(2)
        print(f'ID - {obj.get_id()}')        
        print()
        time.sleep(2)        
    else:
        print("Товара с таким ID нет!")
        print()
        time.sleep(2)


def del_item():
    zapros = input("Какое ID у искомого товара?: ")
    print()
    time.sleep(2)
    Item.del_with_id(zapros)
    print()
    time.sleep(2)


def change():
    zapros = input("Какое ID у искомого товара?: ")
    print()
    time.sleep(2)
    zn = Item.poisk_with_id(zapros)
    if zn[0]:
        flag = True
        while flag:
            attribute = input("Что именно вы хотите изменить(title, category, price, amount, supplier)?: ").lower()
            print()
            time.sleep(2)
            if attribute == "title":
                flag = False
                flag_2 = True
                while flag_2:
                    res = input("Придумайте новое название товару: ")
                    dan = prov_ima(res, "товара")
                    print(dan[1])
                    if dan[0]:
                        flag_2 = False
            elif attribute == "category":
                flag = False
                flag_2 = True
                while flag_2:
                    res = input("Какая категория?: ")
                    dan = prov_ima(res, "категории")
                    print(dan[1])
                    if dan[0]:
                        flag_2 = False
            elif attribute == "supplier":
                flag = False
                flag_2 = True
                while flag_2:
                    res = input("Кто поставщик?: ")
                    dan = prov_ima(res, "поставщика")
                    print(dan[1])
                    if dan[0]:
                        flag_2 = False                
            elif attribute in ('price', 'amount'):
                flag = False
                res = prov("На что меняете?: ")
            else:
                print("Пишите лишь то, что указано в скобках!")
        print()
        time.sleep(2)
        obj = zn[1]
        if attribute == 'title':
            obj.title = res
        elif attribute == 'category':
            obj.category = res
        elif attribute == 'price':
            obj.price = res
        elif attribute == 'amount':
            obj.amount = res
        elif attribute == 'supplier':
            obj.supplier = res        
        data = f'{obj.title} {obj.category} {obj.price} {obj.amount} {obj.supplier}'
        obj = Item.add_in_bd(data)
        Item.del_with_id(zapros)
        print()
        time.sleep(2)
        return [True, obj, int(zapros)]
    else:
        print("Товара с таким ID нет!")
        print()
        time.sleep(2)
        return [False, None, None]


def sort_base_data():
    flag = True
    while flag:
        attribute = input("По какому полю сортировать(title, category, price, price_type, amount, supplier, ID)?: ").lower()
        print()
        time.sleep(2)
        if attribute in ('title', 'category', 'price', 'price_type', 'amount', 'supplier', 'id'):
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
    Item.sorty(attribute, direction)


def upload():
    with open("BD_item.txt", 'r', encoding = 'utf-8') as file:
        for stroc in file:
            prom = (stroc.strip()).split(', ')
            obj = Item.Item.from_string(f'{prom[0]} {prom[1]} {prom[2]} {prom[4]} {prom[5]}')
            Item.Item.poln_items -= 1
            obj.change_id(int(prom[6]))


def save():
    Item.save_lokal_base()
    sp = []
    spid = []
    with open("BD_item.txt", 'r', encoding = 'utf-8') as file:
        for stroc in file:
            sp.append((stroc.strip()).split(', '))
    with open("BD_item.txt", 'w', encoding = 'utf-8') as out:
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
                Item.spisok = []
            elif rech == "print":
                vivod()
                flag = False
            elif rech == "write":
                add_item()
                flag = False
            elif rech == "delete":
                del_item()
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