list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0
max_number = list_numbers[max_index]  # Пусть первое число в списке будет максимальным

for i, current_number in enumerate(list_numbers):  # Перебираем каждое число из списка
    max_number = list_numbers[max_index]
    if current_number >= max_number:  # Если текущее число, больше или равно максимальному, то
        max_index = i  # то перезапишем индекс для максимального последнего числа
        max_number = current_number  # и перезапишем последнее максимальное число


list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]

