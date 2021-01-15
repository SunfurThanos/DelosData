#!/usr/bin/python
# coding: utf-8

#--------------------------------------------------------------------------------------------------

"""
	Autor       : Andrade Echarry -> ALF

	Pais        : Venezuela

	Sistema     : Windows / Linux / Mac OS X | x32 / x64

	Dependencia : Python 2.5 / 2.6 / 2.7 | x32 / x64

	Uso         : permite instalar DelosData en Python (no requiere permisos administrativos)

	Copyright (C) 2020 Andrade Echarry -> ALF. All rights reserved.

"""

if not hasattr(__builtins__, "delos"):
	print ("InstallError: DelosEngine no esta instalado :("); exit()

#--------------------------------------------------------------------------------------------------

setWorkingDir()

#--------------------------------------------------------------------------------------------------

time_sleep = 0.8 if isConsole else 0

#--------------------------------------------------------------------------------------------------

try:
	__import__("DelosData")
	exit ("InstallError: Ya existe una version anterior de DelosData :)", time_sleep)
except: pass

#--------------------------------------------------------------------------------------------------

if isPython3:
	exit ("PythonError: DelosData no es compatible con Python3 :(", time_sleep)


#--------------------------------------------------------------------------------------------------

plugin_archivo = "APP-DelosData.py"

#--------------------------------------------------------------------------------------------------

PROGRAM_DIR = "source-code"
MAIN        = ""
OTHERS      = ""
for archivo in PROGRAM_DIR.path.listdir():
    if archivo.path.ext == "py":
        if archivo.path.name == "__init__":
           MAIN = archivo.path.read()
        else:
            OTHERS+=archivo.path.read()

#--------------------------------------------------------------------------------------------------

import re
RESULT = MAIN
recompilar = re.compile(r'(from .*? import \*)')
che_infeliz = recompilar.findall(RESULT)
RESULT = RESULT.Replace(che_infeliz, OTHERS, maxi=1)
RESULT = RESULT.Replace(che_infeliz)
plugin_archivo.path.save(RESULT).close()

#--------------------------------------------------------------------------------------------------

py_compile = __import__("py_compile")
fileX = plugin_archivo
path_relative = fileX.path.relative
py_compile.compile(file=path_relative)
plugin_archivo.path.delete()

#--------------------------------------------------------------------------------------------------

directorio_python_plugins = delos.__file__.path.dir
directorio_copy = directorio_python_plugins.path.join("DelosData.pyc")
plugin_archivo = plugin_archivo.path.change_ext("pyc")

#--------------------------------------------------------------------------------------------------

if plugin_archivo.path.move(directorio_copy):

	try:
		delos.sys.path.append(directorio_python_plugins)
		import DelosData
		peso = directorio_copy.path.size.info.join(" ")
	except:
		exit ("InstallError: no se pudo instalar", time_sleep)

	mensaje = "** instalacion exitosa\n"
	mensaje+= "Directorio: '{directorio_python_plugins}'\n"
	mensaje+= "Peso: {peso}\n"
	mensaje+= "Version: {__build__}"

	Sleep (mensaje.toF, time_sleep)

else:

	Sleep ("InstallError: no se pudo instalar", time_sleep)
