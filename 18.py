'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
 В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5'''

n = int(input("Введите количество элементов в списке: "))
a = [int(input(f"Введите {i+1} элемент массива: ")) for i in range(n)]
x = int(input("Введите число х: "))
min_delta = abs(x - a[0])
nearest_number_index = 0
for i in range(1, n):
    delta = abs(x - a[i])
    if delta < min_delta:
        min_delta = delta
        nearest_number_index = i
print(f'Ближайшее число к {x} - {a[nearest_number_index]}')