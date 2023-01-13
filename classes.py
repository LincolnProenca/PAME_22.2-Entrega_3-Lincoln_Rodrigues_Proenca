idG = 0
idC = 0
print('meme')

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

class Consultor(usuario_base):
    def __init__(self,nome,user,senha):
        super.__init__(nome,user,senha)
        self.id = idC
        idc += 1
        pass

class Gerente:
    def __init__(self,nome,user,senha):
        super.__init__(nome,user,senha)
        self.id = idG
        idc += 1
        pass

class Projeto:
    def __init__(self):
        pass
