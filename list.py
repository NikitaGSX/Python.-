#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
from pprint import pprint as pp
import csv
import json

os_prod_list    = 'Изготовитель системы'
os_name_list    = 'Название ОС'
os_code_list    = 'Код продукта'
os_type_list    = 'Тип системы'
regex_name      = r':\s+(.+)'
spisok          = ["./data/info_1.txt", "./data/info_2.txt", "./data/info_3.txt"]

#def get_data(**kwargs):
def get_data(prod_name=None, os_name=None, code_name=None, system_name=None):

    '''
    По програме курса есть изучение функций? Столкнулся здесь с позициоными аргументами. А как передать произвольное
    количество каких-то аргументов, без привязки к позиции? *args мне в даном случае не помогло, чувствуется пробел в
    знаниях у меня. И ксати спасибо за курс, у вас хорошо получается доносить информацию.
    Дополнительно. Как определить переменную которая только будет передана в функцию?
    '''

    if prod_name is not None:
#    if kwargs is getattr(prod_name):
#    if kwargs == prod_name:
        os_prod_list = re.findall(regex_name, prod_name)
        return os_prod_list
    elif os_name is not None:
#    if kwargs is getattr(os_name):
        os_name_list = re.findall(regex_name, os_name)
        return os_name_list
    elif code_name is not None:
#    if kwargs is getattr(code_name):
        os_code_list = re.findall(regex_name, code_name)
        return os_code_list
    elif system_name is not None:
#    if kwargs is getattr(system_name):
        os_type_list = re.findall(regex_name, system_name)
        return os_type_list

#with open('./data/read.json') as fjson: # Просто чтение из файла
#    pp(json.load(fjson))

#def write_to_csv(file, prod_name=None, os_name=None, code_name=None, system_name=None):
#
#    '''
#    С данным заданием не справился. Не понимаю как передать в функцию нечто, чтобы передать дальше,
#    в следующую функцию.
#    '''
#
#    DATA = [
#            [get_data(prod_name)],
#            [get_data(os_name)],
#            [get_data(code_name)],
#            [get_data(system_name)]
#            ]
#
#    with open(file, 'r+') as list:
#        writer = csv.writer(list)
#        for row in DATA:
#            writer.writerow(row)

for i in spisok:
    with open(i, encoding="cp1251") as fcsv:
        for line in fcsv.readlines():
            if os_prod_list in line:
#                print(get_data(**{'prod_name': 'line'}))
                print(get_data(prod_name=line))
#                print(write_to_csv('./data/read.csv', prod_name=line))
            elif os_name_list in line:
#                print(get_data(**{'os_name': 'line'}))
                print(get_data(os_name=line))
#                print(get_data('./data/read.csv', os_name=line))
            elif os_code_list in line:
#                print(get_data(**{'code_name': 'line'}))
                print(get_data(code_name=line))
#                print(get_data('./data/read.csv', code_name=line))
            elif os_type_list in line:
#                print(get_data(**{'system_name': 'line'}))
                print(get_data(system_name=line))
#                print(get_data('./data/read.csv', system_name=line))

