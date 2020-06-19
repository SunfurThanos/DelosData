# coding: utf-8

"""
  Autor: Sunfur Thanos

  Pais : Venezuela

  Contacto : hormigence123@gmail.com

  Licencia : GNU GPL v3 <http://www.gnu.org/licenses/>

  Copyright (C) 2020 Sunfur Thanos. All rights reserved.

"""

__version__ = 0.6

__build__   = (__version__, "19/06/2020", "06:02:15 AM")

__author__  = 'Sunfur Thanos'

__email__   = 'hormigence123@gmail.com'

#/

from funcion_genericas import *

#/

HEADER_LEN           = 40
hiper_jumper_limited = 12

#/

### predecir peso del diccionario
# $(to-onelinerize)
def function_size_max(self, size_items=0x1):
	dockerZ = self.get_calc_preHash
	layer1 = dockerZ.calc_size_index_main + (dockerZ.REAL_max_cols*(7+4))
	if size_items > 1:
		layer2 = (layer1 + (dockerZ.REAL_max_cols*size_items)).size().join(" ")
	else:
		layer2 = layer1.size().join(" ")
	return {
		"index"  : (dockerZ.calc_size_index_main).size().join(" "),
		"insert" : layer2
	}

#/

### crear BD de tipo diccionario
def function_export(self, archivo, function=False):

	if archivo.path.isfile:
		return False

	dockerZ = self.get_calc_preHash

	buffsize = 60000
	if dockerZ.calc_size_index_main > buffsize:
		buffsize = buffsize * 128

	FILE = archivo.path.save(mode="+")

	docker = NameSpace()
	docker.end        = dockerZ.calc_size_index_main
	docker.progress   = 0x0
	docker.concurrent = 0x0
	docker.size       = "..."
	docker.finish     = False
	docker.body_bytes = self.chuck_null * buffsize

	if function:
		set_timeout(self.timeout, function, docker)

	while True:
		peso = archivo.path.size.value
		progreso = "%0.2f" % Math("{peso} * 100 / {end}".toF, prec=4)
		docker.progress = max(progreso, 100.0)
		docker.concurrent = min(peso, docker.end)
		docker.size = peso.size().join(" ")

		if peso > dockerZ.calc_size_index_main:
			FILE.cut_from(dockerZ.calc_size_index_main)
			self.size_db = archivo.path.size.info.join(" ")
			peso = archivo.path.size.value
			progreso = "%0.2f" % Math("{peso} * 100 / {end}".toF, prec=4)
			docker.progress = max(progreso, 100.0)
			docker.concurrent = peso
			docker.size = peso.size().join(" ")
			funccion_create_HEADER_MAIN(FILE, dockerZ.REAL_max_cols)
			FILE.close()
			docker.finish = True
			break

		FILE.save( docker.body_bytes )

	return True

#//

### crear HEADER_MAIN
# $(to-onelinerize)
def funccion_create_HEADER_MAIN(FILE, REAL_max_cols):
	save_header_MAIN(FILE, 0x0)
	save_header_count_keys_support(FILE, REAL_max_cols)

#/

### insertar una llave
def function_add_key(self, key, value):

	if self.isClose:
		return "file-close"

	if value.len > 9999: # el item sobre-pasa la longitud permitida
		return "item-size"

	DATA_ITEM = value.toS
	FILE      = self.FILE

	dockerZ = self.get_calc_preHash

	if read_header_MAIN(FILE) == dockerZ.REAL_max_cols: # la tabla esta "llena"
		return "table-UP"

	def toHash(cadena):
		Hash = cadena.hash * dockerZ.len_name_cols
		return Hash % (dockerZ.max_cols*dockerZ.id_hack_chuck_DISC) * dockerZ.len_name_cols

	llave_word = key
	TB   = toHash(llave_word) + HEADER_LEN

	# insertando (jumpers + llaves) comprobando que los jumper no exista si existe se recalcula
	if isJumper(FILE, TB):

		# detectando si la LLAVE (name) existe
		if READ_decode(llave_word, FILE, TB, dockerZ.len_name_cols, hiper_jumper_limited) != False:
			return "EXIST"

		# recalculando posición para la nueva llave
		is_recalc_hashs = False
		new_hash = 0x0008
		lord_craft = 0x0
		for value in xrange(2, hiper_jumper_limited):
			new_hash = TB+(dockerZ.len_name_cols*value)
			if not isJumper(FILE, new_hash):
				is_recalc_hashs = True
				lord_craft = value
				break

		if new_hash.toPositive() > dockerZ.calc_size_index_main:
			print "sorry. el hash es superior al peso del index :2"
			return "ERROR-CRICAL"

		if not is_recalc_hashs:
			print "no se pudo recalcular el hash"
			return "ERROR-CRICAL"

		if isColition(FILE, new_hash):
			print "sorry. hash en colition :2"
			return "ERROR-CRICAL"

		numero = read_header_MAIN(FILE) + 1
		save_header_MAIN(FILE, numero)

		FILE.instance.seek(0, 2)
		final_archivo = FILE.get_cursor
		index_header = COMPRIMIR(final_archivo.toS + "%04d" % (DATA_ITEM.len), 10)

		FILE.cursor(new_hash)
		FILE.save(index_header)

		ENCODE = lord_craft.toS + hashCode(llave_word)
		item_header = COMPRIMIR(ENCODE, 7) + DATA_ITEM + "\x00\x00"

		FILE.cursor(final_archivo)
		FILE.save(item_header)
	else:
		numero = read_header_MAIN(FILE) + 1
		save_header_MAIN(FILE, numero)

		FILE.instance.seek(0, 2)
		final_archivo = FILE.get_cursor
		index_header = COMPRIMIR(final_archivo.toS + "%04d" % (DATA_ITEM.len), 10)

		FILE.cursor(TB)
		FILE.save(index_header)

		ENCODE = "0" + hashCode(llave_word)
		item_header = COMPRIMIR(ENCODE, 7) + DATA_ITEM + "\x00\x00"

		FILE.cursor(final_archivo)
		FILE.save(item_header)

	return "YES" # llave agregada exitosamente

#/

### detectar llave insertada
# $(to-onelinerize)
def function_get_key(self, key, time=False):

	if time:
		import time
		start_time = time.time()
		value = self.get(key)
		seconds = time.time() - start_time
		return value, seconds

	if self.isClose:
		return "file-close"

	FILE = self.FILE

	dockerZ = self.get_calc_preHash

	def toHash(cadena):
		Hash = cadena.hash * dockerZ.len_name_cols
		return Hash % (dockerZ.max_cols*dockerZ.id_hack_chuck_DISC) * dockerZ.len_name_cols

	llave_word = key
	TB = toHash(llave_word) + HEADER_LEN

	# detectando si la LLAVE (name) existe
	DATA = READ_decode(llave_word, FILE, TB, dockerZ.len_name_cols, hiper_jumper_limited)

	# retornando resultado
	return DATA if DATA else False

#//

### funcion para ver cuantas llaves se han insertado
# $(to-onelinerize)
@property
def function_get_count_insert(self):
	return read_header_MAIN(self.FILE)

#/

### cerrar archivo de BD
# $(to-onelinerize)
def function_close(self):
	self.FILE.close()
	self.isClose = True

#/

### funcion para importar diccionario
# $(to-onelinerize)
def open(archivo):

	if not archivo.path.isfile:
		return False

	# creando clase privada
	docker = NameSpace()

	# creando parametros privados
	docker.FILE = archivo.path.save(mode="+")
	docker.keys = read_header_count_keys_support(docker.FILE)
	docker.name_space = "<DelosData at WestWorld/Dolores/host/open>"
	docker.get_calc_preHash = calc_preHash(docker, HEADER_LEN)
	docker.isClose = False
	docker.include({"close":function_close})
	docker.include({"add":function_add_key})
	docker.include({"get":function_get_key})
	docker.include({"get_inserts":function_get_count_insert})
	return docker

#/

### funcion para crear diccionario
# $(to-onelinerize)
def create(keys=False):
	if keys == False:
		return False

	# creando clase privada
	docker = NameSpace()

	# creando parametros privados
	docker.keys = keys
	docker.chuck_null = b"\x00"
	docker.timeout = 0.2
	docker.size_db = False
	docker.name_space = "<DelosData at WestWorld/Dolores/host/create>"
	docker.get_calc_preHash = calc_preHash(docker, HEADER_LEN)
	docker.include({"prediction_size":function_size_max})
	docker.include({"export":function_export})
	return docker
