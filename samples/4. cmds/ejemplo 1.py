# coding: utf-8

import DelosData

#-------------------------------------------------------------------------------------------

setWorkingDir()

#-------------------------------------------------------------------------------------------

file_sample = "./NLP words.xD"
file_sample.path.delete()

#-------------------------------------------------------------------------------------------

# create BD
dict_db = DelosData.create(keys=1000)
dict_db.export(file_sample)

#-------------------------------------------------------------------------------------------

# import BD
dict_db = DelosData.open(file_sample)

#-------------------------------------------------------------------------------------------

# data to save
word = 'Tyranny'
vector_raw = 0.37484456
vector_compress = vector_raw.toCompress()

#-------------------------------------------------------------------------------------------

# insert key
validate = dict_db.add(word, vector_compress)

#-------------------------------------------------------------------------------------------

# check saved value
print dict_db.get(word).toDecompress()

# Total of keys allowed to insert
print dict_db.keys

# total of inserted keys
print dict_db.get_inserts

#-------------------------------------------------------------------------------------------

# closing BD read
dict_db.close()

#-------------------------------------------------------------------------------------------

# detecting if the DB is closed
print dict_db.isClose

print dict_db.get(word)
