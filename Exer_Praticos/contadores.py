from random import randint
from time import sleep
def roleta_números():
    numeros_pares = 0 # quantos números pares aparecem no código
    numeros_impares = 0 # números de vezes que aparece os impares
    pares = []
    impares = []
    qts = int(input("X vezes que vai criar números ? "))
    for i in range(1 , qts+1):
        roleta = randint(0 , 1000)
        if roleta % 2 == 0:
            numeros_pares +=1
            pares.append(roleta)
        else:
            numeros_impares +=1
            impares.append(roleta)
    
    print(f"N PARES : {numeros_pares}")
    print(f"N IMPAR : {numeros_impares}")
    sleep(1)
    
    print(f"\n=== / Lista PAR / === \n{pares}")
    print(f"\n=== / Lista IMPAR / === \n{impares}")


roleta_números()