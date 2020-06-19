# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

archivo_db = "./prueba.chappie"
archivo_db.path.delete()

#-------------------------------------------------------------------------------------------

# ver progreso de generacion (ideal para BD grandes)
def ver_progreso_joder(self):
	console.clear()
	print "progreso de creacion: {progress}% | {concurrent} / {end} | {size}".toF
	if not self.finish: return True

#-------------------------------------------------------------------------------------------

# creando BD tipo diccionario
dict_db = DelosData.create(keys=352770)
dict_db.timeout = 0.4
dict_db.export(archivo_db, ver_progreso_joder)
