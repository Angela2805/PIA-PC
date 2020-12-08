import os
import shutil

#Función para la creación de la carpeta
def crear_dir():
    directorio = "C:/PIA"
    try:
        #Esta sección dicta que, si un directorio existe, lo remueva y cree otro con el mismo nombre
        if os.path.exists(directorio): 
            shutil.rmtree(directorio) 
        os.makedirs(directorio) 
    except OSError:
        print ("La creación de la carpeta %s falló" % directorio)
    else:
        print ("Se ha creado el directorio: %s " % directorio)
        
