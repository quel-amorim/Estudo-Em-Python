from datetime import datetime,timedelta
from random import choice
data = datetime.now()
sugestoes_topicos = ['Fundamentos de controle','Controle de Dados','Criação de CRUDS','Lógica de Algoritmos']
tempoLimite = data + timedelta(days=14)
topicos = choice(sugestoes_topicos)

print(f'Dia {data.strftime("%d/%m/%y")} até {tempoLimite.strftime("%d/%m/%y")}\nTópico de Estudo: {topicos}')