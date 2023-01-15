from classes import *

class Sistema:
    def __init__(self):
        self.gerentes = []  # Lista com todos os gerentes criados
        self.consultores = []  # Lista com todos os consultores criados
        self.projetos = []  # Lista com todos os projetos criados
        self.usuario_atual = usuario_base('None','None','None') #acessível apenas após login, portanto não precisa ser trancado (a ideia é que, ao fazer login o objeto referente ao usuario logado fique aqui e todas as alterações sejam feitas por aqui e depois salvas no objeto original)

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
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p.replace(' ', '').lower() in list:
            print(f'Removido {self.projetos[list.index(p)].nome}')
            self.projetos.pop(list.index(p))
            
        else:
            print('Entrada inválida')

    def definir_senha(self):
        senha1 = 1
        senha2 = 2
        while senha1 != senha2:
            senha1 = input('Insira a senha de login: ')
            senha2 = input('Confirme a senha: ')
            if senha1 != senha2:
                print('As senhas não são iguais. Tente novamente.')
        return senha1

    def criar_consultor(self):
        nome_con = input('Insira o nome do consultor: ')
        user_con = input('Insira o usuário de login: ')
        senha = self.definir_senha()
        con = Consultor(nome_con, user_con,senha)
        self.consultores.append(con)

    def remover_consultor(self):
        list = []
        for i in self.consultores:
            list.append(i.nome)
        p = input(f'Escolha o consultor que quer remover: {" | ".join(list)}\n')
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p.replace(' ', '').lower() in list:
            print(f'Removido {self.consultores[list.index(p)].nome}')
            self.consultores.pop(list.index(p))
        else:
            print('Entrada inválida')

    def criar_gerente(self):
        nome_ger = input('Insira o nome do gerente: ')
        user_ger = input('Insira o usuário de login: ')
        senha = self.definir_senha()
        ger = Gerente(nome_ger, user_ger,senha)
        self.gerentes.append(ger)

    def remover_gerente(self):
        list = []
        for i in self.gerentes:
            list.append(i.nome)
        p = input(f'Escolha o gerente que quer remover: {" | ".join(list)}\n')
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p.replace(' ', '').lower() in list:
            print(f'Removido {self.gerentes[list.index(p)].nome}')
            self.gerentes.pop(list.index(p))
        else:
            print('Entrada inválida')

    def listar(self):
        resp = input('O que você deseja listar?\n Gerentes | Consultores | Projetos\n')
        match resp.lower().strip():
            case ['gerentes', True]:
                list = []
                for i in self.gerentes:
                    list.append(i.nome)
                p = input(f'Escolha o gerente que quer ver: {" | ".join(list)}\n')
                for i in range(len(list)):
                    list[i] = list[i].replace(' ', '').lower()
                if p.replace(' ', '').lower() in list:  
                    obj = self.gerentes[list.index(p)]
                    print(obj)
                else:
                    print('Entrada inválida')

            case ['consultores', True]:
                list = []
                for i in self.consultores:
                    list.append(i.nome)
                p = input(f'Escolha o consultor que quer ver: {" | ".join(list)}\n')
                for i in range(len(list)):
                    list[i] = list[i].replace(' ', '').lower()
                if p.replace(' ', '').lower() in list:  
                    obj = self.consultores[list.index(p)]
                    print(obj)
                else:
                    print('Entrada inválida')

            case ['projetos', True]:
                list = []
                for i in self.projetos:
                    list.append(i.nome)
                p = input(f'Escolha o projeto que quer ver: {" | ".join(list)}\n')
                for i in range(len(list)):
                    list[i] = list[i].replace(' ', '').lower()
                if p.replace(' ', '').lower() in list:
                    obj = self.projetos[list.index(p)]
                    print(obj)
                else:
                    print('Entrada inválida')

            case _:
                print('Entrada inválida')

    def  logar(self):
        """ procurar na lista pelo nome do usuário e ver se a senha bate """
        """ após isso alocar em uma variável(self.usurario_atual) o objeto e liberar as opções novas para consultor e gerente"""
        c = input('Escolha como quer logar: Consultor | Gerente\n')
        user = input('Insira o nome de usuário: ')
        senha = input('Insira a senha de usuário: ')
        if c.lower() == 'consultor':
            lista = self.consultores
        if c.lower() == 'gerente':
            lista = self.gerentes
        for i in lista:
            if i.usuario == user and i.senha == senha:
                self.usuario_atual = i
                print('Login efetuado!\n')
                break
            elif i == lista[len(lista)-1]:
                print('Usuário ou senha invalido!\n')


    """ Funções para usuário logado """
    """ Gerais """
    def ver_dados(self):
        pass

    def modificar_dados(self):
        pass

    def ver_proj_alocados(self):
        pass


def main():
    sis = Sistema()
    sis.welcome()
    escolha = ''
    while escolha.lower().strip() != 'sair':
        if sis.usuario_atual.tipo == 'Consultor':
            logado = True
            escolha = input(opcoes_basicas + opcoes_comuns + opcoes_consultor)
        elif sis.usuario_atual.tipo == 'Gerente':
            logado = True
            escolha = input(opcoes_basicas + opcoes_comuns + opcoes_gerente)
        else:
            logado = False
            escolha = input(opcoes_basicas)
        
        match[ escolha.replace(' ', '').lower(),logado]:
            case ['criarprojeto', False | True]:
                sis.criarprojetos()
            case ['removerprojeto', False | True]:
                sis.removerprojetos()
            case ['criarconsultor', False | True]:
                sis.criar_consultor()
            case ['removerconsultor', False | True]:
                sis.remover_consultor()
            case ['criargerente', False | True]:
                sis.criar_gerente()
            case ['removergerente', False | True]:
                sis.remover_gerente()
            case ['fazerlogin', False | True]:
                sis.logar()
            case ['listar', False | True]:
                sis.listar()
            case ['verificarprojetos', True]:
                pass
            case ['vernome', True]:
                pass
            case ['alterarnome', True]:
                pass
            case ['verusuario' | 'verusuário', True]:
                pass
            case ['alterarusuario' | 'alterarusuário', True]:
                pass
            case ['alterarsenha', True]:
                pass
            case ['gerenciarpedidosdeavanço', True]:
                pass
            case ['gerenciarpedidosderetirada', True]:
                pass
            case ['passaroprojetoaoutrogerente', True]:
                pass
            case ['entregarumprojeto', True]:
                pass
            case ['requisitaravançodeetapa', True]:
                pass
            case ['pedirretiradadoprojeto', True]:
                pass
            case ['sair', False | True]:
                escolha = 'sair'
                print('Adeus!')
            case _:
                print('Entrada inválida')

if __name__ == '__main__':
    main()