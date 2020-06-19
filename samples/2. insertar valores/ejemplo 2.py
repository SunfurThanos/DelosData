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

cedula     = "25.969.358"
perfil_new = "Andrade Echarry:localhost:_3js7RHbLSHKV13qUFCVIhb"

#-------------------------------------------------------------------------------------------

## isertado
validar = dict_db.add(cedula, perfil_new)
if validar == "YES":
	print "perfil creado correctamente"

#-------------------------------------------------------------------------------------------

validar = dict_db.add(cedula, perfil_new)
if validar == "EXIST":
	print "este perfil ya existe. Sorry"

#-------------------------------------------------------------------------------------------

"""

YES          : llave insertada correctamente

EXIST        : la llave ya existe

table-UP     : la tabla (index) esta llena

item-size    : el item sobre-pasa la longitud permitida

ERROR-CRICAL : error critico de escritura

file-close   : el archivo (BD) esta cerrada

"""
