idG = 0
idC = 0
print('teste')
opcoes_comuns = 'Verificar projetos | Ver nome | Alterar Nome | Ver usuário | Alterar usuário | Alterar senha\n'
opcoes_gerente = 'Gerenciar pedidos de avanço | Gerenciar pedidos de retirada | Passar o projeto a outro gerente | Entregar um projeto\n'
opcoes_consultor = 'Requisitar Avanço de etapa | Pedir retirada do projeto\n'

class usuario_base:
    def __init__(self,nome,user,senha):
        self.nome = nome
        self.__usuario = user
        self.__senha = senha
        self.projetos = []

    @property
    def nome(self):
        return self.nome
    @nome.setter
    def nome(self,n):
        self.nome = n

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
        super.__init__(nome,user,senha)
        self.id = idC
        idc += 1
        self.tipo = 'Consultor'
        pass

class Gerente:
    def __init__(self,nome,user,senha):
        super.__init__(nome,user,senha)
        self.id = idG
        idc += 1
        self.tipo = 'Gerente'
        pass

class Projeto:
    def __init__(self,nome, coord,etapa:int,consultor,gerente):
        self.nome = nome
        self.coordenacao = coord
        self.etapa = etapa #15 total
        self.nome_consultor = consultor
        self.nome_gerente = gerente

    def __str__(self):
        return f'''
        Projeto {self.nome} , Etapa : {self.etapa}/15

        Coordenação: {self.coordenacao}
        Consultor: {self.nome_consultor}
        Gerente: {self.nome_gerente}
        '''