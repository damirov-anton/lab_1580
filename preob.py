import csv



def convert(input_file, output_file):
    with open(input_file, 'r', encoding = 'utf-8') as txt_file:
        data = []
        if input_file == "BD_planet.txt":
            row = ['Название', "Радиус", "Масса", "Плотность", "Расстояние_до_Солнца", "Тип_планеты", "ID"]
        elif input_file == "BD_item.txt":
            row = ['Название', "Категория", "Цена", "Тип_цены", "Количество", "Поставщик", "ID"]
        data.append(row)
        for line in txt_file:
            row = line.strip().split(', ')
            data.append(row)
    
    with open(output_file, 'w', newline = '', encoding = 'utf-8-sig') as csv_file:
        writer = csv.writer(csv_file, delimiter = ';')
        writer.writerows(data)
    print(f"Конвертация завершена! Файл сохранён как '{output_file}'")