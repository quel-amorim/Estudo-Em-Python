from models.CriacaoCalculadora import Calculadora
from models.CriacaoTabuada import Tabuada
from models.ProdutosCriados import Produto
from models.Curriculo import Perfil
from models.CriacaoMenuCafe import Categoria
from models.Tarefas import Tarefa
from models.Jogo_Adivinha import Adivinha 
print('-'*50)
print('Bem-vindo ao Menu de Programas já feitos em Python')
print('-'*50)
print('Escolha qual programa deseja testar :')
print('[1] Calculadora')
print('[2] Tabuada')
print('[3] Programa de Produtos')
print('[4] Criar curriculo')
print('[5] Catégorias')
print('[6] Tarefas')
print('[7] Jogo de Adivinhar')
p = int(input('Vamos ver o ... :'))
if p == 1:
    Calculadora().menu()
elif p == 2:
    Tabuada().rodar_tabuada()
elif p == 3:
    Produto().menu_produtos()
elif p == 4:
    Perfil().menu_perfil()
elif p == 5:
    Categoria().menu()
elif p == 6:
    Tarefa().menu()
elif p == 7:
    Adivinha().MenuPrograma()
