from random import randint
def get_unique_list_numbers() -> list[int]:
    list_numbers = []
    list_size = 15
    while len(list_numbers) < list_size:
        number = randint(-10, 10)
        if number not in list_numbers:
            list_numbers.append(number)
    return list_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

