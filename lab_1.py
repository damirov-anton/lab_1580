'''
Алгоритм работы программы.


алг представление часов(hour)
hour = цел(hour)
если hour % 10 = 1 и (hour меньше 6 или больше 21), то
    склонение = час
иначе если hour % 10 от 2 до 4 и (hour меньше 6 или больше 21), то
    склонение = часа
иначе,
    склонение = часов
вернуть строк(hour + склонение)

алг представление минут(minute)
минута = цел(minute)
если minute % 10 = 1 и (minute меньше 6 или больше 21), то
    склонение = минута
иначе если minute % 10 от 2 до 4 и (minute меньше 6 или больше 21), то
    склонение = минуты
иначе,
    склонение = минут
вернуть строк(minute + склонение)

алг представление времени суток(time)
probel = наход(пробел) в time
hour = цел(от начала до пробела) в time
minute = цел(от след после пробела до конца) в time
если hour = 0 и minute = 0, то
   time of day = полночь
иначе если hour = 12 и minute = 0, то
    time of day = полдень
иначе если hour от 0 до 5, то
    time of day = ночи
иначе если hour от 6 до 11, то
    time of day = утра
иначе если hour от 12 до 17, то
    time of day = дня
иначе,
    time of day = вечера
вернуть time of day

алг проверка минут(time)
probel = наход(пробел) в time
minute = цел(от след после пробела до конца) в time
если цел(minute) от 0 до 59, то
    вернуть верно
иначе,
    вернуть неверно

алг проверка часов(time)
probel = наход(пробел) в time
hour = цел(от начала до пробела) в time
если цел(hour) от 0 до 23, то
    вернуть верно
иначе,
    вернуть неверно

алг часы(time)
probel = наход(пробел) в time
hour = цел(от начала до пробела) в time
minute = цел(от след после пробела до конца) в time
если minute = 0, то
    minutes = ровно
иначе,
    minutes = представление минут(minute)
hours = представление часов(hour)
time of day = представление времени суток(time)
если time of day = полночь или time of day = полдень, то
    вернуть time of day
иначе,
    если минуты = ровно, то
        вернуть строк(hours + time of day + minutes)
    иначе,
        вернуть строк(hours + minutes + time of day)

алг преобразование(data)
numbers = список всех цифр
time = пустая строка
separator = неверно
count = 0
last = пустая строка
проходим по всей исходной строке data
    если данный символ в data не входит в numbers и separator = неверно, то
        separator = верно
        count = count + 1
        time = time + пробел
        last = данный символ в data
    иначе
        если данный символ в data входит в numbers и separator = верно, то
            separator = неверно
            time = time + данный символ в data
        иначе если данный символ в data входит в numbers, то
            time = time + данный символ в data
        иначе,
            если last НЕ= данный символ в data, то
                count = count + 1
probel = наход(пробел) в time
hour = цел(от начала до пробела) в time
minute = цел(от след после пробела до конца) в time
если длина строк(hours) больше 2 или длина строк(minutes) больше 2 или count НЕ= 1, то
    вернуть ошибка
иначе,
    вернуть time

алг main()
data = запрос данных
time = преобразование(data)
если time = ошибка, то
    вывести Ошибка, попробуйте ввести время в формате: часы минуты
    завершить функцию
если проверка часов(time) = неверно, то
    вывести Введены недопустимые данные: часы должны быть от 0 до 23.
    завершить функцию
если проверка минут(time) = неверно, то
    вывести Введены недопустимые данные: часы должны быть от 0 до 59.
    завершить функцию
иначе,
    вывести часы(time)
'''


def transform_hours(hour):
    hour = int(hour)
    
    if hour % 10 == 1 and (hour <= 5 or hour >= 20):
        declension = " час "
    
    elif 2 <= hour % 10 <= 4 and (hour <= 5 or hour >= 20):
        declension = " часа "
    
    else:
        declension = " часов "
    return str(hour) + declension


def transform_minutes(minute):
    minute = int(minute)
    
    if minute % 10 == 1 and (minute <= 5 or minute >= 20):
        declension = " минута "
    
    elif 2 <= minute % 10 <= 4 and (minute <= 5 or minute >= 20):
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
    elif 0 <= hours <= 5:
        time_of_the_day = "ночи"
    
    elif 6 <= hours <= 11:
        time_of_the_day = "утра"
    
    elif 12 <= hours <= 17:
        time_of_the_day = "дня"
    
    else:
        time_of_the_day = "вечера"
    return time_of_the_day


def clock(time):
    probel = time.find(" ")
    minute = time[probel + 1:]
    
    if int(minute) == 0:
        minutes = " ровно"
    else:
        minutes = transform_minutes(minute)
    
    hour = time[:probel]
    hours = transform_hours(hour)
    time_of_day = time_of_the_day(time)
    
    if time_of_day == "полночь" or time_of_day == "полдень":
        return time_of_day
    else:
        if minutes == " ровно":
            clock = hours + time_of_day + minutes
        
        else:
            clock = hours + minutes + time_of_day
        return clock


def check_minutes(time):
    probel = time.find(" ")
    
    if 0 <= int(time[probel + 1:]) <= 59:
        return True
    else:
        return False


def check_hours(time):
    probel = time.find(" ")
    
    if 0 <= int(time[:probel]) <= 23:
        return True
    else:
        return False


def convert(data):
    numbers = "0123456789"
    time = ""
    separator = False
    count = 0
    last = ""
    
    for i in range(len(data)):
        if data[i] not in numbers and not(separator):
            time += " "
            separator = True
            count += 1
            last = data[i]
        
        else:
            if separator and data[i] in numbers:
                separator = False
                time += data[i]
            
            elif data[i] in numbers:
                time += data[i]
            
            else:
                if data[i] != last:
                    count += 1
    
    probel = time.find(" ")
    hours = time[:probel]
    minutes = time[probel + 1:]
    
    if len(hours) > 2 or len(minutes) > 2 or count != 1:
        return "ошибка"
    else:
        return time


def main():
    data = input("Введите время: ")
    time = convert(data)
    
    if time == "ошибка":
        print("Ошибка, попробуйте ввести время в формате: часы минуты")
        return
    
    elif not(check_hours(time)):
        print("Введены недопустимые данные: часы должны быть от 0 до 23.")
        return
    
    elif not(check_minutes(time)):
        print("Введены недопустимые данные: минуты должны быть от 0 до 59.")
        return
    
    else:
        print(clock(time))


if __name__ == "__main__":
    main()
