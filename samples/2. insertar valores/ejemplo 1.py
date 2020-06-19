# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

salida = "./saludos.xD"
salida.path.delete()

#-------------------------------------------------------------------------------------------

# crear BD
dict_db = DelosData.create(keys=4600)
dict_db.export(salida)

#-------------------------------------------------------------------------------------------

# importar BD
dict_db = DelosData.open(salida)

#-------------------------------------------------------------------------------------------

## barra de progreso
docker = NameSpace()
docker.end = dict_db.keys
docker.concurrent = 0x0
docker.finish = False

def funcion_progreso(docker):
	console.clear()
	progreso = "%0.2f" % Math("{concurrent} * 100 / {end}".toF, prec=4)
	print ("{progreso}%".toF, docker.concurrent, docker.end,)
	if not docker.finish: return True

set_timeout(0.7, funcion_progreso, docker)

#-------------------------------------------------------------------------------------------

# insertando llaves + valores
for docker.concurrent in xrange(1, dict_db.keys+1):
	llave = "hola " + docker.concurrent.toS
	item  = "ITEM " + docker.concurrent.toS
	dict_db.add(llave, item)
docker.finish = True

#-------------------------------------------------------------------------------------------

"""

NOTA : la longitud de los valores (items) de las llaves no pueden sobrepasar los (9.7 Kbs)

NOTA : las llaves pueden tener una longitud "INFINITA", en el diccionario no se guardan los nombres de las llaves, solo su conversión de memoria espacial cuantificada, es decir cada llave (word) se convierte a una posición de memoria, en dicha posición se guarda el valor numérico (posición) de su item correspondiente, de esta manera nadie que no conozca las llaves podrá obtener información de la BD.

"""
