# -*- coding: utf-8 -*-
import sys
# calculadora(Suma, op1, op2)


#Funcion = sys.argv[1]
#Op1 = float(sys.argv[2])
#Op2 = float(sys.argv[3])

if len(sys.argv) != 4:
    sys.exit ("introducir 3 argumentos")

_, Funcion, Op1, Op2 = sys.argv

try:
    Op1 = float(Op1)
    Op2 = float(Op2)
except:
    sys.exit ("Necesito numeros")
    
    
#funciones = ["suma", "resta", ]

#if operador in funciones:

#else sys.exit("Operadores: suma, resta, divide, multiplica")



if Funcion == "suma":
    print str(Op1), "+", str(Op2), "=", (Op1+Op2)
if Funcion == "resta":
    print str(Op1), "-", str(Op2), "=", (Op1-Op2)
if Funcion == "divide":
    try:
        print str(Op1), "/", str(Op2), "=", (Op1/Op2)
    except ZeroDivisionError:
        print "Division por cero"
if Funcion == "multiplica":
    print str(Op1), "*", str(Op2), "=", (Op1*Op2)
