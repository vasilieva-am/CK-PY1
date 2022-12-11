from string import ascii_lowercase,ascii_uppercase,digits
from random import sample
def get_random_password(n=8) -> str:
    alfabet = ascii_lowercase + ascii_uppercase + digits
    return "".join(sample(alfabet, n))

print(get_random_password())

