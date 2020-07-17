# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

file_db = "./sample.chappie"
file_db.path.delete()

#-------------------------------------------------------------------------------------------

# see generation progress (ideal for large BD)
def func_sample_progress(self):
	console.clear()
	print "creation progress: {progress}% | {concurrent} / {end} | {size}".toF
	if not self.finish: return True

#-------------------------------------------------------------------------------------------

# creating dictionary type DB
dict_db = DelosData.create(keys=352770)
dict_db.timeout = 0.4
dict_db.export(file_db, func_sample_progress)
