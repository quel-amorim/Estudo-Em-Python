from random import randint
from time import sleep

print('A Sorte está escolhendo qual número será sua tabuada')
num = randint(0 , 1000)
sleep(1)
print('Sorte escolhendo ...')
sleep(0.5)
print('...')
sleep(0.9)
print('..')
sleep(1)
print('\n=== / Tabuada do {} / ==='.format(num))
for i in range(0 , 11):
    print(f'{num} x {i} = {num*i}')

print('\n=== / Fim / ===')
