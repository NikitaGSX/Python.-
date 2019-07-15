#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
from pprint import pprint
import csv

os_prod_list    = 'Изготовитель системы'
os_name_list    = 'Название ОС'
os_code_list    = 'Код продукта'
os_type_list    = 'Тип системы'
spisok          = ["./data/info_1.txt", "./data/info_2.txt", "./data/info_3.txt"]

def get_data(prod_name=None, os_name=None, code_name=None, system_name=None):
    if prod_name is not None:
        os_prod_list = re.findall(r'Изготовитель системы:\s+(.+)', prod_name)
        return os_prod_list
    elif os_name is not None:
        os_name_list = re.findall(r'Название ОС:\s+(.+)', os_name)
        return os_name_list
    elif code_name is not None:
        os_code_name = re.findall(r'Код продукта:\s+(.+)', code_name)
        return os_code_list
    elif system_name is not None:
        os_type_list = re.findall(r'Тип системы:\s+(.+)', system_name)
        return os_type_list

#def write_to_csv(file, get_data()):
#    DATA = def get_data()
#    with open(file, r+) as list:
#        writer = csv.writer(list):
#            for row in DATA:
#                writer.writerow(row)

for i in spisok:
    with open(i, encoding="cp1251") as file:
        for line in file.readlines():
            if os_prod_list in line:
                prod_name = line
                print(get_data(prod_name))
            elif os_name_list in line:
                os_name = line
                print(get_data(os_name=os_name))
            elif os_code_list in line:
                code_name = line
                print(get_data(code_name=code_name))
            elif os_type_list in line:
                system_name = line
                print(get_data(system_name=system_name))

