# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

# diseñar BD tipo diccionario
dict_db = DelosData.create(keys=1000)

#-------------------------------------------------------------------------------------------

# predecir el peso maximo que tendra (no incluye valores)
print dict_db.prediction_size()

#-------------------------------------------------------------------------------------------

# predecir el peso maximo que tendra (incluyendo valores)
print dict_db.prediction_size(size_items=80)

