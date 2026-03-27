#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

import sys

def factorial(num): 
    if num < 0: return 0
    elif num == 0: return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

def procesar_rango(rango_str):
    try:
        # Separamos los números usando el guion '-' como divisor
        partes = rango_str.split('-')
        desde = int(partes[0])
        hasta = int(partes[1])
        
        # Validamos que el rango sea lógico 
        if desde > hasta:
            desde, hasta = hasta, desde 
            
        print(f"\nCalculando factoriales desde {desde} hasta {hasta}:")
        for i in range(desde, hasta + 1):
            print(f"  {i}! = {factorial(i)}")
            
    except (ValueError, IndexError):
        print("Error: El formato debe ser NÚMERO-NÚMERO (ejemplo: 4-8)")


# .Intento por argumento de terminal
if len(sys.argv) > 1:
    rango_input = sys.argv[1]
else:
    # .Si se omite, se solicita manualmente
    print("No se detectó un rango como argumento.")
    rango_input = input("Ingrese el rango (ej. 4-8): ")

procesar_rango(rango_input)
