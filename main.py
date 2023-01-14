from classes import *

class Sistema:
    def __init__(self):
        self.gerentes = []  # Lista com todos os gerentes criados
        self.consultores = []  # Lista com todos os consultores criados
        self.projetos = []  # Lista com todos os projetos criados
        self.usuario_atual = None #acessível apenas após login, portanto não precisa ser trancado (a ideia é que, ao fazer login o objeto referente ao usuario logado fique aqui e todas as alterações sejam feitas por aqui e depois salvas no objeto original)

    def welcome(self):
        print('Bem vindo ao sistema de ornaginzação e planejamento \n')

    """ Funções para usuário não logado """
    def criarprojetos(self):
        nome_proj = input('Insira o nome do projeto: ')
        coor_proj = input('Insira a coordenação do projeto: ')
        etp_proj = int(input('Insira a etapa do projeto (0-15): '))
        cst_proj = input('Insira o nome do consultor do projeto: ')
        grt_proj = input('Insira o nome do gerente do projeto: ')
        proj = Projeto(nome_proj, coor_proj, etp_proj,cst_proj,grt_proj)
        self.projetos.append(proj)
    
    def removerprojetos(self):
        list = []
        for i in self.projetos:
            list.append(i.nome)
        p = input(f'Escolha o projeto que quer remover: {" | ".join(list)}\n')
        if p in list:
            self.projetos.pop(list.index(p))
        else:
            print('Entrada inválida')

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
        match resp.lower().strip():
            case 'gerentes':
                pass

            case 'consultores':
                pass

            case 'projetos':
                list = []
                for i in self.projetos:
                    list.append(i.nome)
                p = input(f'Escolha o projeto que quer ver: {" | ".join(list)}\n')
                if p in list:
                    obj = self.projetos[list.index(p)]
                    print(obj)
                else:
                    print('Entrada inválida')

            case _:
                print('Entrada inválida')

    def  logar(self):
        """ procurar na lista pelo nome do usuário e ver se a senha bate """
        """ após isso alocar em uma variável(self.usurario_atual) o objeto e liberar as opções novas para consultor e gerente"""
        pass

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
logado = False
while escolha.lower().strip() != 'sair':
    if sis.usuario_atual.tipo == 'Consultor':
        escolha = input('Escolha o que quer fazer: Criar projeto | Remover Projeto | Criar Consultor | Remover Consultor | Criar Gerente | Remover Gerente | Listar | Sair\n' + opcoes_comuns + opcoes_consultor)
    elif sis.usuario_atual.tipo == 'Gerente':
        escolha = input('Escolha o que quer fazer: Criar projeto | Remover Projeto | Criar Consultor | Remover Consultor | Criar Gerente | Remover Gerente | Listar | Sair\n' + opcoes_comuns + opcoes_gerente)
    else:
        escolha = input('Escolha o que quer fazer: Criar projeto | Remover Projeto | Criar Consultor | Remover Consultor | Criar Gerente | Remover Gerente | Listar | Sair\n')
    
    match escolha.replace(' ', '').lower():
        case 'criarprojeto':
            sis.criarprojetos()
        case 'removerprojeto':
            sis.removerprojetos()
        case 'criarconsultor':
            pass
        case 'removerconsultor':
            pass
        case 'criargerente':
            pass
        case 'removergerente':
            pass
        case 'listar':
            sis.listar()
        case 'sair':
            escolha = 'sair'
            print('Adeus!')
        case _:
            print('Entrada inválida')
