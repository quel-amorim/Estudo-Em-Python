"""Programa consiste pegar um número inteiro e converter em °C , °F , metros para quilometro.Outra parte é gerar um
valor aleatoria e converte o valor para dolar e real"""
from random import randint, uniform
import requests
# Variáveis aleatórias
numero = randint(0, 40)
moeda = round(uniform(1, 100), 2)

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

try:
    # Fazendo a requisição
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json() # Transformando a resposta em dicionário
    cotacao_dolar = float(dados["USDBRL"]["bid"])  # Pegando a cotação atual do dólar
    convertido = moeda * cotacao_dolar

    print(f"Valor aleatório: US$ {moeda:.2f}")
    print(f"Cotação do dólar: R$ {cotacao_dolar:.2f}")
    print(f"Valor convertido: R$ {convertido:.2f}")

except requests.exceptions.RequestException as erro:
    print(f"Erro ao acessar a API: {erro}")

fahre = (numero * 1.8) + 32
quilometro = numero / 1000

print('\nCelsius ----- Fahrenheit')
print(numero , "°C" , '------' , fahre, "°F")
print()
print('\nMetros --- Quilometros')
print(numero ,"metros" , '-----' , quilometro,"quilometros")
