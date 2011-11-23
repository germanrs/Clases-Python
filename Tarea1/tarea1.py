#!/usr/bin/python
# -*- coding: utf-8 -*-
# Como te llamas? Daniel
# Hola Daniel, cuantos anhos tienes? 25
# En tu proximo cumpleaños tendrás 26 años
nombre = raw_input('¿Cual es tu nombre?: ')
try:
    edad = int(raw_input('Hola, %s, cuantos años tienes: ' % (nombre)))
    print 'En tu proximo cumpleaños tendras: %d años ' % (edad+1)
except ValueError:
    print 'Ese no es una edad, adios...'
print 'german'
#asdasdusahduhd
