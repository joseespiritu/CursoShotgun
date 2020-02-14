#CREANDO UNA INSTANCIA DE LA API DE SHOTGUN
import pprint
import shotgun_api3

SERVER_PATH = "https://nocompany.shotgunstudio.com"
SCRIPT_NAME = 'Auth'
SCRIPT_KEY = 'vzjeyzxlnekuqo9cdsvo?oEji'

sg = shotgun_api3.Shotgun(SERVER_PATH,SCRIPT_NAME,SCRIPT_KEY)

pprint.pprint([symbol for symbol in sorted(dir(sg)) if not symbol.startswith('_')]) #FUNCION QUE REGRESA LOS METODOS SI LA CONEXION ES CORRECTA


#CREAR UN SHOT EN UN PROYECTO POR SU ID
import shotgun_api3
from pprint import pprint

SERVER_PATH = "https://nocompany.shotgunstudio.com"
SCRIPT_NAME = 'Auth'
SCRIPT_KEY = 'vzjeyzxlnekuqo9cdsvo?oEji'

if __name__ == '__main__':
	sg = shotgun_api3.Shotgun(SERVER_PATH,SCRIPT_NAME,SCRIPT_KEY)

	data = {
		'project': {"type": "Project", "id": 90},
		'code': '100_010',
		'description': 'Open on a beautiful field with fuzzy bunnies',
		'sg_status_list': 'ip'
	}
	result = sg.create('Shot', data)
	pprint(result)
	print("The id of the {} is {}.".format(result['type'], result['id']))


#ENCONTRAR UN SHOT
import shotgun_api3
from pprint import pprint

SERVER_PATH = "https://nocompany.shotgunstudio.com"
SCRIPT_NAME = 'Auth'
SCRIPT_KEY = 'vzjeyzxlnekuqo9cdsvo?oEji'

if __name__ == '__main__':
	sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

	filters = [['id', 'is', 1209]]
	result = sg.find_one('Shot', filters)
	pprint(result)


#ACTUALIZAR UN SHOT
import shotgun_api3
from pprint import pprint

SERVER_PATH = "https://nocompany.shotgunstudio.com"
SCRIPT_NAME = 'Auth'
SCRIPT_KEY = 'vzjeyzxlnekuqo9cdsvo?oEji'

if __name__ == '__main__':
	sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)
	data = {
		'description': 'Open on a beautiful field with fuzzy bunnies',
		'sg_status_list': 'ip'
	}
	result = sg.update('Shot', 1209, data)
	pprint(result)


#ELIMINAR UN SHOT
import shotgun_api3
from pprint import pprint

SERVER_PATH = "https://nocompany.shotgunstudio.com"
SCRIPT_NAME = 'Auth'
SCRIPT_KEY = 'vzjeyzxlnekuqo9cdsvo?oEji'

if __name__ == '__main__':
	sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

	result = sg.delete("Shot", 1209)
	pprint(result)



#CREAR UN SHOT DESDE UN TASK TEMPLATE
import shotgun_api3
from pprint import pprint

SERVER_PATH = "https://nocompany.shotgunstudio.com"
SCRIPT_NAME = 'Auth'
SCRIPT_KEY = 'vzjeyzxlnekuqo9cdsvo?oEji'

if __name__ == '__main__':
	sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

	filters = [['code', 'is', 'sh002']]
	template = sg.find_one('Shot', filters)
	pprint(template)