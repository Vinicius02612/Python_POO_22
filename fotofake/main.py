from Fotografia import Fotografo
from Pessoa import Pessoa
import datetime

proprietario = Pessoa('Vinicius','12334566','rua jose','12234234')

data = datetime.datetime.now()

foto = Fotografo('https://avatars.githubusercontent.com/u/57628027?v=4',proprietario, data,'Vinicus')



print(foto.get_foto())