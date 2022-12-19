from Pessoa import Pessoa

class Gerente(Pessoa):
    
    def __init__(self, nome, sobrenome, cpf, usuario, senha):
        super().__init__(nome, sobrenome, cpf)
        self._usuario = usuario
        self._senha = senha
    
    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def usuario(self, usr):
        pass


    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, snh):
        if len(snh) < 8 and any(snh.isdigit()): # verifica se a senha digitada contem letras e numeros
            return False, 'senha deve conter pelo menos 8 caracteres contendo letras e numeros'
        else:
            self._senha = snh

    def get_dados_gerente(self):
        print(f'Nome: {self._nome}\nSobrenome:{self._sobrenome}\nCPF: {self._cpf}\nUsuário: {self._usuario}\n Senha:{self._senha} ')