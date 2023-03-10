Id = 0

class usuario_base:
    def __init__(self,nome,user,senha):
        self.nome = nome
        self.__usuario = user
        self.__senha = senha
        global Id
        self.__id = Id # Garantindo ID unico
        Id += 1
        self.projetos = [] #projetos alocados
        self.tipo = None

    @property
    def usuario(self):
        return self.__usuario
    @usuario.setter
    def usuario(self,user):
        self.__usuario = user

    @property
    def id(self):
        return self.__id

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self,senha):
        self.__senha = senha

    def ver_projetos_alocados(self):
        list = []
        for i in self.projetos:
            list.append(i.nome)
        if list == []:
            print('\nVocê está alocado nos seguintes projetos, escolha o que quer ver: Nenhum projeto alocado\n')
            return
        else:
            p = input(f'Você está alocado nos seguintes projetos, escolha o que quer ver: {" | ".join(list)}\n')
        for i in range(len(list)):
            list[i] = list[i].replace(' ', '').lower()
        if p.replace(' ', '').lower() in list:
            obj = self.projetos[list.index(p.replace(' ', '').lower())]
            print(obj)
        else:
            print('Entrada inválida')

    def ver_nome(self):
        print(f'\nNome: {self.nome}\n')

class Consultor(usuario_base):
    def __init__(self,nome,user,senha):
        super().__init__(nome,user,senha)
        self.tipo = 'Consultor'

class Gerente(usuario_base):
    def __init__(self,nome,user,senha):
        super().__init__(nome,user,senha)
        self.tipo = 'Gerente'
        self.req_avanco = []
        self.req_retirada = []

class Projeto:
    def __init__(self,nome, coord,etapa:int,consultor,gerente):
        self.nome = nome
        self.coordenacao = coord
        self.etapa = etapa #15 total
        self.nome_consultor = consultor
        self.nome_gerente = gerente
        self.status = 'Em andamento'
        global Id
        self.__id = Id # Garantindo ID unico
        Id += 1

    @property
    def id(self):
        return self.__id

    def __str__(self): # Customizando a string da classe para fazer um print detalhado na lista
        return f'''
        Projeto {self.nome} , Etapa : {self.etapa}/15

        Coordenação: {self.coordenacao}
        Consultor: {self.nome_consultor}
        Gerente: {self.nome_gerente}
        Status: {self.status}
        '''