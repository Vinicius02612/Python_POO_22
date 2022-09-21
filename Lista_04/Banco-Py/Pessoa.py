import abc, re

class Pessoa(abc.ABC):

    def __init__(self, nome, cpf, data_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        return  self._nome

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
        return self._cpf
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, data): 
        date = data

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
            self._data_nascimento = data 
            return idade
    
            # metodo que retorna uma string de cliente
    def __str__(self):
        return f'\n\tNome: {self._nome}\n\tCPF: {self._cpf}\n\tData de Nascimento: {self._data_nascimento}'