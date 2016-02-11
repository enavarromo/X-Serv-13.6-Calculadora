# -*- coding: utf-8 -*-
import sys
# calculadora(Suma, op1, op2)


Funcion = sys.argv[1]
Op1 = float(sys.argv[2])
Op2 = float(sys.argv[3])
if Funcion == "suma":
    print str(Op1), "+", str(Op2), "=", (Op1+Op2)
if Funcion == "resta":
    print str(Op1), "-", str(Op2), "=", (Op1-Op2)
if Funcion == "divide":
    print str(Op1), "/", str(Op2), "=", (Op1/Op2)
if Funcion == "multiplica":
    print str(Op1), "*", str(Op2), "=", (Op1*Op2)



#print "Arg0: ", sys.argv[0]
#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)


"""
AuxFile = open ("/etc/passwd","r")  # Archivo -> auxiliar
lineas = AuxFile.readlines()        # Auxiliar -> lista[linea, caracter]

shells = {}             # Init diccionario
for linea in lineas:    # Recorro cada linea leida del fichero
    shells[linea.split(":")[0]] = linea.split(":")[-1][:-1] # Cargo el shell de
                                                            # cada root en el
                                                            # diccionario.
print "Numero de shells: " + str(len(shells))   # Imprimo la cantidad de shells
try:                                        
    print "shell de root:", shells["root"]
    print "shell de imaginario:", shells["imaginario"]
#    print "usuario" + blabla... + es distinto de 
#    print "usuario", blabla...,
#    en cuanto a "instante de ejecucion"
except: # Permite especificar el fallo concreto a capturar de los disponibles
    print "Usuario no encontrado en el diccionario."

AuxFile.close
"""
