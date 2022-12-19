class Pessoa:

    def __init__(self,nome, cpf, endereco,telefone):
        self.nome = nome
        self.cpf = cpf
        self.enderoco = endereco
        self.telefone = telefone

    def Nome(self):
        return self.nome

    def __str__(self) -> str:
        return f'{self.nome},{self.cpf}, {self.enderoco}, {self.telefone} '
        