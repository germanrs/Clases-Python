#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# $ python buscar_uuid.py SHC92502EBF
# El UUID de la laptop SHC92502EBF es CAF15C1B-5CEF-476A-B467-841B9888AC1C

import sys
import csv

if len(sys.argv) != 2:
    print "Error"
    sys.exit(1)
    
entrada=sys.argv[1]
if len(entrada) != 11:
    print "Deben ingresar bien el serial..."
    sys.exit(1)

archivo = open('uuid.csv', 'rb')
archivo_csv = csv.reader(archivo)

for columna in archivo_csv:
    if entrada == columna[0]:
        print "El UUID de la laptop %s es %s " % (entrada,columna[1])
