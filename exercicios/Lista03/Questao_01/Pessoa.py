import re

dic_pessoas = {}

class Pessoa:
    def __init__(self,nome, data_nascimento, altura):
        self._nome = nome
        self._dataNascimento = data_nascimento
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
        print(f'Nome: {self._nome} \n Data de Nascimento: {self._dataNascimento} \n Altura: {self._altura}')

    def getIdade(self):
        date = self._dataNascimento

        ## usando lista compreensiva para pegar a data de nascimento em strign e converter para uma lista de inteiros
        data_convertida = [int(s) for s in re.findall(r'-?\d+\.?\d*', date)]

        ## pegando o ano de nascimento que é o ultimo elemento da lista
        get_ano =data_convertida[-1]

        ano_atual = 2022
        if  get_ano > ano_atual:
            print('A data de nascimento tem que ser menor que a data atual ')
            return False
        else:
            idade =  ano_atual - get_ano
            return  f'Sua idade é: {idade}'
