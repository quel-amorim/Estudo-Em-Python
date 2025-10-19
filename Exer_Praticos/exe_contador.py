#Contador
import time
contagem = 0
qts = int(input('Contar até quando ?'))
for i in range(qts):
    print(contagem + i)
    time.sleep(0.5)

print('\n / Fim da contagem ! /')
