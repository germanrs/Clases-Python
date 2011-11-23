# test
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# $ python buscar_uuid.py SHC92502EBF
# El UUID de la laptop SHC92502EBF es CAF15C1B-5CEF-476A-B467-841B9888AC1C

import sys
#try:
#	entrada = sys.argv[1]
#except IndexError:
#	print "No se ingreso nada"
#	sys.exit(1)
if len(sys.argv) != 2:
    print "eeror"
    sys.exit(1)
    
entrada=sys.argv[1]
if len(entrada) != 11:
    print "Error...\n Debes ingregar bien el SERIAL DE LA XO..."
    sys.exit(1)

bd = open("uuid.txt", "r")
for linea in bd:
    linea = linea.strip()
    if entrada == linea[0:11]:
        print "El UUID de la laptop %s: es %s" % (entrada,linea[12:])
        break
else:
    print "No se encontro"
bd.close()
