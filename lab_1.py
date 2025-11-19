"""
Алгоритм программы:

"""


def transform_hours(hour):
    hour = int(hour)
    
    if hour % 10 == 1 and (hour < 6 or hour > 19):
        declension = " час "
    
    elif 2 <= hour % 10 <= 4 and (hour < 6 or hour > 19):
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
