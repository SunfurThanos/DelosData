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
perfil_new = "NAMES:Andrade Echarry:LOCALHOST:_3X709ZHnD2dkCPUHQTdBWU2B0dYnkRbjHwz3pMTv40"

#-------------------------------------------------------------------------------------------

# insertando llave
validar = dict_db.add(cedula, perfil_new)

#-------------------------------------------------------------------------------------------

# haciendo test de redimiento (automatico)
valor, seconds = dict_db.get(cedula, time=True)

print "%s seconds" % seconds.float(4)
print "%s milliseconds" % seconds.toMs()
print "%s nanoseconds"  % seconds.toNs().xfloat()
