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
count = 0
ошика = неверна
проходим по всей исходной строке data
    если данный символ в data не входит в numbers, то
        если данный символ в data является пробелом, то
            count = count + 1
        иначе
            count = count + число, да побольше, уж точно больше 1

если count не равен 1 или первый символ в data не входит в numbers, то
    ошибка верна
если ошибка верна, то
    вернуть ошибка
иначе,
    вернуть data

алг main()
data = запрос данных
time = преобразование(data)
если time = ошибка, то
    вывести Ошибка, попробуйте ввести время в формате: часы(пробел)минуты
    предложить ещё раз
    при отказе
        завершить функцию
если проверка минут(time) = неверно и проверка часов(time) = неверно, то
    вывести Введены недопустимые данные: часы должны быть от 0 до 23, минуты должны быть от 0 до 59.
    предложить ещё раз
    при отказе
        завершить функцию
если проверка часов(time) = неверно, то
    вывести Введены недопустимые данные: часы должны быть от 0 до 23.
    предложить ещё раз
    при отказе
        завершить функцию
если проверка минут(time) = неверно, то
    вывести Введены недопустимые данные: минуты должны быть от 0 до 59.
    предложить ещё раз
    при отказе
        завершить функцию
иначе,
    вывести часы(time)
    предложить ещё раз
    при отказе
        завершить функцию
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
    mistake = False
    count = 0
    strike = 0
    for i in range(len(data)):
        if data[i] not in numbers:
            if data[i] == " ":
                strike = 0
                count += 1
            else:
                count += 15
        else:
            strike += 1
        if strike > 2:
            mistake = True
    if count != 1 or data[0] not in numbers:
        mistake = True
    if mistake:
        return "ошибка"
    else:
        return data
        
    


def main():
    data = input("Введите время: ")
    time = convert(data)
    
    if time == "ошибка":
        print("Ошибка, попробуйте ввести время в формате: часы [пробел] минуты")
        otvet = input("Запустить программу ещё раз? (yes/another) ")
        if otvet.lower() == "yes":
            main()
        else:
            return        
    
    elif not(check_hours(time)) and not(check_minutes(time)):
        print("Введены недопустимые данные: часы должны быть от 0 до 23, минуты должны быть от 0 до 59.")
        otvet = input("Запустить программу ещё раз? (yes/another) ")
        if otvet.lower() == "yes":
            main()
        else:
            return        
    
    elif not(check_minutes(time)):
        print("Введены недопустимые данные: минуты должны быть от 0 до 59.")
        otvet = input("Запустить программу ещё раз? (yes/another) ")
        if otvet.lower() == "yes":
            main()
        else:
            return 
    elif not(check_hours(time)):
        print("Введены недопустимые данные: часы должны быть от 0 до 23.")
        otvet = input("Запустить программу ещё раз? (yes/another) ")
        if otvet.lower() == "yes":
            main()
        else:
            return        
    
    else:
        print(clock(time))
        otvet = input("Запустить программу ещё раз? (yes/another) ")
        if otvet.lower() == "yes":
            main()
        else:
            return        


if __name__ == "__main__":
    main()
