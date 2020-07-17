
DelosData 0.6
=============

API for Python to create dictionary type files (key + value), with unique and innovative properties that allow you to find a key instantly on any type of computer, unlike [Redis](https://aws.amazon.com/en/redis/) DelosData provides cross-platform, portable, simple, efficient and productive writing, DelosData is your best option for large volumes of data, more than an alternative.

*What is instantaneous speed?* In my opinion, if your algorithm in all the N variants always took from 0.03 to 180 milli-seconds, then we are talking about an excellent constant speed marker, so the speed of a software algorithm or per CPU chip, they have different requirements, because their nature is not the same for the N cases where they will interact.

---

> What problems does DelosData solve?

**Data security** Without the keys, basic information + encrypted items you cannot access the data that is stored in the file, if the BD is stolen no Hacker will be able to violate it, for the first time your company data will be 100 % safe.

**Productivity** Thanks to the fact that all the keys are kept in a single file on disks or SSDs and not in RAM, any user can easily transport or recover the data unlike [Redis](https://aws.amazon.com/es/redis/).

**Performance** For example, now Facebook could access a user's log data in a file that has more than 300 million keys, in just 0.6 milli-seconds from a simple home computer that has at least: single core processor, 80GB disk and 256MB RAM.

**Compression** The structure of a DelosData DB is conditioned so that it can be compressed with `7z` with a compression rate of 14% or more, making it easy to backup or transfer from one server to another, something that `Redis` cannot offer you.

---

> usage example for the NLP

Creating dictionary for 2 million words

```python
import DelosData

file_BD = "./NLP words.xD"
dict_db = DelosData.create(keys=2000000)
dict_db.export(file_BD)
```

Opening file and inserting a new key, `how to know if a key exists?`, Every time you insert a key, the system automatically detects whether it exists or not! To avoid corruption events!, DelosData is ideal in NLP for tasks like, `Byte Pair Encoding` & `Token embeddings`

```python
import DelosData

dict_db         = DelosData.open("./NLP words.xD")
word            = 'Tyranny'
vector_raw      = 0.37484443789236456545315
vector_compress = vector_raw.toCompress()
dict_db.add(word, vector_compress)
```

If you have already opened or reopened the file (BD) you can read a key, which has been inserted

```python
print dict_db.get('Tyranny').toDecompress()
```

How to close the BD manually?

```python
dict_db.close()
```

DelosData is productive and easy to use. Did you like it, do you want more usage examples?

---

**consultation list** [see documentation](DOC.md).

---

**NOTE** This API only works in Python 2.7, in higher versions the support is not available for now until there are sponsors :)

## How to install DelosData?

*STEP 1*
- Make sure you have Python 2.7 installed

*STEP 2*
- Install the powerful Productivity FrameWork [DelosEgine] in Python 2.7 (https://github.com/SunfurThanos/DelosEngine-ES)

*STEP 3*
- You can now install DelosData in Python 2.7, by running the file [install.py](install.py)

*END*
- Congratulations you can now use DelosData in Python 2.7 :)

---

**License** [GNU GPL v3](http://www.gnu.org/licenses)

---

# How do i convert DelosData to portable?
Assuming you want to use DelosData in Python for web development and the `administrators` of the server you pay to host your web or ML project, they don't let you install new plugins for the Python interpreter, there is NO PROBLEM, that has a solution! You will see both DelosEngine and DelosData when installed, they are just simple `.pyc` files, so they can be easily transported.

*STEP 0*
- Install DelosEngine and DelosData on your personal computer :)

*STEP 1*
- You must find out where DelosEngine is installed

```python
print (delos.__file__)
```

*STEP 2*
- Copy the `DelosEngine.pyc` file to your project directory

*STEP 3*
- You must find out where DelosData is installed

```python
import DelosData
print (DelosData.__file__)
```

*STEP 4*
- Copy the `DelosData.pyc` file to your project directory


*FINAL STEP*

Now we import DelosEngine and DelosData in the `$ main.py` of your project, does the order matter ?, you will see DelosEngine is a! Program that rebels against" good "Python practices !, so the import order is worth Much, what happens internally when I import DelosEngine ?, all its functions will remain in memory `memory allocated to the Python interpreter that is running your application`, therefore when you import DelosData it will automatically inherit the DelosEngine functions that are in the shared workspace,! making DelosEngine and DelosData run anywhere !, with this you save the day, using a new technology and without begging changes to third parties :)

```python
import DelosEngine
import DelosData

file_BD = "./BD_de_prueba.xD"
dict_db = DelosData.create(keys=1000)
dict_db.export(file_BD)

key     = "!I'm hungry :(!"
dict_db = DelosData.open(file_BD)
dict_db.add(key, "Tirania")

print dict_db.get(key)
```

---

> ¿tengo una pagina o proyecto Web, que uso le puedo dar a tu DelosData?

1. Use it as if it were an XML, JSON or TXT.

2. If you are creating an interactive Chatbot, you can use DelosData to save the data related to the statistics of the selected character, story abandonment point, completed story, video link reception, etc.

3. Statistics of web users! Not even painted for forums and social networks !.

4. login data, useful for banks & social networks.

5. monitoring and follow-up of road cameras among other branches.

---

## Do you like DelosData, do you want to help the project?

- If you consider that the DelosData is worth something for your day to day, you can send me a remittance, with which you will make the project remain FREE & FREE! ...

you are a large, small, Freelance company, are you interested in this project ?, let me know !, this project needs sponsors who want to help the project with advertising, donations and suggestions, they will be included in the credits of the project as the HEROES: )

*developer email*: hormigence123@gmail.com | sunfur@protomail.com

---

**NOTE** Without sponsors the development will be stagnant in this version :(

---

## Herramientas en desarrollo en DelosData

**Python3** Support so it can be run in Python3

**Reliability** Ensuring 1,000% integrity when new data is inserted, the idea is to preserve and secure the data without increasing the size of the index that stores the jumpers.

**SSB** Less weight of the index

**CUSTOM 1** Support to modify the item values ​​of the already integrated keys.

**CUSTOM 2** Customizable size for items.

**CrytoG** To illegally encode an item of a certain key, but by means of a password, that is, the characters of the key of the item itself will be used as a password to encode and decode, while maintaining the original length of the data (item), the algorithm itself will never know if the correct password has actually been used, with which a Hacker attacker will never know if it is close or not to decrypt the stolen data, this algorithm accepts a password of INFINITE length, not even if you have the source code of the program that encodes or decodes the algorithm can be hacked.

**Find G8** Support for searching by numerical concurrency.

**CUSTOM 3** The data of the items will keep their original data structure, therefore if you put a list of value, when you generate a query it will return the data in list format, with which professional queries can be made.

**Auto-page** The system is told what is the maximum weight per page (file), that way we can have dictionaries divided into several files, useful for multiple purposes.

**SuperDelete** Already with the created pagination tool it is feasible to erase keys + value, or only the values ​​of the keys, the almost instantaneous deletion will depend on the pagination value established and the power of the computer.

**Spider G9** technology to quantify dynamic memory positions, this will allow advanced concurrency searches such as, `the color cat * walked * the roof`, the system will iterate all the keys that meet that concurrency pattern , this will allow the processing of big data to be a game for children, since the searches will be very fast linear regardless of the number of keys in the dictionary, first the system generates an Array where all the memory positions ranges where the keys related to the search pattern, that procedure if it is instantaneous, the range iteration procedure if it is linear.

**Re-write** DelosData is made in Python from 0 with an amazing and enviable performance, even so the idea is to re-code the DelosData kernel in C ++, that way the performance and query speed will be 4 times faster In this way the project will be 100% complete.

---

*Sunfur Thanos* If you learn to be open to adapt, you will be invincible!

---

## ¿Foro de preguntas en español?

- Para dirigir sus comentarios, ideas de desarrollo, dudas o hablar de Python, puede hacerlo por medio del chat para programadores en español.

*sala IRC*: #python-es | #python-es_OFFTOPIC
