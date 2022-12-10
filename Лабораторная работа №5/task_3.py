import random
def get_unique_list_numbers() -> list[int]:
    list_size = 15
    l = []
    while len(l) < list_size:
        list_ = list(set(random.randint(-10, 10) for num in range(list_size)))
        break
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
