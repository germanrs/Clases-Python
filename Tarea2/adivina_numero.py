#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Entrar el limite: 100
# Los números cuadrados son:
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# random
import random

numero_aleatorio = random.randint(1,10)
intentos = 0

entrada_numero = None

while entrada_numero != numero_aleatorio:
    entrada_numero = int(raw_input('Adivina el numero! '))
    intentos = intentos + 1
    if entrada_numero > numero_aleatorio:
        print 'Muy alto'
    else:
        print 'Muy bajo'
print 'Adivinaste el numero en %d intentos' % (intentos)
