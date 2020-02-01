#SE PUEDE HACER DESDE LA INTERFAZ WEB

#CREATE
import shotgun_api3
sg = shotgun_api3.Shotgun("https://learn.shotgunstudio.com", login="learn", password="*******")
sg.find_one("Project", [["name", "is", "crud"]])
{'type': 'Project', 'id': 90}
project = sg.find_one("Project", [["name", "is", "crud"]])
sg.create("Shot", {"code": "sh002", "project": project})
{'id': 1207, 'code': 'sh002', 'project': {'id': 90, 'name': 'CRUD', 'type': 'Project'}, 'type': 'Shot'}


#READ
sg.find_one("Project", [["name", "is", "crud"]])
project = sg.find_one("Project", [["name", "is", "crud"]])

#MANERA INCORRECTA DE OBTENER EL SHOT
sg.find("Shot", [["code", "is", "sh001"]])
sg.find_one("Shot", [["code", "is", "sh001"]])

#MANERA CORRECTA DE OBTENER EL SHOT
sg.find("Shot", [["code", "is", "sh001"], ["project", "is", project]])
sg.find_one("Shot", [["code", "is", "sh001"], ["project", "is", project]])

#CON EL ESTATUS DE LA LISTA
sg.find_one("Shot", [["code", "is", "sh001"], ["project", "is", project]], ["sg_status_list"])

#CON LA DESCRIPCION
sg.find_one("Shot", [["code", "is", "sh001"], ["project", "is", project]], ["sg_status_list", "description"])

#OBTENIENDO TODOS LOS SHOTS
sg.find("Shot",[["project", "is", project]])

shots = sg.find("Shot", [["project", "is", project]])
for shot in shots:
    print shot
    
shots = sg.find("Shot", [["project", "is", project]], ["sg_status_list", "description"])

for shot in shots:
    print shot


#UPDATE
project = sg.find_one("Project", [["name", "is", "crud"]])

sequence = sg.create("Sequence", {"project": project, "code": "seq001"})

sequence

shots = sg.find("Shot", [["project", "is", project]])
for shot in shots:
    sg.update("Shot", shot["id"], {"sg_status_list": "ip", "sg_sequence": sequence})
    
    
    
#DELETE
project = sg.find_one("Project", [["name", "is", "crud"]])
shots = sg.find("Shot", [["project", "is", project]])

for shot in shots:
    sg.delete("Shot", shot["id"])
    
#REVIVE
for shot in shots:
    sg.revive("Shot", shot["id"])
