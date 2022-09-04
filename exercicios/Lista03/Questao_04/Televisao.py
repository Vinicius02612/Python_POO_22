##Crie uma classe Televisao e uma classe ControleRemoto que pode controlar o volume e trocar os canais da
#televisão. O controle de volume permite: aumentar ou diminuir a potência do volume de som em uma unidadede cada vez; aumentar e diminuir o número do canal em uma unidade trocar para um canal indicado; consultar
#o valor do volume de som e o canal selecionado. A classe controle remoto deve possuir um menu iterativo para
#o usuário escolher as opções desejadas.

class Televisao:

    def __init__(self, volume, canal, status):
        self._volume = volume
        self._canal = canal
        self._status = status

    @property
    def getVolume(self):
        return  self._volume
        
    @getVolume.setter
    def Setvolume(self, vol):
        volMax = 100
        volMin = 0
        if vol < volMax and vol > volMin:
            self._volume = vol
            return True
        else:
            return False


    @property
    def getCanal(self):
        return self._canal
    
    @getCanal.setter
    def setCanal(self, canal):
        maxCanal = 100
        minCanal = 1
        if canal  < maxCanal and canal > minCanal:
            self._canal = canal
            return True
        else:
            return False
    
    @property
    def getStatus(self):
        return self._status
    
    @getStatus.setter
    def setStatus(self, status):
        if status == 0:
            self._status = status
            print('Tv esta ligada!')
        if status == 1:
            print('Esta desligada!')
        else:
            return False
   
  