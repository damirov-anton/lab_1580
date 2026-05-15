'''
Примечание.
Для сортировки для каждого поля нужен отдельный магичский метод сравнения
Но мы знаем их всего 6, тогда как же сделать сортировку на 7 полей?
Здесь представлено более разумный метод, позвалящий сравнивать сколько душе угодно полей
Но также в комментариях указаны части кода, через различные магические методы, но по меньшему числу полей
'''


spisok = []
with open("BD_item.txt", 'r', encoding = 'utf-8') as file:
    count = len(file.readlines())

class Item:
    poln_items = count
    def __init__(self, title, category, price, amount, supplier):
        global spisok
        Item.poln_items += 1
        self.__id = Item.poln_items
        self.title = title
        self.category = category
        self.price = price
        self.amount = amount
        self.supplier = supplier
        if 0 <= price <= 1000:
            self.__price_type = 'econom'
        elif 1000 < price <= 5000:
            self.__price_type = 'medium-low'
        elif 5000 < price <= 20000:
            self.__price_type = 'medium-high'
        elif 20000 < price <= 100000:
            self.__price_type = 'premium'
        else:
            self.__price_type = 'luxury'
        print()
        print(f"Создание ID {self.__id}")
        spisok.append(self)

        
    
    def __copy__(self):
        return copy.copy(self)
    
    def __del__(self):
        print()
        print(f"Удаление ID {self.__id}")
    
    def __str__(self):
        return f'{self.title}, {self.category}, {self.price}, {self.__price_type}, {self.amount}, {self.supplier}, {self.__id}'
    
    def __repr__(self):
        return f'Item({self.title}, {self.category}, {self.price}, {self.amount}, {self.supplier})'
    
    def get_price_type(self):
        return self.__price_type
    
    def get_id(self):
        return self.__id
    
    def change_id(self, ID):
        print(f"Замена ID: {self.__id} - {ID}")
        self.__id = ID
    
    def attributes(self):
        return self.title, self.category, self.price, self.__price_type, self.amount, self.supplier, self.__id
    
    def __lt__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.vib < other.vib #self.name > other.name
    
    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.vib == other.vib #self.price > other.price
    '''
    def __gt__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.amount > other.amount
    
    def __ne__(self, other):
    if not isinstance(other, Item):
            return NotImplemented
        return self.__id > other.__id
    
    '''
    
    @classmethod
    def from_string(cls, data):
        ima, cat, price, amount, sup = data.split()
        return cls(ima, cat, int(price), int(amount), sup)

    

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
    obj = Item.from_string(data)
    return obj

def sorty(attribute, direction):
    global spisok
    if attribute == 'title':
        for item in spisok:
            item.vib = item.title
    elif attribute == 'category':
        for item in spisok:
            item.vib = item.category
    elif attribute == 'price':
        for item in spisok:
            item.vib = int(item.price)
    elif attribute == 'price_type':
        for item in spisok:
            item.vib = item.get_price_type()
    elif attribute == 'amount':
        for item in spisok:
            item.vib = int(item.amount)
    elif attribute == 'supplier':
        for item in spisok:
            item.vib = item.supplier
    elif attribute == 'id':
        for item in spisok:
            item.vib = int(item.get_id())
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
        obj = spisok[zn[2]]
        del spisok[zn[2]]
        del obj
    else:
        print("ID не найден")

def save_lokal_base():
    global spisok
    with open("BD_item.txt", 'a', encoding = 'utf-8') as out:
        for item in spisok:
            print(item, file = out)