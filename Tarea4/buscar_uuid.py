# test
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# $ python buscar_uuid.py SHC92502EBF
# El UUID de la laptop SHC92502EBF es CAF15C1B-5CEF-476A-B467-841B9888AC1C

import sys

#entrada = sys.argv[1]

if len(sys.argv) == 2:
        print sys.argv[1]
else:
        print "debe ingresar algo..."


bd = open("/home/german/Escritorio/pyton/uuid.txt", "r")

for linea in bd:
# while linea:
    linea = linea.strip()
#    print linea
    if entrada == linea[0:11]:
        print "El UUID de la laptop %s: es %s" % (entrada,linea[12:47])
        break
else:
    print "No se encontro"

bd.close()

