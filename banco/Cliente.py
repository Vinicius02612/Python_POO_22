from Pessoa import Pessoa


# classe Cliente que extende de pessoa, porem com atribibutos de usuario e senha
class Cliente(Pessoa):

    __slot__ = ['nome', 'sobrenome', 'cpf', 'usuario', 'senha']

    def __init__(self, nome, sobrenome, cpf, usuario, senha):
        super().__init__(nome, sobrenome, cpf)
        self._usuario = usuario
        self._senha = senha
    

    @property
    def usuario(self):
        return self._usuario


    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario
        return self._usuario

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha
        return self._senhas
    
    def __str__(self):
        return f'{self._nome},{self._sobrenome}, {self._cpf},{self._usuario}, {self._senha}'
