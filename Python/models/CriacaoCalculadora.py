class Calculadora:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def pegar_valores(self):
        while True:
            try:
                self.num1 = float(input('Primeiro valor: '))
                self.num2 = float(input('Segundo valor: '))
                break
            except ValueError:
                print("Erro! Digite apenas números.")

    def rodar_calculadora(self):
        print('-' * 20)
        print('Bem-vindo ao programa da Calculadora')
        print('-' * 20)

        self.pegar_valores()

        while True:
            print('\n[1] somar')
            print('[2] diminuir')
            print('[3] divisão')
            print('[4] multiplicar')
            print('[5] todas operações')
            print('[6] trocar valores')
            print('[0] sair')

            escolha = input("\nEscolha: ")

            match escolha:
                case "1":
                    self.somar()
                case "2":
                    self.diminuir()
                case "3":
                    self.divi()
                case "4":
                    self.mult()
                case "5":
                    self.somar()
                    self.diminuir()
                    self.divi()
                    self.mult()
                case "6":
                    self.pegar_valores()
                case "0":
                    print('Fim.')
                    break
                case _:
                    print('Opção inválida.')

    def somar(self):
        print(f'{self.num1} + {self.num2} = {self.num1 + self.num2}')

    def diminuir(self):
        print(f'{self.num1} - {self.num2} = {self.num1 - self.num2}')

    def divi(self):
        if self.num2 != 0:
            print(f'{self.num1} / {self.num2} = {self.num1 / self.num2}')
        else:
            print('Erro: divisão por zero!')

    def mult(self):
        print(f'{self.num1} x {self.num2} = {self.num1 * self.num2}')

