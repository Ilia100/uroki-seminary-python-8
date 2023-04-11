# Задача 38:
#  Дополнить телефонный справочник возможностью изменения и удаления данных.
#  Пользователь также может ввести имя или фамилию,
#   и Вы должны реализовать функционал для изменения и удаления данных


import csv


def read_csv(filename='hw/phonebook.csv'):
    with open(filename, 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            data.append(line.strip('\n').split(','))
    return data


def display_all_records():
    data = read_csv() 
    for row in data:
        print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def find_last_name():
    last_name = input('Введите фамилию: ')
    data = read_csv() 
    for row in data:
        if row[0] == last_name:
            print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def find_phone_number():
    phone = input('Введите номер телефона: ')
    data = read_csv() 
    for row in data:
        if row[2] == phone:
            print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def add_data(filename='hw/phonebook.csv'):
    with open(filename, 'a', encoding='utf-8') as file:  
        info = input('Введите данные абонента (фамилия, имя, номер, комментарий - через запятую): ').split(', ')
        file.write(','.join(info) + '\n')
        print('Данные записаны.')

def change_data(filename='hw/phonebook.csv'):
    last_name = input('Введите фамилию: ')
    with open(filename, 'r+', encoding='utf-8') as file: 
        reader = csv.reader(file)
        with open('hw/phonebook2.csv', 'w+', encoding='utf-8') as f: 
            writer = csv.writer(f)
            for row in reader:
                if row[0]==last_name:
                    print(1111)
                    print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')
                    print(f'Что сделать с информацией по данному абоненту?\n1 - удалить все данные\n'
                                '2 - Сменить Фамилию\n3 - Сменить Имя\n4 - Сменить Телефон\n5 - Редактировать комментарий\n')
                    num = input()
                    if num == '1':
                        row=""
                    elif num == '2':
                        row[0]=(input("Введите Фамилию абонента: "))
                    elif num == '3':
                        row[1] = (input("Введите Имя абонента: "))
                    elif num == '4':
                        row[2] = input("Введите Телефон абонента: ")                
                    elif num == '5':
                        row[3] = input("Введите Описание абонента: ")
                writer.writerow(row)






number = 0
while number != '6':
    print('Введите число для операции со справочником:')
    print('1 - вывести весь справочник;\n2 - найти абонента по фамилии;\n'
          '3 - найти абонента по номеру телефона;\n4 - ввести данные нового абонента;\n'
          '5 - изменить данные абонента;\n6 - завершить работу.')

    number = input()

    if number == '1':
        display_all_records()

    elif number == '2':
        find_last_name()

    elif number == '3':
        find_phone_number()

    elif number == '4':
        add_data()

    elif number == '5':
        change_data()

else:
    print('Работа завершена.')