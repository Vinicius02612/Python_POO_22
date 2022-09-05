


from Televisao import Televisao


class ControleRemoto:

 
    def __init__(self, televisao = Televisao()):
        self.televisao = televisao
    

    def DiminuiCanal(self):
        self.televisao._canal += 1
        print(f'Canal atual: {self.televisao._canal}')

    def AumentaCanal(self):
        self.televisao._canal -= 1
        print(f'Canal: {self._televisao._canal}')
    
    def ReduzirVolume(self):
        self.televisao._volume -= 1
    
    def AumentarVolume(self):
        self.televisao._volume += 1
    

    def ProcuraCanal(self):
        cnl = int(input('informe o canal que procura: '))
        self.televisao._canal = cnl
        print(f'Canal atual: {self.televisao._canal} ')