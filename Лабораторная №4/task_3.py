def delete(list_, index=None):
    if index == None:
        end_list = list_[:-1]
    else:
        _ = index+1
        end_list = list_[:index] + list_[_:]

    return end_list


print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]

