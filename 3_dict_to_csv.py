"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

person_list = [
        {'age': 18, 'name': 'Ted', 'job': 'desinger'},
        {'age': 29, 'name': 'Alex', 'job': 'developer'},
        {'age': 21, 'name': 'Max', 'job': 'cook'},
        {'age': 23, 'name': 'Mary', 'job': 'fashion model'},
        {'age': 28, 'name': 'Elizabeth', 'job': 'actor'},
        {'age': 31, 'name': 'Metthew', 'job': 'businessman'}
    ]

def main():
    with open('jobs.csv', 'w', encoding='utf-8') as file:
        fields = ['age', 'name', 'job']
        persons = csv.DictWriter(file, fields, delimiter=';')
        persons.writeheader()
        for person in person_list:
            persons.writerow(person)

if __name__ == "__main__":
    main()
