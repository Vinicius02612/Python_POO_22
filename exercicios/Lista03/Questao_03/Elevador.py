

class Elevador:
    
    def __init__(self,total_Andares,capacidade,quant_pessoas ,andarAtual = 0):
        self._total_Andares = total_Andares
        self._andarAtual = andarAtual
        self._capacidade = capacidade
        self._quant_pessoas = quant_pessoas
    
# get e setter do total de andares 
# ==========================================  
    @property
    def tota_Andares(self):
        return self._total_Andares
    

    @tota_Andares.setter
    def setTotal(self, t):
        self._total_Andares = t
# ==========================================

# get e setter do andar atual 
# ==========================================
    @property
    def AndarAtual(self):
        return self._andarAtual
    
    
    @AndarAtual.setter
    def AndarAtual(self, a):
        self._andarAtual = a
# ===========================================

# get e setter da capacidade 
# ==========================================
    @property
    def capacidade(self):
        return self._capacidade 

    @capacidade.setter
    def capacidade(self, c):
        self._capacidade = c 
# ===========================================

# get e setter da quantidade de pessaos
# ==========================================
    @property
    def pessoa(self):
        return self._quant_pessoas
    
    @pessoa.setter
    def setPessoa(self, p):
        self._quant_pessoas = p
# ==============================================   



# Metodos do elevador
# ==========================================
    def inicializa(self, capacidade, totalAndares):
            self._capacidade = capacidade
            self._total_Andares = totalAndares
            return True


    def Entrar(self, quantPessoa,andarAtual):
        if quantPessoa < self._capacidade and andarAtual > 0:
            self._quant_pessoas += quantPessoa
            self._andarAtual += andarAtual
            return True
        else:
            return False
        
    

    def Sair(self, pessoa):
        if self._quant_pessoas > 0:
            self._quant_pessoas -= pessoa
        else:
            print('Não da pra sair por que ta vazio')
            return False

 # Sobe : para subir um andar (não deve subir se já estiver no último andar);   
    def Subir(self,andar):
        if andar > self._andarAtual and andar < self._total_Andares:
            self._andarAtual = andar
            return True
        else:
            print('Total de andares execedido')
            return False

    def Descer(self,andar):
        if andar < self._andarAtual and andar > 0:
            self._andarAtual = andar
        else:
           print('impossivel descer, voce ja esta no terreo.')

    def MostraElevador(self):
        print(f'Total de Andares: {self._total_Andares}\n'
              f'Capacidade: {self._capacidade}\n'
              f'Quantide de Pessoas: {self._quant_pessoas}\n'
              f'Andar Atual: {self._andarAtual}\n')
