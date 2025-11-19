import json

class Perfil:
    def __init__(self):
        self.modelo_perfil = []
    
    def addPerfil(self):
        nome = input('Diga o nome que deseja aparecer no programa : ')
        email = input('Email de contato : ')
        texto = input('Diga alguma coisa sobre você : ')
        
        while True:
            try:
                x = int(input('Quantas habilidades você tem? '))
                break
            except ValueError:
                print('Erro! Digite um número.')
        
        habilidades = []

        for _ in range(x):
            soft = input('Habilidade : ')
            skill = input('[1] Básico\n[2] Intermediário\n[3] Avançado\n[4] Pouco Conhecimento\nDiga seu nível : ')
            

            habilidades.append({
                "soft": soft,
                "skill": skill
            })

        dados = {
            "nome": nome,
            "email": email,
            "texto": texto,
            "habilidades": habilidades
        }

        self.modelo_perfil.append(dados)
        print('Dados colocados!')

    def salvar_json(self):
        if not self.modelo_perfil:
            print('Não há nada na lista.')
        else:
            with open('perfil.json', 'w') as arquivo:
                json.dump(self.modelo_perfil, arquivo, indent=4)
            print("Arquivo salvo!")

    def exibir(self):
        if not self.modelo_perfil:
            print("Nenhum perfil cadastrado ainda.")
            return
        
        print("\n=== Perfis cadastrados ===")
        for perfil in self.modelo_perfil:
            print(f"\nNome: {perfil['nome']}")
            print(f"Email: {perfil['email']}")
            print(f"Sobre: {perfil['texto']}")
            print("Habilidades:")
            
            for h in perfil["habilidades"]:
                print(f"  - {h['soft']} (Nível: {h['skill']})")
            
            print("-" * 40)
    
    def menu_perfil(self):
        print('-=-'*10)
        print('Menu de Criação de Perfil')
        print('-=-'*10)
        while True:
            print('[1] Criar')
            print('[2] Salvar')
            print('[3] Exibir')
            print('[4] Sair')

            op = input('\nEscolha :')

            match op:
                case "1":
                    self.addPerfil()
                case "2":
                    self.salvar_json()
                case "3":
                    self.exibir()
                case "4":
                    print('--- Fechando ---')
                    break
                case _:
                    print('Erro !')
                    continue