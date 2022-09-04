
dic_Agenda = {}
class Agenda:
    def __init__(self, nome, idade,altura):
        self._nome = nome
        self._idade = idade
        self._altura = altura
    
    def __str__(self):
        return f'\n\tNome: {self._nome}\n\t Idade:{self._idade}\n\tAltura: {self._altura}'


    # setter de nome
    @property
    def nome(self):
        return self._nome
    
    #getter de nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        return self._nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade
        return self._idade
    
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def idade(self, idade):
        self._altura = idade
        return self._altura

    def ImprimeAgenda(self):
        print(
            f'Nome: {self._nome}\n'
            f'Idade: {self._idade}\n'
            f'Altura: {self._altura}\n'
        )
