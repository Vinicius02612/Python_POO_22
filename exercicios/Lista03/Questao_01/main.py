from Pessoa import Pessoa

dic_pessoas = {}

def preenche_dados():
    nome = input('Nome: ')
    dataNascimento = input('Data de Nascimento: ')
    altura = float(input('Altura: '))

    pessoa =  Pessoa(nome, dataNascimento, altura)
    dic_pessoas[nome] = pessoa

def listarPessoas():
    for i in dic_pessoas.values():
        i.listaPessoas()
        
def PegaIdade():
    for i in dic_pessoas.values():
        i.getIdade()
     


preenche_dados()

listarPessoas()

PegaIdade()

