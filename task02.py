# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Введите натуральное число: "))
list_factorial = []
factorial = 1
for i in range(1, number + 1):
    factorial *=i
    list_factorial.append(factorial)
print(list_factorial)