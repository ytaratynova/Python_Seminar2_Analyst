# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.

import random

def InputPosition(q_p):
    position = []
    for i in range(q_p):
        position.append(int(input(f'введите позицию {i+1} элемента из списка, произведение которых вы хотите найти от 0 до {number - 1}: ')))
    return position

def Composition(list_position, number_list):
    compos = 1
    for i in range(len(list_position)):
        compos *=number_list[list_position[i]]
    return compos

my_list = []

number = int(input("Введите натуральное число: "))
print(f'Ваш случайный список из {number} элементов в диапазое [{-1*number},{number}]:')
for i in range(number):
    my_list.append(random.randint(-number, number))
print(my_list)

quantity_position = int(input(f"введите натуральное число - количество элементов списка, произведение которых вы хотите найти от 1 до {number}: "))
list_of_positions = InputPosition(quantity_position)

print(f'Произведение элементов на позициях {list_of_positions}: {Composition(list_of_positions, my_list)}')






