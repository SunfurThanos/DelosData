# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

file = "./saludos.xD"
file.path.delete()

#-------------------------------------------------------------------------------------------

# create BD
dict_db = DelosData.create(keys=1000)
dict_db.export(file)

#-------------------------------------------------------------------------------------------

# import BD
dict_db = DelosData.open(file)

#-------------------------------------------------------------------------------------------

identification_card = "25.969.358"
new_profile         = "NAMES:Andrade Echarry:LOCALHOST:_3js7RHbLSHKV13qUFCVIhb"

#-------------------------------------------------------------------------------------------

# insert key
validar = dict_db.add(identification_card, new_profile)

#-------------------------------------------------------------------------------------------

# showing key item
data = dict_db.get(identification_card)
if data: print data.cut(":").group(2)

#-------------------------------------------------------------------------------------------

data = dict_db.get("26.111.456")
if data:
	print data.cut(":").group(2)
else:
	print "The required profile does not exist. Sorry"
