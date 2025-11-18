class Tabuada:
    def __init__(self):
        self.num = 0
    
    def gerar_valores(self):
        while True:
            try:
                self.num = int(input('Escolha um número para começar a tabuada :'))
                break
            except ValueError:
                print('Erro !')
                continue
        
    def tab(self):
        for i in range(0 , 11):
            print(f'{self.num} x {i} = {self.num*i}')
    
    def rodar_tabuada(self):
        print('-'*10)
        print('Menu da Tabuada')
        print('-'*10)
        self.gerar_valores()
        while True:
            print('[1] Começar')
            print('[2] Trocar os valores')
            print('[3] Fechar')
            x = input('\nEscolha :')

            match x:
                case "1":
                    self.tab()
                case "2":
                    self.gerar_valores()
                case "3":
                    print('Fechando ...')
                    break
                case _:
                    print('Desconhecido')