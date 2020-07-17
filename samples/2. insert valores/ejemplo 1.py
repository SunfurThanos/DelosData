# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

file_sample = "./file_sample.xD"
file_sample.path.delete()

#-------------------------------------------------------------------------------------------

# create BD
dict_db = DelosData.create(keys=4600)
dict_db.export(file_sample)

#-------------------------------------------------------------------------------------------

# import BD
dict_db = DelosData.open(file_sample)

#-------------------------------------------------------------------------------------------

## progress bar
docker = NameSpace()
docker.end = dict_db.keys
docker.concurrent = 0x0
docker.finish = False

def func_progress(docker):
	console.clear()
	progreso = "%0.2f" % Math("{concurrent} * 100 / {end}".toF, prec=4)
	print ("{progreso}%".toF, docker.concurrent, docker.end,)
	if not docker.finish: return True

set_timeout(0.7, func_progress, docker)

#-------------------------------------------------------------------------------------------

# inserting keys + values
for docker.concurrent in xrange(1, dict_db.keys+1):
	llave = "hello " + docker.concurrent.toS
	item  = "ITEM " + docker.concurrent.toS
	dict_db.add(llave, item)
docker.finish = True

#-------------------------------------------------------------------------------------------

"""

NOTE: the length of the values ​​(items) of the keys cannot exceed (9.7 Kbs)

NOTE: the keys can have an "INFINITE" length, the names of the keys are not saved in the dictionary, only their quantized spatial memory conversion, that is, each key (word) is converted to a memory position, in that position the numerical value (position) of its corresponding item is saved, in this way no one who does not know the keys will be able to obtain information from the DB.

"""
