# 3'. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.


spisok = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {spisok}")
new_spisok = []
[new_spisok.append(i) for i in spisok if i not in new_spisok]
print(f"Список из неповторяющихся элементов: {new_spisok}")