
Create BD
=========

**create (keys = number)**
Lets create the BD, specifying how many keys it will have

**prediction\_size (size\_items = number) **
Lets make a prediction of how much the DB will weigh before being created

**size\_db**
You can show the weight of the generated DB.

**timeout = number**
Variable that allows specifying how much the update frequency will be for the progress function.

**export(file_db, func\_progress)**
Function to export the BB to a file `final creation of the BD`, you can specify the output file and the progress function, that is, you can assign a function and there show the generation progress, ideal for large BDs.

---

Insert keys
===========

**open (file_db)**
BD import function created

**add**
Lets you insert a key + value

**close()**
Close BD

**isClose**
Detect if the key has been inserted

**keys**
Numbers of keys allowed to insert

**get\_inserts**
Numbers of inserted keys

---

## Inserts-returns

**AND IT IS**
Key inserted correctly

**EXIST**
The key already exists

**table-UP**
The table (index) is full

**item-size**
The item overrides the allowed length

**ERROR-CRICAL**
Critical writing error

**file-close**
The file (BD) is closed

---

see inserted keys
=================

**get(key\_name, time=bool)**
Function to extract the value of a key, it is also possible to validate if the key does not exist

**close()**
Close BD

**isClose**
Detect if the key has been inserted

**keys**
Numbers of keys allowed to insert

**get\_inserts**
Numbers of inserted keys
