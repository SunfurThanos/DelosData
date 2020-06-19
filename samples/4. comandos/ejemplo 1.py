# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

salida = "./NLP words.xD"
salida.path.delete()

#-------------------------------------------------------------------------------------------

# crear BD
dict_db = DelosData.create(keys=1000)
dict_db.export(salida)

#-------------------------------------------------------------------------------------------

# importar BD
dict_db = DelosData.open(salida)

#-------------------------------------------------------------------------------------------

# datos a guardar
palabra = 'Tirania'
vector_raw = 0.37484456
vector_comprimido = vector_raw.toCompress()

#-------------------------------------------------------------------------------------------

# insertando llave
validar = dict_db.add(palabra, vector_comprimido)

#-------------------------------------------------------------------------------------------

# consultar valor guardado
print dict_db.get(palabra).toDecompress()

# total de llaves permitidas a insertar
print dict_db.keys

# total de llaves insertadas
print dict_db.get_inserts

#-------------------------------------------------------------------------------------------

# cerrando lectura de BD
dict_db.close()

#-------------------------------------------------------------------------------------------

# detectando si la BD esta cerrada
print dict_db.isClose

print dict_db.get(palabra)
