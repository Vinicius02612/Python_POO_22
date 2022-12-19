import skimage.io
import matplotlib.pyplot as plt
import datetime
""" import plotly.io as pio
pio.renderers.default = 'svg' """
""" Foto -> str com endereço da imagem (o atributo deverá armazenar a imagem e não o
endereço dela, dica: from skimage.io import imread)

Fotógrafo -> Pessoa com Nome, CPF, Endereço e telefone

Data -> data que a fotografia foi obtida

Proprietário -> Pessoa

Quantidade de Fotos -> contador para quantidade de objetos Fotografia criados


A classe Fotografia terá os seguintes métodos:

Mostrar Fotografia (dica: from matplotlib.pyplot import imshow)

Propriedades da Fotografia: tamanho da Fotografia em pixels (dica: fotografia.shape),
fotógrafo, data


Métodos para alterar e acessar atributos.

Crie Slots
 """



class Fotografo:

    __slot__ = ['foto','fotografo', 'data','qtd']
    _qtd_ = 0
    def __init__(self, foto, fotografo, data, props):
        self._foto = skimage.io.imread(foto)
        self._fotografo = fotografo
        self._data = data
        self._props = props
        Fotografo._qtd_ += 1

    @property
    def foto(self):
        return self._foto
    
    @foto.setter
    def foto(self, foto):
        self._foto = foto
        return self._foto

    @property
    def fotografo(self):
        return self._fotografo
    
    @fotografo.setter
    def fotogrado(self, nmFotografo):
        self._fotografo = nmFotografo
        return self._fotografo
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data
        return self._data
    
    @property
    def props(self):
        return self._props
    
    @props.setter
    def props(self, props):
        self._props = props
        return self._props

    @staticmethod
    def get_qtd(self):
        return Fotografo._qtd_

    def get_foto(self):
       return plt.imshow(self._foto)