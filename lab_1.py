"""
Алгоритм программы:

пока пользователь не завершил программу
запрашиваем его данные
проверяем их на ошибки
    в случае ошибки информируем о правильном формате ввода
    в случае несоответствии с возможными значениями информируем об этом
иначе
    выдаём желаемый результат
предлагаем повторить

проверка введённых данных:
вводим счётчик
проверяем каждый эллемент введёных данных
    если данный эллемент не число, то проверяем, что это пробел и он не стоит вначале
        если это так, то обнуляем счётчик
        иначе выводим ошибку
    иначе прибавляем к счётчику 1
    если счётчик больше 2, то выводим ошибку
выводим обратно изначальные данные

Обратботка ответа пользователя на продолжение работы программы:
если пользователь согласился, то продолжаем программу
если пользователь отказался, то завершаем программу
иначе предупреждаем о некоректности введённых данных
Получение результата:
считываем уже проверенные данные пользователя
проверяем на особые случаи
    если это особый случай, то выводим его
выбираем минутам и часам верное склонение
    если склонение минут ровно, то выводим результат в особом порядке
иначе
    выводим результат в штатном порядке

"""


def transform_hours(hour):
    hour = int(hour)
    
    if hour % 10 == 1 and (hour < 6 or hour >= 21):
        declension = " час "
    
    elif 2 <= hour % 10 < 5 and (hour < 6 or hour >= 21):
        declension = " часа "
    
    else:
        declension = " часов "
    return str(hour) + declension


def transform_minutes(minute):
    minute = int(minute)
    
    if minute % 10 == 1 and (minute < 6 or minute >= 21):
        declension = " минута "
    
    elif 2 <= minute % 10 < 5 and (minute < 6 or minute >= 21):
        declension = " минуты "
    
    else:
        declension = " минут "
    return str(minute) + declension


def time_of_the_day(time):
    probel = time.find(" ")
    hours = int(time[:probel])
    minutes = int(time[probel + 1:])
    
    if hours == 0 and minutes == 0:
        time_of_the_day = "полночь"
    
    elif hours == 12 and minutes == 0:
        time_of_the_day = "полдень"
    elif 0 <= hours < 6:
        time_of_the_day = "ночи"
    
    elif 6 <= hours < 12:
        time_of_the_day = "утра"
    
    elif 12 <= hours < 18:
        time_of_the_day = "дня"
    
    else:
        time_of_the_day = "вечера"
    return time_of_the_day


def clock(time):
    time_of_day = time_of_the_day(time)
    
    if time_of_day == "полночь" or time_of_day == "полдень":
        return time_of_day
    
    probel = time.find(" ")
    minute = time[probel + 1:]
    
    if int(minute) == 0:
        minutes = " ровно"
    else:
        minutes = transform_minutes(minute)
    
    hour = time[:probel]
    hours = transform_hours(hour)
    
    if minutes == " ровно":
        clock = hours + time_of_day + minutes  
    else:
        clock = hours + minutes + time_of_day
    return clock


def check_minutes(time):
    probel = time.find(" ")
    
    if 0 <= int(time[probel + 1:]) < 60:
        return True
    else:
        return False


def check_hours(time):
    probel = time.find(" ")
    
    if 0 <= int(time[:probel]) < 24:
        return True
    else:
        return False


def convert(data):
    numbers = "0123456789"
    count = 0
    strike = 0
    for i in range(len(data)):
        if data[i] not in numbers:
            if data[i] == " " and i != 0:
                strike = 0
                count += 1
            else:
                return "ошибка"
        else:
            strike += 1
        if strike > 2 or count > 1:
            return "ошибка"
    return data
        

def razgovor():
    while True:
        otvet = input("Запустить программу ещё раз? (y/n): ")
        if otvet.lower() == "y":
            return True
        elif otvet.lower() == "n":
            return False
        else:
            print("Указано же! y/n. Другие значения не принимаются!")


def main():
    usl = True
    while usl:
        data = input("Введите время: ")
        time = convert(data)
    
        if time == "ошибка":
            print("Ошибка, попробуйте ввести время в формате: часы [пробел] минуты")
    
        elif not(check_hours(time)) and not(check_minutes(time)):
            print("Введены недопустимые данные: часы должны быть от 0 до 23, минуты должны быть от 0 до 59.")
    
        elif not(check_minutes(time)):
            print("Введены недопустимые данные: минуты должны быть от 0 до 59.")

        elif not(check_hours(time)):
            print("Введены недопустимые данные: часы должны быть от 0 до 23.")
    
        else:
            result = clock(time)
            print(result)

        usl = razgovor()
            
    return


if __name__ == "__main__":
    main()
