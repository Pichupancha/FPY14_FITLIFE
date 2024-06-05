import os
import msvcrt
import csv

Cliente = []
while True:
    print("Presione para continuar")
    msvcrt.getch()
    os.system("cls")
    print("""
    Sistema de gestión de reservas FitLife
    ----------------------------------------
    1) Registrar un nuevo usuario.
    2) Reservar una clase y generar reporte CSV.
    3) Consultar clase disponible.        
    4) Consultar reservas de un usuario.
    0) Salir del programa.""")
    opcion = int(input("Seleccione : "))
    if opcion==0:
        break
    elif opcion==1:
        print("\033[35mRegistrar un nuevo usuario\033[0m")
        
    elif opcion==2:
        print("\033[35mReservar una clase y generar reporte CSV\033[0m")
    elif opcion==3:
        print("\033[35mConsultar clase disponible\033[0m")
    elif opcion==4:
        print("\033[35mConsultar reservas de un usuario\033[0m")
    else: 
        print("\033[31mOpcion no valida\033[0m")