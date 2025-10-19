from random import randint

def gerador_telefone():
    ddd = randint(11 , 99)
    cell = randint(0 , 999999999)
    completo = f'+55 ({ddd:02d}) 9{cell:08d}'
    print(completo)
    print(f'Digitos total : {len(str(completo))}')

gerador_telefone()