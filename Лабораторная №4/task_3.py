def delete(list_, index=None):
    if index is None or index == -1:
        end_list = list_[:-1]
    else:
        end_list = list_[:index] + list_[index+1:]
    return end_list

print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]

