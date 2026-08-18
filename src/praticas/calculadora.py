"""Calculadora focada em variáveis, condições, loops, funções e dicionários."""
class Calculadora:
    def __init__(self):
        self.historico = []
        self.n1 = 0
        self.n2 = 0

    def coletar_variaveis(self):
        while True:
            try:
                self.n1 = float(input('1° valor: '))
                self.n2 = float(input('2° valor: '))
                break
            except ValueError:
                print('Valor incorreto! Digite apenas números.')

    def salvar_historico(self, operacao):
        self.historico.append(operacao)

    def somar(self):
        operacao = f'{self.n1} + {self.n2} = {self.n1+self.n2}'
        print(operacao)
        self.salvar_historico(operacao)

    def diminuir(self):
        operacao = f'{self.n1} - {self.n2} = {self.n1 - self.n2}'
        print(operacao)
        self.salvar_historico(operacao)

    def dividir(self):
        if self.n2 == 0:
            print('Não é possível dividir por zero!')
            return
        operacao = f'{self.n1} / {self.n2} = {self.n1 / self.n2}'
        print(operacao)
        self.salvar_historico(operacao)

    def multiplicar(self):
        operacao = f'{self.n1} * {self.n2} = {self.n1 * self.n2}'
        print(operacao)
        self.salvar_historico(operacao)

    def mostrar_historico(self):
        if not self.historico:
            print('Nenhuma operação realizada!')
            return

        print('\nHistórico de operações:')
        for numero, operacao in enumerate(self.historico, start=1):
            print(f'{numero}. {operacao}')

    def iniciar(self):
        self.coletar_variaveis()
        operacoes = {
            1: self.somar,
            2: self.diminuir,
            3: self.dividir,
            4: self.multiplicar
        }

        while True:
            print('\n' + '~-~' * 20)
            print('Opções de operações')
            print('1. Somar')
            print('2. Diminuir')
            print('3. Dividir')
            print('4. Multiplicar')
            print('5. Todas')
            print('6. Histórico')
            print('7. Trocar valores')
            print('0. Voltar ao menu inicial')

            try:
                escolha = int(input('Escolha: '))
            except ValueError:
                print('Digite apenas um número!')
                continue

            if escolha in operacoes:
                operacoes[escolha]()

            elif escolha == 5:
                for operacao in operacoes.values():
                    operacao()

            elif escolha == 6:
                self.mostrar_historico()

            elif escolha == 7:
                self.coletar_variaveis()

            elif escolha == 0:
                break

            else:
                print('Opção inválida!')

    def menu_inicial(self):
        while True:
            print('\n' + '~-~' * 10)
            print('Projeto Calculadora')
            print('~-~' * 10)
            print('1. Começar')
            print('2. Trocar variáveis')
            print('0. Sair')
            try:
                escolha = int(input('Escolha:'))
            except ValueError:
                print('Digite apenas um número!')
                continue

            if escolha == 1:
                self.iniciar()

            elif escolha == 2:
                self.coletar_variaveis()

            elif escolha == 0:
                print('Encerrando o programa...')
                break

            else:
                print('Opção inválida!')


def main():
    rodar = Calculadora()
    rodar.menu_inicial()


if __name__ == '__main__':
    main()
