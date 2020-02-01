#Existen 6 formas de instalar shotgun

#DESCARGAR DESDE GITHUB
#BUSCAR LA ULTIMA VERSION EN EL REPOSITORIO DE GITHUB
#OBTENER EL CODIGO FUENTE Y DEL ARCHIVO COMPRIMIDO COPIAR 
#LA CARPETA EN DOCUMENTOS O EN CUALQUIER UBICACION
#DESDE CONSOLA ACCEDER A /python-api-3.2.2/
#e iniciar python

import shotgun_api3
sg = shotgun_api3.Shotgun("https://learn.shotgunstudio.com", login="learn", password="*******")
sg.find_one("Project", [["name", "contains", "cuts"]], ["name"])


#CLONAR DESDE GITHUB Y REALIZAR LOS MISMOS PASOS COMO SI SE DESCARGARA EL CODIGO FUENTE


#INSTALAR DESDE PIP & VIRTUALENV
#DESDE CONSOLA IR A LA CARPETA EN DONDE SE DESEA INSTALAR Y EJECUTAR EL COMANDO

virtualenv sg_python_api
source sg_python_api/bin/activate
#COMANDO PIP DE LA DOCUMENTACION
#COMANDO EJECUTAR PYTHON
import shotgun_api3
exit()
deactivate

#INSTALAR SHOTGUN DESKTOP Y ACCEDER A LA CONSOLA DESDE AHI

sg = shotgun

project = engine.context.project

shots = sg.find(
    "Shot",
    [["project", "is", project]],
    ["code", "sg_status_list"]
)

for shot in shots:
    print shot
    

#USANDO LA CONSOLA DCC DE LOS PROGRAMAS DE MODELADO

import sgtk

engine = sgtk.platform.current_engine()

project = engine.context.project

sg = engine.shotgun

shots = sg.find(
    "Shot",
    [["project", "is", project]],
    ["code", "sg_status_list"]
)

for shot in shots:
    print shot


#USANDO TANK SHELL
