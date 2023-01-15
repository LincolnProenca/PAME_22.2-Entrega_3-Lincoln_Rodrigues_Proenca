idg = 0
idc = 0
opcoes_basicas = 'Escolha o que quer fazer: Criar projeto | Remover Projeto | Criar Consultor | Remover Consultor | Criar Gerente | Remover Gerente | Listar | Fazer Login | Sair\n'
opcoes_comuns = 'Verificar projetos | Ver nome | Alterar Nome | Ver usuário | Alterar usuário | Alterar senha\n'
opcoes_gerente = 'Gerenciar pedidos de avanço | Gerenciar pedidos de retirada | Passar o projeto a outro gerente | Entregar um projeto\n'
opcoes_consultor = 'Requisitar Avanço de etapa | Pedir retirada do projeto\n'

class usuario_base:
    def __init__(self,nome,user,senha):
        self.nome = nome
        self.__usuario = user
        self.__senha = senha
        self.projetos = [] #projetos alocados
        self.tipo = None

    @property
    def usuario(self):
        return self.__usuario
    @usuario.setter
    def usuario(self,user):
        self.__usuario = user

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self,senha):
        self.__senha = senha

    def ver_projetos(self):
        pass

class Consultor(usuario_base):
    def __init__(self,nome,user,senha):
        super().__init__(nome,user,senha)
        global idc
        self.id = idc #garantindo id unico
        idc += 1
        self.tipo = 'Consultor'
        pass

class Gerente(usuario_base):
    def __init__(self,nome,user,senha):
        super().__init__(nome,user,senha)
        global idg
        self.id = idg #garantindo id unico
        idg += 1
        self.tipo = 'Gerente'
        pass

class Projeto:
    def __init__(self,nome, coord,etapa:int,consultor,gerente):
        self.nome = nome
        self.coordenacao = coord
        self.etapa = etapa #15 total
        self.nome_consultor = consultor
        self.nome_gerente = gerente

    def __str__(self): # Customizando a string da classe para fazer um print detalhado na lista
        return f'''
        Projeto {self.nome} , Etapa : {self.etapa}/15

        Coordenação: {self.coordenacao}
        Consultor: {self.nome_consultor}
        Gerente: {self.nome_gerente}
        '''