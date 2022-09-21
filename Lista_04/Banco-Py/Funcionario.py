from Pessoa import Pessoa

# classe conta que estende de dentro de funcionarios.
class Funcionario(Pessoa):

    def __init__(self, nome, cpf, data_nascimento, salario):
        super().__init__(nome, cpf, data_nascimento)
        self._salario = salario


    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario
        return salario
    
    def imprime(self):
        print(f'Nome: {self._nome}\n'
            f'Cpf: {self._cpf}\n'
            f'Data de nascimento: {self._data_nascimento}\n'
            f'Salario: {self._salario}\n')

    # metodo que retorna uma string de cliente
    def __repr__(self):
        return f'\n\tNome: {self._nome}\n\tCPF:{self._cpf}\n\tSalario: {self._salario}'






