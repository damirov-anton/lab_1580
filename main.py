import planet_menu
import item_menu
import preob



def main():
    usl = True
    while usl:
        flag = True
        while flag:
            mode = input("С чем будем работать(planet, item, stop)?: ").lower()
            print()
            if mode == "stop":
                flag = False
                usl = False
            elif mode == "planet":
                flag = False
                planet_menu.menu()
            elif mode == "item":
                flag = False
                item_menu.menu()
            else:
                print("Введите только то, что в скобках!")
                print()
    preob.convert("BD_planet.txt", "BD_planet.csv")
    preob.convert("BD_item.txt", "BD_item.csv")

if __name__ == '__main__':
    main()