from Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, profissao):
        super().__init__(nome, cpf, data_nascimento)
        self._profissao = profissao
        self._cliente_seguro = None
        pass

    @property
    def profissao(self):
        return self._profissao
    
    @profissao.setter
    def profissao(self, pfs):
        self._profissao = pfs
        return self._profissao
    

    @property
    def cliente_seguro(self):
        return self._cliente_seguro
    
    @cliente_seguro.setter
    def cliente_seguro(self, seguro):
        self._cliente_seguro = seguro
        return self.cliente_seguro
    
    def imprimeCliente(self):
        print(f'Nome: {self._nome}\n'
            f'CPF: {self._cpf}\n'
            f'Data de Nascimento: {self._data_nascimento}\n'
            f'Profissao: {self._profissao}\n')
        # metodo que retorna uma string de cliente

    def __repr__(self):
        return f'\n\tNome: {self._nome}\n\tCPF: {self._cpf}\n\tData de nascimento: {self._data_nascimento}\n\t Profissão: {self._profissao}\n'

# Usando associação de classes
class Seguro_de_vida(Cliente):

    def __init__(self, nome, cpf,  v_mensal, v_total):
        self._nome = nome
        self._cpf = cpf
        self._v_mensal = v_mensal
        self._v_total = v_total
    
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
    def v_mensal(self):
        return self._v_mensal
    
    @v_mensal.setter
    def v_mensal(self, v):
        self._v_mensal = v
        return self._v_mensal
    
    @property
    def v_total(self):
        return self._v_total

    @v_total.setter
    def v_total(self, v):
        self._v_total = v
        return self._v_total


    def dados_do_seguro(self):
        print(f'\nNome: {self._nome} \nCPF: {self._cpf} \nValor Mensal: {self._v_mensal} \nValor Total: {self._v_total}\n')