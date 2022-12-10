# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
list_dictionary = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(0, 16)]

pprint(list_dictionary)