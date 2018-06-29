#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Daniil
#
# Created:     17.03.2018
# Copyright:   (c) Daniil 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import globals

def check():
    if globals.location == globals.tavern:
        return globals.location.name
