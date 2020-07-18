# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

archivo_db = "./prueba.chappie"
archivo_db.path.delete()

#-------------------------------------------------------------------------------------------

# creando BD tipo diccionario
dict_db = DelosData.create(keys=1000)
validar = dict_db.export(archivo_db)

#-------------------------------------------------------------------------------------------

if validar:
	print "la BD fue creada: {size_db}".toF
else:
	print "no se puedo crear, el archivo ya existe"

#-------------------------------------------------------------------------------------------

"""

NOTA : la BD no puede sobrepasar los (93 GB), de lo contrario el Index colapsara y ocasionara errores graves de escritura y lectura.

"""
