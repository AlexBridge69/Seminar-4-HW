print("Задача 1")
print(
    "Создать и заполнить файл случайными целыми значениями. \n"
    "Выполнить сортировку содержимого файла по возрастанию."
)

import random


def sort(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0:
            if value < list[i]:
                list[i + 1] = list[i]
                list[i] = value
                i -= 1
            else:
                break


with open('file.txt', 'w') as insert_data:
    for i in range(20):
        insert_data.writelines(str(random.randint(0, 100)))
        insert_data.writelines('\n')

number_list = []

with open('file.txt', 'r') as import_data:
    number_list = import_data.readlines()

# Сортировка списка неработает с элементами типа "str", поэтому переводим элементы в тип "int".
for i, item in enumerate(number_list):
    number_list[i] = int(item)

sort(number_list)

with open('file.txt', 'a') as return_data:
    return_data.write("Отсортированный список: \n")
    for i in number_list:
        return_data.write(str(i) + '\n')

print("Исходный список и результат сортировки записаны в файле 'file.txt'.")

print("Задача 2")
print(
    "Дан список чисел. Создать список в который попадают числа, \n"
    "описывающие возрастающую последовательность \n"
    "и содержащие максимальное количество элементов."
)

# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]

'''
1. Собираем последовательности от самого младшего и самого старшего элемента главного списка.
2. Заносим их в отдельные списки. Чтобы не путаться, всё связанное со списком от старшего индекса имеет приписку "reverse".
3. Ищем самую большую последовательность в каждом списке.
4. Все элементы одного списка, которых нет во втором списке переносим во второй список.
5. Сортируем полученный список.
6. Результат в консоли.
'''


def get_list_from_low(in_list, index_of_start_low):
    list_from_low = list()
    start_element = in_list[index_of_start_low]
    list_from_low.append(start_element)
    for i in range(index_of_start_low, len(in_list)):
        if start_element < in_list[i]:
            list_from_low.append(in_list[i])
            start_element = in_list[i]
    return list_from_low


def get_list_from_high(in_list, index_of_start_high):
    list_from_high = list()
    start_element = in_list[index_of_start_high]
    list_from_high.append(start_element)
    for i in range(index_of_start_high, -1, -1):
        if start_element > in_list[i]:
            list_from_high.append(in_list[i])
            start_element = in_list[i]
    return list_from_high


def get_list_of_lengths(in_list):
    list_of_lengths = list()
    for i in range(len(in_list)):
        list_of_lengths.append(len(in_list[i]))
    return list_of_lengths


def get_index_of_max_length(in_list):
    index_of_max_length = 0
    for i in range(len(in_list)):
        if in_list[i] > in_list[index_of_max_length]:
            index_of_max_length = i
    return index_of_max_length


original_list = [1, 5, 2, 3, 4, 6, 1, 7]
length_of_original_list = len(original_list)
print(original_list)

list_of_sub_lists = list()
list_of_sub_lists_in_reverse = list()

for i in range(length_of_original_list):
    list_of_sub_lists.append(get_list_from_low(original_list, i))
for i in range(length_of_original_list - 1, -1, -1):
    list_of_sub_lists_in_reverse.append(get_list_from_high(original_list, i))

list_of_lengths = get_list_of_lengths(list_of_sub_lists)
list_of_lengths_reverse = get_list_of_lengths(list_of_sub_lists_in_reverse)

index_of_max_length = get_index_of_max_length(list_of_lengths)
index_of_max_length_reverse = max_length_reverse = get_index_of_max_length(list_of_lengths_reverse)

list_1 = list_of_sub_lists[index_of_max_length]
list_2_reverse = list_of_sub_lists_in_reverse[index_of_max_length_reverse]

for i in range(len(list_1)):
    if list_1[i] not in list_2_reverse:
        list_2_reverse.append(list_1[i])

# Функцуия сортировки взята из этого же файла, но из прошлой задачи.

sort(list_2_reverse)
print(list_2_reverse)
