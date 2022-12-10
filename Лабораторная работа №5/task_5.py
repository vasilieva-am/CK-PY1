import string
from random import sample
def get_random_password(n=8) -> str:
    list_alfabet = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits)
    return "".join(sample(list_alfabet, n))

print(get_random_password())

