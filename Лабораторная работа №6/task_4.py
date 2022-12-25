import json

INPUT_FILE = "input1.csv"

def csv_to_list_dict(INPUT_FILE, delimiter=',', new_line='\n'):
    with open(INPUT_FILE, "r") as f:
        heads = f.readline()[:-1].split(delimiter)
        values = [i[:-1].split(delimiter) for i in f.readlines()]

    return [dict(zip(heads, values[j])) for j in range(len(values))]



print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
