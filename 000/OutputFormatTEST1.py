import sys
sys.path.append('/nfs/ovfcToolkit/Resources/site-packages')
import shotgun_api3

SERVER_PATH = "https://nocompany.shotgunstudio.com"
SCRIPT_NAME = 'Auth'
SCRIPT_KEY = 'vzjeyzxlnekuqo9cdsvo?oEji'

if __name__ == '__main__':
    sg = shotgun_api3.Shotgun(SERVER_PATH,SCRIPT_NAME,SCRIPT_KEY)
    
    #VARIABLE PARA TRAER LOS DATOS DEL PROYECTO
    test1 = sg.find_one("Project", [["name", "is", "TEST1"]])
    
    #FITLRO PARA LA BUSQUEDA DEL PROYECTO
    filtro = [['id', 'is', test1['id']]]
    req = ['code','sg_type']
    
    project = sg.find_one('Project', filtro, req)
    
    print(project)
    
    info_shot = ['project', 'sg_sequence','code','task_template','sg_versions']
    shots = sg.find('Shot', [['project', 'is', project]],info_shot)
                 
    for shot in shots:
        versions = shot['sg_versions']
        version_final = ''
        if len(versions) == 1:
            version_final = versions[0]['name']
        print('Proyecto: '+shot['project']['name']
            +'\nSecuencia: '+shot['sg_sequence']['name']
            +'\nShot: '+shot['code']
            +'\nTarea: '+shot['task_template']['name']
            +'\nVersion: '+version_final
            +'\n'
            +'\n'+shot['project']['name']+'_'+shot['sg_sequence']['name']+'_'+shot['code']+'_'+shot['task_template']['name'].strip(' ')+'_'+version_final+'.ma'
            +'\n')