class Pessoa:
    def __init__(self,nome, data_cimento, altura):
        self._nome = nome
        self._dataNascimento = data_cimento
        self._altura = altura
    
    @property
    def nome(self):
        return self._nome 
    
    @nome.setter
    def nome(self, n):
        self._nome = n

    @property
    def dataNascimento(self):
        return self._dataNascimento

    @dataNascimento.setter
    def dataNascimento(self, dt):
        self._dataNascimento = dt

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, alt):
        self._altura = alt
    
    def listaPessoas(self):
        print(f'Nome: {self._nome} \n Data de Nascimento: {self._dataNascimento} \n Altura: {self._altira}')

    