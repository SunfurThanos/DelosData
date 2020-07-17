# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

# design dictionary type BD
dict_db = DelosData.create(keys=1000)

#-------------------------------------------------------------------------------------------

# predict the maximum weight you will have (does not include values)
print dict_db.prediction_size()

#-------------------------------------------------------------------------------------------

# predict the maximum weight you will have (including values)
print dict_db.prediction_size(size_items=80)

