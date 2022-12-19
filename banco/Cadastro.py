class Cadastro:
    __slot__ = ['_cadastroPessoa']
    def __init__(self):
        self._cadastroPessoa = []


    def buscarPessoa(self, cpf):
        for lp in self._cadastroPessoa:
            if lp.cpf == cpf:
                return lp
        return None

    def cadastrarPessoa(self, pessoa):
        #verifica se a pessoa exite
        isPessoa = self.buscarPessoa(pessoa.cpf)
        if isPessoa == None:
            self._cadastroPessoa.append(pessoa)
            return True
        else:
            return False
