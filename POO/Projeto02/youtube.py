class Canal:
    def __init__(self,nome,inscritos=1):
        self.nome = nome
        self.inscritos = inscritos

    def __repr__(self):
        return f' YT : {self.nome}  N:{self.inscritos}'

p1 = Canal('Programador Web',20000)
p2 = Canal('Engenheiro de Software',9999999)

print(p1)
print(p2)