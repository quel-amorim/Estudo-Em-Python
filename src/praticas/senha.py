from random import choice
from string import ascii_letters , octdigits,punctuation

caracteres = ascii_letters + octdigits + punctuation
for i in range(3):
    senha = ''.join(choice(caracteres) for _ in range(16))
    print(i,'->' , senha)