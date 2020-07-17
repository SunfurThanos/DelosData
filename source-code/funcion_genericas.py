# coding: utf-8

"""
  Autor: Sunfur Thanos

  Pais : Venezuela

  Contacto : hormigence123@gmail.com

  Licencia : GNU GPL v3 <http://www.gnu.org/licenses/>

  Copyright (C) 2020 Sunfur Thanos. All rights reserved.

"""

#/

# $(to-onelinerize)
def set_dimension(valor):
	"""hack dimension de anti-colision: suaviza las dimensiones cuanticas del vector hash para posiciones del disco en cache"""
	if valor.len > 3:
		kana_coo = 1000
	else:
		if valor.len > 1:
			kana_coo = 100
		else:
			kana_coo = 50

	kana = kana_coo
	while True:
		kana+=(kana_coo*2)
		if kana > valor: break

	if kana >= 700000:
		return 10, kana

	if kana > 10000:
		return 10, valor

	if kana > 1000:
		return 4, kana + 800

	if kana > 100:
		return 2, kana + 80

	return 2, valor

#/

# $(to-onelinerize)
def calc_preHash(self, HEADER_LEN):
	"""calcular pre-hash parameters: creando cache seguro (hash::pointer*)"""
	max_cols = self.keys
	REAL_max_cols = max_cols
	jumper_intel, max_cols = set_dimension(max_cols)

	user_maxlen_nameCols = 10
	len_name_cols = user_maxlen_nameCols

	id_hack_chuck_DISC = jumper_intel
	calc_size_index_main = (((max_cols*id_hack_chuck_DISC)*(len_name_cols)) + (HEADER_LEN) )

	docker = NameSpace()
	docker.max_cols = max_cols
	docker.REAL_max_cols = REAL_max_cols
	docker.len_name_cols = len_name_cols
	docker.id_hack_chuck_DISC = id_hack_chuck_DISC
	docker.calc_size_index_main = calc_size_index_main

	return docker

#/

# $(to-onelinerize)
def COMPRIMIR(cadena, intel_struct):
	"""funcion generica para comprimir cadenas de numeros"""
	comprimido = cadena.toCompress()
	return ("\x00"*intel_struct)[comprimido.len:] + comprimido

#//

# $(to-onelinerize)
def DESCOMPRIMI(cadena):
	"""funcion generica para descomprimir cadenas de numeros"""
	return cadena.strip("\x00").toDecompress()

#/

# $(to-onelinerize)
def read_header_MAIN(FILE):
	"""funcion generica para leer el HEADER_MAIN: permite leer el header del archivo (dict:BD*)"""
	FILE.cursor(0x0)
	datos = FILE.read(6)[-1]
	return DESCOMPRIMI(datos).toN

#//

# $(to-onelinerize)
def save_header_MAIN(FILE, numero):
	"""funcion generica para modificar el HEADER_MAIN <- (dict:BD*)"""
	FILE.cursor(0x0)
	FILE.save( COMPRIMIR(numero, 6) )

#/

# $(to-onelinerize)
def save_header_count_keys_support(FILE, REAL_max_cols):
	"""funcion para el HEADER_MAIN: guardar cantidad de llaves soportadas"""
	FILE.cursor(0x7)
	FILE.save(COMPRIMIR(REAL_max_cols, 6))

#//

# $(to-onelinerize)
def read_header_count_keys_support(FILE):
	"""funcion para el HEADER_MAIN: leer cantidad de llaves soportadas"""
	FILE.cursor(0x7)
	datos = FILE.read(6)[-1]
	return DESCOMPRIMI(datos).toN

#/

# $(to-onelinerize)
def isJumper(FILE, TB):
	"""detectar si un jumper existe (jumper -> key_pos*): jumper es posicion de memoria donde se guarda, la posicion codificada del item + (name_key_hash) de una correspondiente llave"""
	FILE.cursor(TB)
	DATA = DESCOMPRIMI(FILE.read(10)[1])
	return DATA if any(DATA) else False

#/

# $(to-onelinerize)
def hashCode(string):
	"""convertir KEY to (hash:ID*): permite convertir el nombre de la llave a (name_key_hash)"""
	prevHash = 0x0
	for currVal in "$Sunfur$"+string+len(string).toS: # "$Sunfur$"+string+"$Sunfur$":
		prevHash = ((prevHash << 5) - prevHash) + ord(currVal)
	return prevHash.toS[-12:]

#/

# $(to-onelinerize)
def isColition(FILE, TB):
	"""detectar si un jumper esta en colisión"""
	FILE.cursor(TB+9)
	return FILE.read(1)[-1] != b"\x00"

#/

def decodificar_llave(llave_word, FILE, TB, len_name_cols, hiper_jumper_limited):
	"""decodificando jumper (mostrando item): permite validar si una llave existe y extrae su valor (ITEM)"""
	NUM_HASH     = False
	index_header = isJumper(FILE, TB)

	ENCODE = "0" + hashCode(llave_word)

	if index_header:
		try:
			index_header[:-4].toN
		except:
			return 0x492F4B61, "Sorry. BD corrupta"

	if index_header:
		pointer_pos = index_header[:-4].toN
		len_item    = index_header[-4:].toN
		FILE.cursor(pointer_pos)
		NUM_HASH = DESCOMPRIMI(FILE.read(7)[-1])
		FILE.cursor(pointer_pos+7)
		DATA_ITEM = FILE.read(len_item)[-1]

	if (NUM_HASH == ENCODE):
		return True, DATA_ITEM
	else:
		active = False
		for value in xrange(2, hiper_jumper_limited):
			new_hash = TB+(len_name_cols*value)
			FILE.cursor(new_hash)
			index_header = isJumper(FILE, new_hash)

			if index_header:
				try:
					pointer_pos = index_header[:-4].toN
					len_item    = index_header[-4:].toN
					FILE.cursor(pointer_pos)
				except:
					continue

				ENCODE = value.toS + hashCode(llave_word)

				NUM_HASH = DESCOMPRIMI(FILE.read(7)[-1])
				FILE.cursor(pointer_pos+7)
				DATA_ITEM = FILE.read(len_item)[-1]

				if (NUM_HASH == ENCODE):
					active = True
					return True, DATA_ITEM

	return False, "Sorry. la llave no existe"

#//

# $(to-onelinerize)
def READ_decode(llave_word, FILE, TB, len_name_cols, hiper_jumper_limited):
	"""funcion complementaria para leer una llave"""

	find_yes = False
	valid, x = decodificar_llave(llave_word, FILE, TB, len_name_cols, hiper_jumper_limited)

	if valid == 0x492F4B61:
		exit(x)

	if valid:
		find_yes = True
		return x

	return False
