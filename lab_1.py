"""
Алгоритм программы:
пока пользователь хочет использовать программу не закнчиваем
запрашиваем его данные
проверяем их на ошимбки
в случае ошибки информируем
предлагаем повторить
"""


def transform_hours(hour):
    hour = int(hour)
    
    if hour % 10 == 1 and (hour < 6 or hour > 19):
        declension = " час "
    
    elif 1 < hour % 10 < 5 and (hour < 6 or hour > 19):
        declension = " часа "
    
    else:
        declension = " часов "
    return str(hour) + declension


def transform_minutes(minute):
    minute = int(minute)
    
    if minute % 10 == 1 and (minute < 6 or minute > 19):
        declension = " минута "
    
    elif 1 < minute % 10 < 5 and (minute < 6 or minute > 19):
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
    elif -1 < hours < 6:
        time_of_the_day = "ночи"
    
    elif 5 < hours < 12:
        time_of_the_day = "утра"
    
    elif 11 < hours < 18:
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
    
    if -1 < int(time[probel + 1:]) < 60:
        return True
    else:
        return False


def check_hours(time):
    probel = time.find(" ")
    
    if -1 < int(time[:probel]) < 24:
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
        

def razgovor():
    flag = True
    while flag:
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
            print(clock(time))

        usl = razgovor()
            
    return


if __name__ == "__main__":
    main()
