from classes import *

class Sistema:
    def __init__(self):
        self.gerentes = []  # Lista com todos os gerentes criados
        self.consultores = []  # Lista com todos os consultores criados
        self.projetos = []  # Lista com todos os projetos criados
        self.projetos_finalizados = [] #Lista com todos os projetos finalizados
        self.usuario_atual = usuario_base('None','None','None') #acessível apenas após login, portanto não precisa ser trancado (a ideia é que, ao fazer login o objeto referente ao usuario logado fique aqui e todas as alterações sejam feitas por aqui e depois salvas no objeto original)

    def welcome(self):
        print('Bem vindo ao sistema de ornaginzação e planejamento \n')

    """ Funções para usuário não logado """
    def criarprojetos(self):
        nome_proj = input('Insira o nome do projeto: ')
        coor_proj = input('Insira a coordenação do projeto: ')
        try:
            etp_proj = int(input('Insira a etapa do projeto (0-15): '))
        except:
            print('\nO valor da etapa deve ser um inteiro entre 0 e 15! Tente novamente')
            return
        cst_proj = input('Insira o nome do consultor do projeto: ')
        grt_proj = input('Insira o nome do gerente do projeto: ')
        proj = Projeto(nome_proj, coor_proj, etp_proj,'','')
        """ Associando projetos a gerente e consultor """
        if self.consultores == []:
            print('\nConsultor não encontrado! Entre como o gerente do projeto para alocar um consultor\n')
        if self.gerentes == []:
            print('\nGerente não encontrado! Entre como um gerente para alocar-se ao projeto\n')
        for i in self.consultores:
            if i.nome.replace(' ', '').lower() == cst_proj.replace(' ', '').lower():
                i.projetos.append(proj)
                proj.nome_consultor = i.nome
                break
            elif i == self.consultores[len(self.consultores)-1]:
                print('\nConsultor não encontrado! Entre como o gerente do projeto para alocar um consultor\n')

        for i in self.gerentes:
            if i.nome.replace(' ', '').lower() == grt_proj.replace(' ', '').lower():
                i.projetos.append(proj)
                proj.nome_gerente = i.nome
                break
            elif i == self.gerentes[len(self.gerentes)-1]:
                print('\nGerente não encontrado! Entre como um gerente para alocar-se ao projeto\n')
        """ Adicionando projeto ao sistema """
        self.projetos.append(proj)
        
    def removerprojetos(self):
        list = []
        for i in self.projetos: # Gerando lista de projetos
            list.append(i.nome)
        p = input(f'Escolha o projeto que quer remover: {" | ".join(list)}\n')
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p.replace(' ', '').lower() in list: # Comparando a resposta com a lista
            nome = self.projetos[list.index(p.replace(' ', '').lower())].nome
            print(f'Removido {nome}')
            self.projetos.pop(list.index(p.replace(' ', '').lower()))
            
        else:
            print('\nEntrada inválida\n')

    def definir_senha(self): # Função para criar senhas
        senha1 = 1
        senha2 = 2
        while senha1 != senha2: # Loop para garantir que as senhas sejam iguais
            senha1 = input('Insira a senha de login: ')
            senha2 = input('Confirme a senha: ')
            if senha1 != senha2:
                print('As senhas não são iguais. Tente novamente.')
        return senha1

    def criar_consultor(self): # Função para criar consultor
        nome_con = input('Insira o nome do consultor: ')
        user_con = input('Insira o usuário de login: ')
        lista = self.consultores + self.gerentes
        for i in lista:
            if i.nome.replace(' ', '').lower() == user_con.replace(' ', '').lower():
                print('Nome de usuário já utilizado, tente outro!\n')
                return
        senha = self.definir_senha()
        con = Consultor(nome_con, user_con,senha)
        self.consultores.append(con)

    def remover_consultor(self): # Função para remover consultor
        list = []
        for i in self.consultores:
            list.append(i.nome)
        p = input(f'Escolha o consultor que quer remover: {" | ".join(list)}\n')
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p.replace(' ', '').lower() in list:
            nome = self.consultores[list.index(p.replace(' ', '').lower())].nome
            print(f'Removido {nome}')
            self.consultores.pop(list.index(p.replace(' ', '').lower()))
        else:
            print('\nEntrada inválida\n')

    def criar_gerente(self): # Função para criar gerente
        nome_ger = input('Insira o nome do gerente: ')
        user_ger = input('Insira o usuário de login: ')
        lista = self.consultores + self.gerentes
        for i in lista:
            if i.nome.replace(' ', '').lower() == user_ger.replace(' ', '').lower():
                print('Nome de usuário já utilizado, tente outro!\n')
                return
        senha = self.definir_senha()
        ger = Gerente(nome_ger, user_ger,senha)
        self.gerentes.append(ger)

    def remover_gerente(self): # Função para remover gerente
        list = []
        for i in self.gerentes:
            list.append(i.nome)
        p = input(f'Escolha o gerente que quer remover: {" | ".join(list)}\n')
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p.replace(' ', '').lower() in list:
            if self.gerentes[list.index(p.replace(' ', '').lower())].projetos == []:
                nome = self.gerentes[list.index(p.replace(' ', '').lower())].nome
                print(f'Removido {nome}')
                self.gerentes.pop(list.index(p.replace(' ', '').lower()))
            else:
                print('\nEsse gerente ainda possui projetos e não pode ser excluído\n')
        else:
            print('\nEntrada inválida\n')

    def listar(self): # Função para listar os diferentes tipos de objetos
        resp = input('O que você deseja listar?\n Gerentes | Consultores | Projetos\n')
        match resp.lower().strip():
            case 'gerentes': # Parte para listar gerentes
                list = []
                for i in self.gerentes:
                    list.append(i.nome)
                if list == []:
                    print('Escolha o gerente que quer ver: Nenhum gerente encontrado\n')
                    return
                p = input(f'Escolha o gerente que quer ver: {" | ".join(list)}\n')
                for i in range(len(list)):
                    list[i] = list[i].replace(' ', '').lower()
                if p.replace(' ', '').lower() in list:  
                    obj = self.gerentes[list.index(p.replace(' ', '').lower())]
                    lista = []
                    for i in obj.projetos:
                        lista.append(i.nome)
                    if lista == []:
                        lista = 'Nenhum projeto alocado'
                    else:
                        lista = " | ".join(lista)
                    print(f'''
                    Nome: {obj.nome}
                    Projetos: {lista}
                    Cargo : {obj.tipo}
                    ''')
                else:
                    print('\nEntrada inválida\n')

            case 'consultores': # Parte para listar consultores
                list = []
                for i in self.consultores:
                    list.append(i.nome)
                p = input(f'Escolha o consultor que quer ver: {" | ".join(list)}\n')
                if list == []:
                    print('Escolha o consultor que quer ver: Nenhum consultor encontrado\n')
                    return
                for i in range(len(list)):
                    list[i] = list[i].replace(' ', '').lower()
                if p.replace(' ', '').lower() in list:  
                    obj = self.consultores[list.index(p.replace(' ', '').lower())]
                    lista = []
                    for i in obj.projetos:
                        lista.append(i.nome)
                    if lista == []:
                        lista = 'Nenhum projeto alocado'
                    else:
                        lista = " | ".join(lista)
                    print(f'''
                    Nome: {obj.nome}
                    Projetos: {lista}
                    Cargo : {obj.tipo}
                    ''')
                else:
                    print('\nEntrada inválida\n')

            case 'projetos': # Parte para listar projetos
                list = []
                for i in self.projetos + self.projetos_finalizados:
                    list.append(i.nome)
                if list == []:
                    print('Escolha o projeto que quer ver: Nenhum projeto encontrado\n')
                    return
                p = input(f'Escolha o projeto que quer ver: {" | ".join(list)}\n')
                for i in range(len(list)):
                    list[i] = list[i].replace(' ', '').lower()
                if p.replace(' ', '').lower() in list:
                    if list.index(p.replace(' ', '').lower()) < len(self.projetos):
                        obj = self.projetos[list.index(p.replace(' ', '').lower())]
                    else:
                        obj = self.projetos_finalizados[list.index(p.replace(' ', '').lower()) - len(self.projetos)]
                    print(obj)
                else:
                    print('\nEntrada inválida\n')

            case _:
                print('\nEntrada inválida\n')

    def  logar(self):
        c = input('Escolha como quer logar: Consultor | Gerente\n')
        if c.lower() == 'consultor':
            lista = self.consultores
        elif c.lower() == 'gerente':
            lista = self.gerentes
        else:
            print('Escolha de tipo de login inválida')
            return
        if lista == []:
            print('Nenhum usuário encontrado')
            return
        user = input('Insira o nome de usuário: ')
        senha = input('Insira a senha de usuário: ')
        
        for i in lista:
            if i.usuario == user and i.senha == senha:
                self.usuario_atual = i
                print('Login efetuado!\n')
                break
            elif i == lista[len(lista)-1]:
                print('Usuário ou senha invalido!\n')

    """ Funções para usuário logado """
    """ Gerais """
    def ver_usuario(self): # Função para verificar todas as informações do usuário
        list = []
        for i in self.usuario_atual.projetos:
            list.append(i.nome)
        if list == []:
            list = 'Nenhum projeto alocado'
        else:
            list = " | ".join(list)
        print(f'''
        Nome: {self.usuario_atual.nome}
        Usuário: {self.usuario_atual.usuario}
        Senha: {self.usuario_atual.senha}
        Projetos: {list}
        Cargo : {self.usuario_atual.tipo}
        Id: {self.usuario_atual.id}
        ''')    

    def alterar_nome_usuario(self): # Função para alterar o nome
        nome = input('Insira o novo nome: ')
        self.usuario_atual.nome = nome
        if self.usuario_atual.projetos != []:
            for i in self.usuario_atual.projetos:
                if self.usuario_atual.tipo == 'Gerente':
                    self.projetos[self.projetos.index(i)].nome_gerente = nome
                    i.nome_gerente = nome
                elif self.usuario_atual.tipo == 'Consultor':
                    i.nome_consultor = nome
                    self.projetos[self.projetos.index(i)].nome_consultor = nome
        self.update_usuario()
        

    def alterar_nome_usuario_login(self): # Função para alterar nome de login do usuario
        nome = input('Insira o novo nome de usuário: ')
        lista = self.consultores + self.gerentes
        for i in lista:
            if i.id == self.usuario_atual.id:
                lista.pop(lista.index(i))
        for i in lista:
            if i.nome.replace(' ', '').lower() == nome.replace(' ', '').lower():
                print('Nome de usuário já utilizado, tente outro!\n')
                return
        self.usuario_atual.nome = nome
        self.update_usuario()

    def alterar_senha_usuario(self): # Função para alterar a senha do usuario
        senha = input('Insira a nova senha: ')
        self.usuario_atual.senha = senha
        self.update_usuario()

    def trocar_usuario(self): # Função para alternar entre usuários
        print('Logout efetuado!\n')
        self.update_usuario()
        self.usuario_atual = usuario_base('None','None','None')
        self.logar()

    def update_usuario(self): # Função para atualizar as informações do usuário
        list = []
        lista = []
        if self.usuario_atual.tipo == 'Consultor':
            lista = self.consultores
        elif self.usuario_atual.tipo == 'Gerente':
            lista = self.gerentes
        for i in lista:
            list.append(i.id)
        index = list.index(self.usuario_atual.id)
        if self.usuario_atual.tipo == 'Consultor':
            self.consultores[index] = self.usuario_atual
        elif self.usuario_atual.tipo == 'Gerente':
            self.gerentes[index] = self.usuario_atual

    """ Consultores """
    def req_avanco_etapa(self): # Função para requisitar o avanço de etapa em um determinado projeto
        list = []
        for i in self.usuario_atual.projetos:
            list.append(i.nome)
        p = input(f'Escolha o projeto que quer avançar: {" | ".join(list)}\n')
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p.replace(' ', '').lower() in list:
            proj =self.usuario_atual.projetos[list.index(p.replace(' ', '').lower())]
            req = [f"""
            Requisição de avanço para o projeto: {proj.nome}
            Feita pelo consultor: {self.usuario_atual.nome}\n
            """,proj.nome]
            for i in self.gerentes:
                if i.nome.replace(' ', '').lower() == proj.nome_gerente.replace(' ', '').lower():
                    i.req_avanco.append(req)
                    print('Requisição feita!\n')
                elif i == self.gerentes[len(self.gerentes)-1]:
                    print('Gerente não encontrado!\n')
                    return
        else:
            print('\nEntrada inválida\n')

    def req_retirada_projeto(self): # Função para requisitar a saída de um projeto
        list = []
        for i in self.usuario_atual.projetos:
            list.append(i.nome)
        p = input(f'Escolha o projeto quer pedir retirada: {" | ".join(list)}\n')
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p.replace(' ', '').lower() in list:
            proj =self.usuario_atual.projetos[list.index(p.replace(' ', '').lower())]
            req = [f"""
            Requisição de retirada do projeto: {proj.nome}
            Feita pelo consultor: {self.usuario_atual.nome}\n
            """,proj.nome,self.usuario_atual.id,self.usuario_atual.projetos.index(proj)]   
            for i in self.gerentes:
                if i.nome.replace(' ', '').lower() == proj.nome_gerente.replace(' ', '').lower():
                    i.req_retirada.append(req)
                    print('Requisição feita!\n')
                    return
                elif i == self.gerentes[len(self.gerentes)-1]:
                    print('Gerente não encontrado!\n')
                    return
        else:
            print('\nEntrada inválida\n')

    """ Gerentes """
    def gerenciar_pedidos_avanco(self): # Função para gerenciar os pedidos de avanço do projeto feitos pelo consultor
        list = []
        for i in self.usuario_atual.req_avanco:
            list.append(i[1])
        if list == []:
            print(f'Escolha qual requisição quer visualizar: Nenhuma requisição encontrada\n')
            return
        p = input(f'Escolha qual requisição quer visualizar: {" | ".join(list)}\n')
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p.replace(' ', '').lower() in list:
            print(self.usuario_atual.req_avanco[list.index(p.replace(' ', '').lower())][0])
            e = input('O que deseja fazer com a requisição: Aceitar | Recusar\n')
            if e.replace(' ', '').lower() == 'aceitar':
                lista = []
                for i in self.projetos:
                    lista.append(i.nome.replace(' ', '').lower())
                index = lista.index(list[list.index(p.replace(' ', '').lower())])
                self.projetos[index].etapa += 1
                print('Etapa do projeto avançada!\n')
            elif e.replace(' ', '').lower() == 'recusar':
                print('Requisição recusada!\n')
            else:
                print('Escolha inválida! Tente novamente.')
                return
            self.usuario_atual.req_avanco.pop(list.index(p.replace(' ', '').lower()))
        else:
            print('\nEntrada inválida\n')

    def gerenciar_pedidos_retirada(self): # Função para gerenciar os pedidos de retirada feitos pelo consultor
        list = []
        for i in self.usuario_atual.req_retirada:
            list.append(i[1])
        if list == []:
            print(f'Escolha qual requisição quer visualizar: Nenhuma requisição encontrada\n')
            return
        p = input(f'Escolha qual requisição quer visualizar: {" | ".join(list)}\n')
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p.replace(' ', '').lower() in list:
            print(self.usuario_atual.req_retirada[list.index(p.replace(' ', '').lower())][0])
            e = input('O que deseja fazer com a requisição: Aceitar | Recusar\n')
            if e.replace(' ', '').lower() == 'aceitar':
                lista = []
                for i in self.projetos:
                    lista.append(i.nome.replace(' ', '').lower())
                index = lista.index(list[list.index(p.replace(' ', '').lower())])
                for i in self.consultores:
                    if i.id == self.usuario_atual.req_retirada[index][2]:
                        consultor = i
                self.consultores[self.consultores.index(consultor)].projetos.pop(self.usuario_atual.req_retirada[index][3])
                self.projetos[index].nome_consultor = ''
                print('Consultor retirado do projeto!\n')
            elif e.replace(' ', '').lower() == 'recusar':
                print('Requisição recusada!\n')
            else:
                print('Escolha inválida! Tente novamente.')
                return
            self.usuario_atual.req_retirada.pop(list.index(p.replace(' ', '').lower()))
        else:
            print('\nEntrada inválida\n')
    
    def passar_projeto(self): # Função para passar o projeto para outro gerente
        list = []
        for i in self.usuario_atual.projetos:
            list.append(i.nome)
        if list == []:
            print('\nVocê está alocado nos seguintes projetos, escolha o que quer passar: Nenhum projeto alocado\n')
            return
        else:
            p = input(f'Você está alocado nos seguintes projetos, escolha o que quer passar: {" | ".join(list)}\n').replace(' ', '').lower()
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p in list:
            proj_id = self.usuario_atual.projetos[list.index(p)].id
            for i in self.projetos:
                if i.id == proj_id:
                    proj_index = self.projetos.index(i)
                elif i == self.projetos[len(self.projetos)-1]:
                    print('Index invalido!\n')
                    return
            list_ger = []
            for i in self.gerentes:
                list_ger.append(i.nome)
            g = input(f'Escolha para qual gerente deseja passar o projeto: {" | ".join(list_ger)}\n').replace(' ', '').lower()
            for i in list_ger:
                list_ger[list_ger.index(i)] = list_ger[list_ger.index(i)].replace(' ', '').lower()
            if g in list_ger:
                ger_index = list_ger.index(g)
                self.usuario_atual.projetos.pop(list.index(p))
                self.projetos[proj_index].nome_gerente = self.gerentes[ger_index].nome
                self.gerentes[ger_index].projetos.append(self.projetos[proj_index])
                print('Projeto Realocado com sucesso!')
            else:
                print('Gerente não encontrado! Tente novamente')
                return
        else:
            print('\nEntrada inválida\n')

    def entregar_projeto(self): # Função para entregar o projeto (os projetos entregues ficam armazenados e ainda podem ser visualizados com a opção "listar")
        list = []
        for i in self.usuario_atual.projetos:
            list.append(i.nome)
        if list == []:
            print('\nVocê está alocado nos seguintes projetos, escolha o que entregar: Nenhum projeto alocado\n')
            return
        else:
            p = input(f'Você está alocado nos seguintes projetos, escolha o que quer entregar: {" | ".join(list)}\n').replace(' ', '').lower()
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p in list:
            proj_id = self.usuario_atual.projetos[list.index(p)].id
            for i in self.projetos:
                if i.id == proj_id:
                    proj_index = self.projetos.index(i)
                    break
                elif i == self.projetos[len(self.projetos)-1]:
                    print('Index invalido!\n')
                    return
            if self.projetos[proj_index].etapa != 15:
                r = input(f'O projeto ainda está na etapa {self.projetos[proj_index].etapa}/15. Tem certeza que deseja entregar? Sim | Não\n')
                if r.replace(' ', '').replace('ã', 'a').lower() == 'nao':
                    return
            self.usuario_atual.projetos.pop(list.index(p))
            self.update_usuario()
            con = self.projetos[proj_index].nome_consultor
            for consultor in self.consultores:
                if consultor.nome == con:
                    for projeto in consultor.projetos:
                        if projeto.nome == self.projetos[proj_index].nome:
                            self.consultores[self.consultores.index(consultor)].projetos.pop(self.consultores[self.consultores.index(consultor)].projetos.index(projeto))
            
            self.projetos[proj_index].status = 'Entregue'
            self.projetos_finalizados.append(self.projetos[proj_index])
            self.projetos.pop(proj_index)
            print('\nProjeto entregue!\n')
        else:
            print('\nEntrada inválida\n')

    def gerenciar_alocacao_projetos(self): # Gerenciar a alocação em projetos de forma manual
        e = input('Escolha o que quer fazer: Alocar um consultor a um projeto seu | Entrar em um projeto\n').replace(' ', '').lower()
        if e == 'alocarumconsultoraumprojetoseu':
            self.alocar_consultor()
        elif e == 'entraremumprojeto':
            self.entrar_projeto()
        else:
            print('\nEntrada inválida!\n')

    def entrar_projeto(self): # Função para entrar em um projeto
        list = []
        for i in self.projetos:
            list.append(i.nome)
        if list == []:
            print('\nEscolha qual projeto deseja entrar: Nenhum projeto alocado\n')
            return
        else:
            p = input(f'Escolha qual projeto deseja entrar: {" | ".join(list)}\n').replace(' ', '').lower()
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p in list:
            proj_index = self.projetos.index(self.projetos[list.index(p)])
            if self.projetos[proj_index].nome_gerente != '':
                print('\nEsse projeto já possui um gerente alocado! Tente outro\n')
                return
            
            self.usuario_atual.projetos.append(self.projetos[proj_index])
            self.update_usuario()
            self.projetos[proj_index].nome_gerente = self.usuario_atual.nome
            print('\nEntrada no projeto feita com sucesso!\n')

    def alocar_consultor(self): # Função para alocar um consultor em um projeto
        list = []
        for i in self.usuario_atual.projetos:
            list.append(i.nome)
        if list == []:
            print('\nVocê está alocado nos seguintes projetos, escolha a qual alocar um consultor: Nenhum projeto alocado\n')
            return
        else:
            p = input(f'Você está alocado nos seguintes projetos, escolha a qual alocar um consultor: {" | ".join(list)}\n').replace(' ', '').lower()
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p in list:
            proj_id = self.usuario_atual.projetos[list.index(p)].id
            for i in self.projetos:
                if i.id == proj_id:
                    proj_index = self.projetos.index(i)
                    break
                elif i == self.projetos[len(self.projetos)-1]:
                    print('Index invalido!\n')
                    return
            if self.projetos[proj_index].nome_consultor != '':
                print('\nEsse projeto já possui um consultor alocado! Tente outro\n')
                return

            list_con = []
            for i in self.consultores:
                list_con.append(i.nome)
            c = input(f'Escolha consultor quer alocar no projeto: {" | ".join(list_con)}\n').replace(' ', '').lower()
            for i in list_con:
                list_con[list_con.index(i)] = list_con[list_con.index(i)].replace(' ', '').lower()
            if c in list_con:
                con_index = list_con.index(c)
            else:
                print('\nConsultor não encontrado! Tente novamente\n')
                return

            self.projetos[proj_index].nome_consultor = self.consultores[con_index].nome
            self.consultores[con_index].projetos.append(self.projetos[proj_index])
            print('\nConsultor alocado com sucesso!\n')

        else:
            print('\nEntrada inválida\n')
