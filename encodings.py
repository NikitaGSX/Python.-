#!/usr/bin/python
# coding: utf-8

"""
Данный способ комментирования применяется в описниях функций.
Здесь же я хотел указать, что поменял кодирвку скрипта на utf-8. Возможно не точно понял задание.
А также указать сайт https://repl.it/languages/python3, его я использовал в качестве онлайн конструктора.
"""
# 1.

first = 'разработка'
second = 'сокет'
third = 'декоратор'

print(type(first),type(second),type(third)) # Здесь у меня возникли сложности с переносом сторк, подстановка \n вызывает ошибку при выполнении. Нужно внимательнее ознакомится с синтаксисом print()

# 2.

b = type(b'function')
c = type(b'method')

print(type(b'class'))
print(b)
print(c)

# 3. Невозможно записать в байтовом типе type без кавычек, так как это будет модуль type(). В данном примере все слова это строки и их возможно записать в байтовом типе.

at = 'attribute'
cl = 'класс'
fu = 'функция'
ty = 'type'

print(type(b'at'))
print(type(b'cl'))
print(type(b'fu'))
print(type(b'ty'))

# 4.

one = 'разработка'
two = 'администрирование'
three = 'protocol'
four = 'standard'

bone = one.encode()
btwo = two.encode()
bthree = three.encode()
bfour = four.encode()

print(bone.decode())
print(btwo.decode())
print(bthree.decode())
print(bfour.decode())

