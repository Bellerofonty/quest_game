#-------------------------------------------------------------------------------
# Name:        go_to_tavern
# Purpose:     Квест: пойти в таверну
#
# Author:      Daniil
#
# Created:     18.03.2018
# Copyright:   (c) Daniil 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():
    import globals as gl

    if gl.location == gl.tavern:
        print('Вот и таверна')
