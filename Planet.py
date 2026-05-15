'''
Примечание.
1. Масса в килограммах Крайне не удобна! Вместо этого она будет измеряться в петатоннах = 10 ** 18 кг
2. Для сортировки для каждого поля нужен отдельный магичский метод сравнения
   Но мы знаем их всего 6, тогда как же сделать сортировку на 7 полей?
   Здесь представлено более разумный метод, позвалящий сравнивать сколько душе угодно полей
   Но также в комментариях указаны части кода, через различные магические методы, но по меньшему числу полей

'''


spisok = []
with open("BD_planet.txt", 'r', encoding = 'utf-8') as file:
    count = len(file.readlines())

class Planet:
    poln_planets = count
    def __init__(self, title, radius, weight, distance):
        global spisok
        Planet.poln_planets += 1
        self.__id = Planet.poln_planets
        self.title = title
        self.radius = radius
        self.weight = weight
        self.distance = distance
        self.__plotn = int((3 * weight * 10 ** 18) / (3.14 * 4 * (radius * 1000) ** 3))
        if 120 <= distance <= 180 and 5100 <= radius <= 7950 and 18 * 10 ** 5 <= weight <= 300 * 10 ** 5 and 4500 <= self.__plotn <= 6000:
            self.__typ = "Землеподобная_планета"
        elif self.__plotn <= 1400:
            self.__typ = "Газовый_гигант"
        elif self.__plotn > 2000:
            self.__typ = "Каменная"
        elif distance >= 2500:
            self.__typ = "Ледяной_гигант"
        else:
            self.__typ = "Газовый_гигант"
        print()
        print(f"Создание ID {self.__id}")
        spisok.append(self)

        
    
    def __copy__(self):
        return copy.copy(self)
    
    def __del__(self):
        print()
        print(f"Удаление ID {self.__id}")
        
    def __str__(self):
        return f'{self.title}, {self.radius}, {self.weight}, {self.__plotn}, {self.distance}, {self.__typ}, {self.__id}'
    
    def __repr__(self):
        return f'Planet({self.title}, {self.radius}, {self.weight}, {self.distance})'
    
    def get_plotn(self):
        return self.__plotn
    
    def get_typ(self):
        return self.__typ
    
    def get_id(self):
        return self.__id
    
    def change_id(self, ID):
        print(f"Замена ID: {self.__id} - {ID}")
        self.__id = ID
    
    def attributes(self):
        return self.title, self.radius, self.weight, self.__plotn, self.distance, self.__typ, self.__id
    
    def __lt__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self.vib < other.vib #self.title > other.title
    
    def __eq__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self.vib == other.vib #self.radius > other.radius
    '''
    def __gt__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self.weight > other.weight
    
    def __le__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self.__plotn > other.__plotn
    
    def __ne__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self.distance > other.distance
    
    def __ge__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        return self.__id > other.__id
    '''
    
    @classmethod
    def from_string(cls, data):
        ima, rad, weg, dis = data.split()
        return cls(ima, int(rad), int(weg), int(dis))

    

def poisk_with_id(ID):
    global spisok
    if not ID.isdigit():
        return False, None, None
    ID = int(ID)
    for i in range(len(spisok)):
        if spisok[i].get_id() == ID:
            return True, spisok[i], i
    return False, None, None
    
def add_in_bd(data):
    global spisok
    obj = Planet.from_string(data)
    return obj

def sorty(attribute, direction):
    global spisok
    if attribute == 'title':
        for planet in spisok:
            planet.vib = planet.title
    elif attribute == 'type':
        for planet in spisok:
            planet.vib = planet.get_typ()
    elif attribute == 'radius':
        for planet in spisok:
            planet.vib = int(planet.radius)
    elif attribute == 'weight':
        for planet in spisok:
            planet.vib = int(planet.weight)
    elif attribute == 'density':
        for planet in spisok:
            planet.vib = int(planet.get_plotn())
    elif attribute == 'distance':
        for planet in spisok:
            planet.vib = int(planet.distance)
    elif attribute == 'id':
        for planet in spisok:
            planet.vib = int(planet.get_id())
    length = len(spisok)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if spisok[j] > spisok[j + 1]:
                spisok[j], spisok[j + 1] = spisok[j + 1], spisok[j]
    if direction == "reverse":
        spisok = spisok[::-1]

def del_with_id(ID):
    zn = poisk_with_id(ID)
    if zn[0]:
        del spisok[zn[2]]
    else:
        print("ID не найден")

def save_lokal_base():
    global spisok
    with open("BD_planet.txt", 'a', encoding = 'utf-8') as out:
        for planet in spisok:
            print(planet, file = out)