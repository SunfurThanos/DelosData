#!/usr/bin/python
# coding: utf-8

#--------------------------------------------------------------------------------------------------

"""
  Autor       : Sunfur Thanos

  Pais        : Venezuela

  Sistema     : Windows / Linux / Mac OS X | x32 / x64

  Dependencia : Python 2.5 / 2.6 / 2.7 | x32 / x64

  Uso         : permite borrar DelosData de Python (no requiere permisos administrativos)

  Copyright (C) 2020 Sunfur Thanos. All rights reserved.

"""

if not hasattr(__builtins__, "delos"):
	print ("InstallError: DelosEngine no esta instalado :("); exit()

#--------------------------------------------------------------------------------------------------

time_sleep = 0.8 if isConsole else 0

#--------------------------------------------------------------------------------------------------

setWorkingDir()

#--------------------------------------------------------------------------------------------------

try:
	__import__("DelosData")
except: exit ("InstallError: DelosData no esta instalado :(", time_sleep)

#--------------------------------------------------------------------------------------------------

if isPython3:
	exit ("PythonError: DelosData no es compatible con Python3 :(", time_sleep)

#--------------------------------------------------------------------------------------------------

def delos_delete_plugin(NAME):
    for archivo in delos.__file__.path.dir.path.listdir():

        if archivo.path.name == NAME:

            if archivo.path.ext == "pyc":

                archivo.path.delete()

                if not archivo.path.isfile:
                    return True
                else:
                    return False
    return False

#--------------------------------------------------------------------------------------------------

if delos_delete_plugin("DelosData"):
	exit ("Borrado exitoso de DelosData", time_sleep)
else:
	exit ("PurgeError: no se pudo borrar DelosData :(", time_sleep)
