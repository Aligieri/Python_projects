'''
Удалите входной элемент из списка 3-мя способами. Определите самый быстрый.
Input: элемент введеный с клавиатуры(число)
Output: список с элементами, список без введенного элемента, скорость выполнения(в миллисекундах)
Примечание: Используйте заполнение списка случайно сгенерированными числами с диапазоном(например от 0 до 9)
'''

import random
import time

main_list = []
element_index = 0

elements_count = int(input("Введите количество элементов в списке\n"))

for i in range(elements_count):
    main_list.insert(i, random.randint(0, 9))

print("Список сгенерирован из ", elements_count, " элементов\n")
print("Первичный список", main_list)

deleteNum = int(input("Введите элемент для удаления\n"))
start_time = time.time()

main_list_copy1 = main_list.copy()

while element_index <= elements_count - 1:
    if deleteNum == main_list_copy1[element_index]:
        print("Удаляем", main_list_copy1[element_index],  "на позиции", element_index)
        del main_list_copy1[element_index]
        elements_count -= 1
    else:
        element_index += 1

print("Список после выполнения операции:", main_list_copy1)
linear_search_time = time.time() - start_time
print("Время операции методом линейного поиска", linear_search_time, "секунд")
