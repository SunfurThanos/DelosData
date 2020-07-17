#!/usr/bin/python
# coding: utf-8

#--------------------------------------------------------------------------------------------------

"""
	Author     : Sunfur Thanos

	Country    : Venezuela

	System     : Windows / Linux / Mac OS X | x32 / x64

	Dependency : Python 2.5 / 2.6 / 2.7 | x32 / x64

	Use        : allows to install DelosData in Python (does not require administrative permissions)

	Copyright (C) 2020 Sunfur Thanos. All rights reserved.

"""

if not hasattr(__builtins__, "delos"):
	print ("InstallError: DelosEngine is not installed :("); exit()

#--------------------------------------------------------------------------------------------------

setWorkingDir()

#--------------------------------------------------------------------------------------------------

time_sleep = 0.8 if isConsole else 0

#--------------------------------------------------------------------------------------------------

try:
	__import__("DelosData")
	exit ("InstallError: A previous version of DelosData already exists :)", time_sleep)
except: pass

#--------------------------------------------------------------------------------------------------

if isPython3:
	exit ("PythonError: DelosData is not compatible with Python3 :(", time_sleep)


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
		exit ("InstallError: could not install", time_sleep)

	mensaje = "** Installation successful\n"
	mensaje+= "directory: '{directorio_python_plugins}'\n"
	mensaje+= "Size: {peso}\n"
	mensaje+= "Version: {__build__}"

	Sleep (mensaje.toF, time_sleep)

else:

	Sleep ("InstallError: could not install", time_sleep)
