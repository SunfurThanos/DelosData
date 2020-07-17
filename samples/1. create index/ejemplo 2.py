# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

file_db = "./sample.chappie"
file_db.path.delete()

#-------------------------------------------------------------------------------------------

# creating dictionary type DB
dict_db  = DelosData.create(keys=1000)
validate = dict_db.export(file_db)

#-------------------------------------------------------------------------------------------

if validate:
	print "the BD was created: {size_db}".toF
else:
	print "cannot create, file already exists"

#-------------------------------------------------------------------------------------------

"""

NOTE: the BD cannot exceed (93 GB), otherwise the Index will collapse and cause serious writing and reading errors.
"""
