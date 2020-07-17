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

key  = "25.969.358"
item = "Andrade Echarry:localhost:_3js7RHbLSHKV13qUFCVIhb"

#-------------------------------------------------------------------------------------------

## insert
validate = dict_db.add(key, item)
if validate == "YES":
	print "successfully created profile"

#-------------------------------------------------------------------------------------------

validate = dict_db.add(key, item)
if validate == "EXIST":
	print "this profile already exists. Sorry"

#-------------------------------------------------------------------------------------------

"""

YES          : key inserted correctly

EXIST        : the key already exists

table-UP     : table (index) is full

item-size    : the item exceeds the allowed length

ERROR-CRICAL : critical writing error

file-close   : the file (BD) is closed

"""
