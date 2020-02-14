# LIBRERIAS IMPORTADAS PARA DEBUG Y API SHOTGUN
import pprint
import shotgun_api3

# VARIABLES PARA CONEXION
SERVER_PATH = "https://nocompany.shotgunstudio.com"
SCRIPT_NAME = 'Auth'
SCRIPT_KEY = 'vzjeyzxlnekuqo9cdsvo?oEji'

if __name__ == '__main__':
	# AUTENTICACION
	sg = shotgun_api3.Shotgun(SERVER_PATH,SCRIPT_NAME,SCRIPT_KEY)

    	#CREACION DE PROYECTO DESDE API
	"""proyecto_data = {
      		"name": "TEST2",
        	"sg_type": "Other",
        	"sg_description": "Test 2 prueba de shots, secuencias y tareas.",
        	"tank_name": "test2",
    	}
    	proyectoCreado = sg.create("Project", proyecto_data)"""
    
	#INSTANCIA DE PROYECTO
	test2 = sg.find_one("Project", [["name", "is", "TEST2"]])

	#DATOS PARA CREACION LAS TAREAS
	tarea1_data = {
		'project': {'type':'Project', 'id':test2['id']},
		'content': 'Modelar',
		'sg_description': 'Realizar modelado',
		'sg_status_list': 'wtg',
		'start_date': '2020-01-01',
		'due_date': '2020-01-10'
    }

	tarea2_data = {
		'project': {'type':'Project', 'id':test2['id']},
		'content': 'Animar',
		'sg_description': 'Realizar animacion',
		'sg_status_list': 'wtg',
		'start_date': '2020-01-11',
		'due_date': '2020-01-30'
    }
	
	tarea3_data = {
		'project': {'type':'Project', 'id':test2['id']},
		'content': 'Texturas',
		'sg_description': 'Realizar texturas',
		'sg_status_list': 'wtg',
		'start_date': '2020-02-01',
		'due_date': '2020-02-10'
    }
	
	#CREACION DE TAREAS
	tarea1 = sg.create('Task', tarea1_data)
	tarea2 = sg.create('Task', tarea2_data)
	tarea3 = sg.create('Task', tarea3_data)

	# DATOS PARA CREACION DE SHOTS
	shot1_data = {
		'project': {"type": "Project", "id": test2['id']},
		'code': 'sh0001',
		'description': 'Mi shot1 test',
		'sg_status_list': 'wtg',
	}

	shot2_data = {
		'project': {"type": "Project", "id": test2['id']},
		'code': 'sh0002',
		'description': 'Mi shot2 test',
		'sg_status_list': 'wtg'
	}

	#CREACION DE SHOTS
	shot1 = sg.create('Shot', shot1_data)
	shot2 = sg.create('Shot', shot2_data)

	#CREANDO SECUENCIA
	sequence = sg.create("Sequence", {"project": test2, "code": "seq0001"})
	sequence

	#BUSQUEDA DE SHOTS
	shots = sg.find("Shot", [["project", "is", test2]])

	#ASIGNAR SECUENCIA A SHOTS
	for shot in shots:
		sg.update("Shot", shot["id"], {"sg_sequence": sequence})
		print(shot)