# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

file_sample = "./sample_nlp.xD"
file_sample.path.delete()

#-------------------------------------------------------------------------------------------

# create BD
dict_db = DelosData.create(keys=1000)
dict_db.export(file_sample)

#-------------------------------------------------------------------------------------------

# import BD
dict_db = DelosData.open(file_sample)

#-------------------------------------------------------------------------------------------

identification_card = "25.969.358"
new_profile         = "NAMES:Andrade Echarry:LOCALHOST:_3X709ZHnD2dkCPUHQTdBWU2B0dYnkRbjHwz3pMTv40"

#-------------------------------------------------------------------------------------------

# insert llave
dict_db.add(identification_card, new_profile)

#-------------------------------------------------------------------------------------------

# doing performance test (manual)
start_time = Application.time
dict_db.get(identification_card)
seconds = Application.time - start_time

print "%s seconds" % seconds.float(4)
print "%s milliseconds" % seconds.toMs()
print "%s nanoseconds"  % seconds.toNs().xfloat()
