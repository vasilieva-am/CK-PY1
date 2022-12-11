from random import randint
def get_unique_list_numbers(start = -10, end = 10, list_size = 15) -> list[int]:
    list_numbers = []
    while len(list_numbers) < list_size:
        number = randint(start, end)
        if number not in list_numbers:
            list_numbers.append(number)

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

