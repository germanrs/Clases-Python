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
# branch devel

limite = int(raw_input('Ingrese el limite: '))
inicio = 1
resultado = inicio * inicio
print 'Los números cuadrados son: '

while resultado <= limite:
    print resultado
    inicio = inicio + 1
    resultado = inicio * inicio

