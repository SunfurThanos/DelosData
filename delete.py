#!/usr/bin/python
# coding: utf-8

#--------------------------------------------------------------------------------------------------

"""
  Author     : Sunfur Thanos

  Country    : Venezuela

  System     : Windows / Linux / Mac OS X | x32 / x64

  Dependency : Python 2.5 / 2.6 / 2.7 | x32 / x64

  Usage      : Delete DelosData from Python (does not require administrative permissions)

  Copyright (C) 2020 Sunfur Thanos. All rights reserved.

"""

if not hasattr(__builtins__, "delos"):
	print ("InstallError: DelosEngine is not installed :("); exit()

#--------------------------------------------------------------------------------------------------

time_sleep = 0.8 if isConsole else 0

#--------------------------------------------------------------------------------------------------

setWorkingDir()

#--------------------------------------------------------------------------------------------------

try:
	__import__("DelosData")
except: exit ("InstallError: DelosData is not installed :(", time_sleep)

#--------------------------------------------------------------------------------------------------

if isPython3:
	exit ("PythonError: DelosData is not compatible with Python3 :(", time_sleep)

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
	exit ("DelosData successful deletion", time_sleep)
else:
	exit ("PurgeError: DelosData could not be deleted :(", time_sleep)
