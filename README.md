
DelosData 0.6
=============

API para Python para crear archivos de tipo diccionario (llave+valor), con propiedades únicas e innovadoras que permiten encontrar una llave de manera instantánea en cualquier tipo de ordenador, a diferencia de [Redis](https://aws.amazon.com/es/redis/) DelosData proporciona una escritura multiplataforma, portable, sencilla, eficaz y productiva, DelosData más que una alternativa es tu mejor opción para grandes volúmenes de datos.

*Que es velocidad instantánea?* según mi criterio, si tu algoritmo en todas las N variantes siempre tardara desde 0,03 a 180 mili-segundos, entonces hablamos de un excelente marcador de velocidad constante, así que la velocidad de un algoritmo por software o por chip de CPU, tienen requerimientos diferentes, porque su naturaleza no es la misma para los N casos en donde interactuaran.

---

> ¿Que problemas resuelve DelosData?

**Seguridad de datos** Sin las llaves, información básica + items codificados no se puede acceder a los datos que están guardados en el archivo, si la BD es robada ningún Hacker podrá violentarla, por primeras vez los datos de tu empresa estarán 100% seguros.

**Productividad** Gracias a que todas las llaves se guardan en un único archivo en discos o SSD y no en la RAM, puede fácilmente cualquier usuario transportar o recuperar los datos a diferencia de [Redis](https://aws.amazon.com/es/redis/).

**Rendimiento** Por ejemplo ahora Facebook, podría acceder a los datos de logeo de un usuario en un archivo que tenga más de 300 millones de llaves, en solo 0.6 milli-segundos desde un simple ordenador domestico, que tenga como mínimo: un procesador de un solo núcleo, 80 GB de disco y 256 MB de RAM.

**Compresión** La estructura de una BD de DelosData esta acondicionada para que pueda ser comprimida con `7z` con una tasa de compresión de 14% o más, haciendo que sea fácil el respaldo o la transferencia de un servidor a otro, algo que `Redis` no puede ofrecerte.

---

> ejemplo de uso para el NLP

Creando diccionario para 2 millones de palabras

```python
import DelosData

archivo_BD = "./NLP words.xD"
dict_db = DelosData.create(keys=2000000)
dict_db.export(archivo_BD)
```

Abriendo archivo y insertando una nueva llave, `¿como saber si una llave existe?`, cada vez que insertas una llave, el sistema detecta automáticamente si existe o no !para evitar eventos de corrupción!, DelosData es ideal en NLP para tareas como, `Byte Pair Encoding` & `Token embeddings`

```python
import DelosData

dict_db           = DelosData.open("./NLP words.xD")
palabra           = 'Tirania'
vector_raw        = 0.37484443789236456545315
vector_comprimido = vector_raw.toCompress()
dict_db.add(palabra, vector_comprimido)
```

Si ya tienes abierto o abres nuevamente el archivo (BD) puedes leer una llave, que haya sido insertada

```python
print dict_db.get('Tirania').toDecompress()
```

¿como cerrar la BD de forma manual?

```python
dict_db.close()
```

DelosData es productivo y fácil de usar, ¿Te gusto quieres más ejemplos de uso?, !pues que esperas descarga DelosData y lee los ejemplos de la carpeta [samples](samples).

---

**lista de consulta** [ver documentación](DOC.md).

---

**NOTA** Esta API solo funciona en Python 2.7, en versiones superiores el soporte no esta disponible por ahora hasta que haya patrocinadores :)

## ¿Como instalar DelosData?

*PASO 1*
- Asegúrese de tener instalado Python 2.7

*PASO 2*
- Instale en Python 2.7 el Potente FrameWork de productividad [DelosEgine](https://github.com/SunfurThanos/DelosEngine-ES)

*PASO 3*
- Ya puedes instalar DelosData en Python 2.7, ejecutando el archivo [install.py](install.py)

*FIN*
- Felicidades ya puedes usar DelosData en Python 2.7 :)

---

**Licencia** [GNU GPL v3](http://www.gnu.org/licenses)

---

# ¿como convierto DelosData a portable?
Suponiendo que deseas usar DelosData en Python para desarrollo web y los `administradores` del servidor de donde pagas para hospedar tu proyecto web o ML, no te dejan instalar nuevos complementos para el interprete de Python, !NO hay PROBLEMA, eso tiene solución!, veras tanto DelosEngine y DelosData al ser instalados, solo son simples archivos `.pyc`, por lo cual pueden ser fácilmente transportados.

*PASO 0*
- Instala DelosEngine y DelosData en tu computadora personal :)

*PASO 1*
- Debes averiguar donde esta instalado DelosEngine

```python
print (delos.__file__)
```

*PASO 2*
- Copia el archivo `DelosEngine.pyc` al directorio de tu proyecto

*PASO 3*
- Debes averiguar donde esta instalado DelosData

```python
import DelosData
print (DelosData.__file__)
```

*PASO 4*
- Copia el archivo `DelosData.pyc` al directorio de tu proyecto


*PASO FINAL*

Ahora importamos en el `$main.py` de tu proyecto a DelosEngine y DelosData, ¿el orden importa?, veras DelosEngine es un !programa que se rebela ante las "buenas" practicas de Python!, así que el orden de importación vale mucho, ¿que pasa internamente cuando importo DelosEngine?, todas sus funciones quedaran en memoria `memoria asignada al interprete de Python que esta corriendo tu aplicación`, por ende cuando importas DelosData este va a heredar de forma automática las funciones de DelosEngine que están en el espacio de trabajo compartido, !haciendo que DelosEngine y DelosData corra donde sea!, ya con esto salvas el día, usando una nueva tecnología y sin mendigar cambios a terceros :)

```python
import DelosEngine
import DelosData

archivo_BD = "./BD_de_prueba.xD"
dict_db    = DelosData.create(keys=1000)
dict_db.export(archivo_BD)

llave = "!Tengo Hambre :(!"
dict_db = DelosData.open(archivo_BD)
dict_db.add(llave, "Tirania")

print dict_db.get(llave)
```

---

> ¿tengo una pagina o proyecto Web, que uso le puedo dar a tu DelosData?

1. Usalo como si fuera un XML, JSON o TXT.

2. Si estas creando un Chatbot interactivo, puedes usar DelosData para guardar los datos relativos a las estadísticas de personaje seleccionado, punto de abandono de la historia, historia completada, recepción de enlace a vídeo, etc.

3. Estadísticas de usuarios web !que ni pintado para foros y redes sociales!.

4. datos de logeo, útil para bancos & redes sociales.

5. monitoreo y seguimiento de cámaras viales entre otras ramas.

---

## ¿Foro de preguntas?

- Para dirigir sus comentarios, ideas de desarrollo, dudas o hablar de Python, puede hacerlo por medio del chat para programadores en español.

*sala IRC*: #python-es | #python-es_OFFTOPIC

---

## ¿Te gusta DelosData, quieres ayudar al proyecto?

- Si consideras que el DelosData vale algo para tu día a día, puedes enviarme una remesa,
con lo cual harás que el proyecto siga siendo ¡GRATUITO & LIBRE!...

eres una empresa grande, pequeña, Freelance, ¿te interesa este proyecto?, !házmelo saber!, este proyecto necesita patrocinadores que deseen ayudar al proyecto con publicidad, donativos y sugerencias, los mismos serán incluidos en los créditos del proyecto como los HÉROES :)

*correo del desarrollador*: hormigence123@gmail.com | sunfur@protomail.com

---

**NOTA** Sin patrocinadores el desarrollo quedara estancado en esta versión :(

---

## Herramientas en desarrollo en DelosData

**Python3** Soporte para que pueda ser ejecutado en Python3

**Fiabilidad** Asegurar al 1.000% la integridad cuando se insertan nuevos datos, la idea es preservar y asegurar los datos sin aumentar el tamaño del index que almacena los jumpers.

**SSB** Menor peso del index

**CUSTOM 1** Soporte para modificar los valores items de las llaves ya integradas.

**CUSTOM 2** Tamaño personalizable para los items.

**CrytoG** Codificar de manera ilegible un item de una determinada llave, pero por medio de una contraseña, es decir se utilizara los caracteres de la llave del propio item como contraseña para codificar y decodificar, pero manteniendo la longitud original de los datos (item), el propio algoritmo nunca sabrá si realmente se ha utilizado la contraseña correcta, con lo cual un atacante Hacker nunca sabrá si esta cerca o no de descifrar los datos robados, este algoritmo acepta una contraseña de longitud INFINITA, ni-siquiera si posees el código fuente del programa que codifica o decodifica se podrá hackear el algoritmo.

**Find G8** Soporte para hacer búsquedas por concurrencia numérica.

**CUSTOM 3** Los datos de los items conservaran su estructura de datos original, por ende si de valor colocas una lista, cuando generes una consulta te devolverá los datos en formato de lista, con cual se puede realizar consultas profesionales.

**Auto-page** Se le dice al sistema cual es el peso máximo por pagina (archivo), de esa manera podemos tener diccionarios dividido en varios archivos, útil para múltiples propósitos.

**SuperDelete** Ya con la herramienta de paginación creada es factible el borrado de llaves + valor, o solamente los valores de las llaves, el borrado casi instantáneo dependerá del valor de paginación establecida y de la potencia del ordenador.

**Spider G9** tecnología para cuantificar posiciones de memoria dinámica, esto permitirá hacer búsquedas por concurrencia avanzadas como por ejemplo, `el gato de color*caminaba*el tejado`, el sistema iterara todas las llaves que cumplan con ese patrón de concurrencia, esto permitirá que el procesado del big data sea un juego para niños, ya que las búsquedas serán muy rápidas lineales sin importar la cantidad de llaves del diccionario, primero el sistema genera un Array donde están todos los rangos posiciones de memoria donde se encuentra las llaves relacionadas con el patrón de búsqueda, ese procedimiento si es instantáneo, el procedimiento de iteración de rangos si es lineal.

**Re-escritura** DelosData esta hecho en Python desde 0 con un rendimiento asombroso e envidiable, aun así la idea es re-codificar el núcleo de DelosData en C++, de esa manera el rendimiento y velocidad de consulta sera 4 veces más rápido, de esta manera el proyecto estará terminado al 100%.

---

*Sunfur Thanos* Si aprendes a estar abierto para adaptarte ¡seras invencible!
