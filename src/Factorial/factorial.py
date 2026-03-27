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

def procesar_rango_flexible(rango_str):
    try:
        partes = rango_str.split('-')
        
        # -hasta (ejemplo: -10) 
        if partes[0] == "" and partes[1] != "":
            desde = 1
            hasta = int(partes[1])
        
        # desde- (ejemplo: 55-) 
        elif partes[0] != "" and partes[1] == "":
            desde = int(partes[0])
            hasta = 60
            
        # "desde-hasta" (ejemplo: 4-8) 
        elif partes[0] != "" and partes[1] != "":
            desde = int(partes[0])
            hasta = int(partes[1])
        
        else:
            print("Formato no reconocido.")
            return

        # Validación desde hasta
        if desde > hasta:
            print(f"Error: El inicio ({desde}) no puede ser mayor al fin ({hasta}).")
            return

        print(f"\nProcesando rango: {desde} a {hasta}")
        for i in range(desde, hasta + 1):
            print(f"  {i}! = {factorial(i)}")
            
    except (ValueError, IndexError):
        print("Error: Use el formato 'n-m', '-m' o 'n-'.")

# Entrada de datos
if len(sys.argv) > 1:
    rango_input = sys.argv[1]
else:
    print("No se detectó argumento de rango.")
    rango_input = input("Ingrese el rango (ej. -10 o 55-): ")

procesar_rango_flexible(rango_input)