
Crear BD
========

| Funcion | Retorno | Descripción |
| --- | --- | --- | --- |
| **create(keys=number)** | method | permite crear la BD, especificando cuantas llaves tendrá |
| **prediction\_size(size\_items=number)** | dict | permite hacer una predicción de cuanto pesara la BD antes de ser creada |
| **size\_db** | str_size_info | podrás mostrar el peso de la BD generada |
| **timeout = number** | None | variable que permite especificar, cuanto sera la frecuencia de actualizacion para la funcion de progreso |
| **export(file, func\_progress)** | bool | función para exportar la BB a un archivo `creación final de la BD`, puedes especificar el archivo de salida y la función de progreso, es decir puedes asignar una función y allí mostrar el progreso de generación, ideal para grandes BD |

---

Insertar llaves
===============

| Funcion | Retorno | Descripción |
| --- | --- | --- | --- |
| **open** | method | funcion para importar BD creada |
| **add** | [Inserts_returns](#inserts-returns) | permite insertar una llave + valor |
| **close()** | None | cierra BD |
| **isClose** | bool | detectar si la llave ha sido insertada |
| **keys** | number | numeros de llaves permitidas a insertar |
| **get\_inserts** | number | numeros de llaves insertadas |

## Inserts-returns

| Funcion | Descripción |
| --- | --- | --- | --- |
| **YES** | llave insertada correctamente |
| **EXIST** | la llave ya existe |
| **table-UP** | la tabla (index) esta llena |
| **item-size** | el item sobre-pasa la longitud permitida |
| **ERROR-CRICAL** | error critico de escritura |
| **file-close** | el archivo (BD) esta cerrada |

---

ver llaves insertadas
=====================

| Funcion | Retorno | Descripción |
| --- | --- | --- | --- |
| **get(key\_name, time=bool)** | string / False | funcion para extraer el valor de una llave, tambien es posible validar si la llave no existe |
| **close()** | None | cierra BD |
| **isClose** | bool | detectar si la llave ha sido insertada |
| **keys** | number | numeros de llaves permitidas a insertar |
| **get\_inserts** | number | numeros de llaves insertadas |
