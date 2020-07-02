
Crear BD
========

**create(keys=number)**
Permite crear la BD, especificando cuantas llaves tendrá

**prediction\_size(size\_items=number)**
Permite hacer una predicción de cuanto pesara la BD antes de ser creada

**size\_db**
Podrás mostrar el peso de la BD generada.

**timeout = number**
Variable que permite especificar, cuanto sera la frecuencia de actualizacion para la funcion de progreso.

**export(file_db, func\_progress)**
Función para exportar la BB a un archivo `creación final de la BD`, puedes especificar el archivo de salida y la función de progreso, es decir puedes asignar una función y allí mostrar el progreso de generación, ideal para grandes BD.

---

Insertar llaves
===============

**open(file_db)**
Funcion para importar BD creada

**add**
Permite insertar una llave + valor

**close()**
Cerrar BD

**isClose**
Detectar si la llave ha sido insertada

**keys**
Numeros de llaves permitidas a insertar

**get\_inserts**
Numeros de llaves insertadas

---

## Inserts-returns

**YES**
Llave insertada correctamente

**EXIST**
La llave ya existe

**table-UP**
La tabla (index) esta llena

**item-size**
El item sobre-pasa la longitud permitida

**ERROR-CRICAL**
Error critico de escritura

**file-close**
El archivo (BD) esta cerrada

---

ver llaves insertadas
=====================

**get(key\_name, time=bool)**
Funcion para extraer el valor de una llave, tambien es posible validar si la llave no existe

**close()**
Cerrar BD

**isClose**
Detectar si la llave ha sido insertada

**keys**
Numeros de llaves permitidas a insertar

**get\_inserts**
Numeros de llaves insertadas
