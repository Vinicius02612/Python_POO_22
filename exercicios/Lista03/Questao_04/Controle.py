from Televisoa import Televisao


class ControleRemoto:

    def __init__(self) -> None:
        self._tv = Televisao()
    
    def aumentar_volume(self):
        vol = int(input('informe em quanto vc quer aumentar:'))
        self._tv.Setvolume(vol)
    
    def diminuir_volume(self):
        self._tv.Setvolume