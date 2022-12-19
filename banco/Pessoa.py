class Pessoa:

    __slot__ = ['nome', 'sobrenome', 'cpf']

    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sbnome):
        self._sobrenome = sbnome
        return self._sobrenome

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
        return self._cpf
    
    def get_dados(self):
        print(f'Nome:{self._nome}\n sobrenome: {self._sobrenome}\nCPF: {self._cpf}')

    def __str__(self):
        return f'Nome:{self._nome}\n sobrenome: {self._sobrenome}\nCPF: {self._cpf}'


