class Calculadora:
    def __init__(self):
        self.H = []
    
    def valores(self):
        while True:
            try:
                self.n1 = float(input('1 ° número :'))
                self.n2 = float(input('2 ° número :'))
                break
            except ValueError:
                print('Erro de digitação !')
                continue
    
    def atralhos(self):
        print('[1] Somar')
        print('[2] Subtrair')
        print('[3] Divisão')
        print('[4] Multiplicação')
        print('[5] Trocar valores')
        print('[6] Todas operações')
        print('[0] Sair')
    
    def somar(self):
        r = self.n1 + self.n2
        print(f'{self.n1} + {self.n2} = {r}')
        return r

    def sub(self):
        r = self.n1 - self.n2
        print(f'{self.n1} - {self.n2} = {r}')
        return r
    
    def div(self):
        if self.n2 == 0:
            print('Divisão por zero !')
        else:
            r = self.n1 / self.n2
            print(f'{self.n1} / {self.n2} = {r}')
            return r
    
    def mult(self):
        r = self.n1 * self.n2
        print(f'{self.n1} x {self.n2} = {r}')
        return r
    
    def todas(self):
        print('\nTodas Operações')
        dados = {
        "Soma" : self.somar(),
        "Sub" : self.sub(),
        "Divisão" : self.div(),
        "Multiplicação" : self.mult()
        }
        self.H.append(dados)
        for _ , d in enumerate(self.H , start=1):
            print(d)
        
    def menu(self):
        print('-=-'*10)
        print('Menu do Programa Calculadora')
        print('-=-'*10)
        self.valores() # pegar valores antes de começar as operaçoes
        print('OPERAÇÕES REGISTRADAS')
        print('-'*10)
        while True:
            self.atralhos() # atralhos registrados
            escolha = input('Escolha :')
            
            match escolha:
                case "1":
                    self.somar()
                case "2":
                    self.sub()
                case "3":
                    self.div()
                case "4":
                    self.mult()
                case "5":
                    self.valores()
                case "6":
                    self.todas()
                case "0":
                    print('--- Fim ---')
                    break
