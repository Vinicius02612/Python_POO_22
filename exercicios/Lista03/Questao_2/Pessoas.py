
dic_Agenda = {}
class Agenda:
    def __init__(self, nome, idade,altura):
        self._nome = nome
        self._idade = idade
        self._altura = altura

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
    
## Tentar refazer de outra forma 
    def armazenarPessoa():
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        altura = float(input('Altura: '))

        AgendaP = Agenda(nome, idade, altura)
        dic_Agenda[nome] = AgendaP

    def ImprimirPessoa(self):
        print(f'\nNome: {self._nome}\n'
            f'\nIdade: {self._idade}\n' 
            f'\nAltura: {self._altura}\n'
        )


i = 1
A = Agenda
while i > 0:
    print(
        '\n1- Armazenar Pessoa'
        '\n2 - Remover Pessoa'
        '\n3 - Buscar Pessoa'
        '\n4 - Imprimir Agenda')
    
    opc = int(input('Digite uma opção: '))

    if opc == 1:
        A.armazenarPessoa()
    if opc == 2:
        A.ImprimirPessoa()