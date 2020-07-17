# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

file_sample = "./file_sample.xD"
file_sample.path.delete()

#-------------------------------------------------------------------------------------------

# create BD
dict_db = DelosData.create(keys=1000)
dict_db.export(file_sample)

#-------------------------------------------------------------------------------------------

# import BD
dict_db = DelosData.open(file_sample)

#-------------------------------------------------------------------------------------------

key  = "25.969.358"
item = "NAMES:Andrade Echarry:LOCALHOST:_3X709ZHnD2dkCPUHQTdBWU2B0dYnkRbjHwz3pMTv40"

#-------------------------------------------------------------------------------------------

# insert key
dict_db.add(key, item)

#-------------------------------------------------------------------------------------------

# doing performance test (automatic)
value, seconds = dict_db.get(key, time=True)

print "%s seconds" % seconds.float(4)
print "%s milliseconds" % seconds.toMs()
print "%s nanoseconds"  % seconds.toNs().xfloat()
