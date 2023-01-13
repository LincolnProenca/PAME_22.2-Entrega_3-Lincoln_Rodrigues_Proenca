from classes import *

class Sistema:
    def __init__(self):
        self.gerentes = []
        self.consultores = []
        self.projetos = []

    def welcome(self):
        print('Bem vindo ao sistema de ornaginzação e planejamento')

    """ Funções para usuário não logado """
    def criar_projetos(self):
        pass
    
    def remover_projetos(self):
        pass

    def criar_consultor(self):
        pass

    def remover_consultor(self):
        pass

    def criar_gerente(self):
        pass

    def remover_gerente(self):
        pass

    def listar(self):
        resp = input('O que você deseja listar?\n Gerentes | Consultores | Projetos\n')
        match resp:
            case 'Gerentes':
                pass
            case 'Consultores':
                pass
            case 'Projetos':
                pass
            case _:
                print('Entrada inválida')

    """ Funções para usuário logado """
    """ Gerais """
    def ver_dados(self):
        pass

    def modificar_dados(self):
        pass

    def ver_proj_alocados(self):
        pass


            


sis = Sistema()
sis.welcome()
escolha = ''
while escolha.tolower() != 'sair':
    escolha = input('Escolha o que quer fazer: Criar projeto | Remover Projeto | Criar Consultor | Remover Consultor | Criar Gerente | Remover Gerente | Listar | Sair\n ')
    
    match escolha.replace(' ', '').tolower():
        case 'criarprojeto':
            pass
        case 'removerprojeto':
            pass
        case 'criarconsultor':
            pass
        case 'removerconsultor':
            pass
        case 'criargerente':
            pass
        case 'removergerente':
            pass
        case 'listar':
            pass
        case 'sair':
            escolha = 'sair'
        case _:
            print('Entrada inválida')
