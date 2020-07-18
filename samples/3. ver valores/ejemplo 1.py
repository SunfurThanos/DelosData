# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

salida = "./saludos.xD"
salida.path.delete()

#-------------------------------------------------------------------------------------------

# crear BD
dict_db = DelosData.create(keys=1000)
dict_db.export(salida)

#-------------------------------------------------------------------------------------------

# importar BD
dict_db = DelosData.open(salida)

#-------------------------------------------------------------------------------------------

cedula     = "25.969.358"
perfil_new = "NAMES:Andrade Echarry:LOCALHOST:_3js7RHbLSHKV13qUFCVIhb"

#-------------------------------------------------------------------------------------------

# insertando llave
validar = dict_db.add(cedula, perfil_new)

#-------------------------------------------------------------------------------------------

# mostrando item de la llave
datos = dict_db.get(cedula)
if datos: print datos.cut(":").group(2)

#-------------------------------------------------------------------------------------------

datos = dict_db.get("26.111.456")
if datos:
	print datos.cut(":").group(2)
else:
	print "El perfil requerido no existe. Sorry"
