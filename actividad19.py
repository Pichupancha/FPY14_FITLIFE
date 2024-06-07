import os
import msvcrt
import csv

#FUNCION PARA CREAR TITULOS
def titulo(texto : str):
    print(f"\033[33m{texto.upper()}\033[0m")

def error(texto : str):
    print(f"\033[31m{texto.upper()}\033[0m")

def exito(texto : str):
    print(f"\033[32m{texto.upper()}\033[0m")

#Tuplas - Clases
clases = [
    ("PESAS","LUN-MIE 08:30 a.m",10),
    ("ZUMBA","MAR-JUE 3:30-5:40 p.m",20),
    ("NUTRICION","VIERNES 6:00-7:30 a.m",2),
    ("CROSSFIT","SAB 11:30-12:55 p.m",10)
]
#diccionario para usuarios
usuarios = {}
#lista -reservas
reservas = []
#Contador para el id del usuario
numero_usuario = 100
#comenzamos el sistema
while True:
    print("Presiona para continuar")
    msvcrt.getch()
    os.system("cls")

    print("""\033[32m
    Sistema de gestion FitLife
    ════════════════════════════════\033[0m
    1) Registrar usuario.
    2) Reservar clase.
    3) Consultar clases disponibles.
    4) Consultar clases del usuario.
    5) Consultar usuarios.
    0) Salir.      
    \033[32m════════════════════════════════\033[0m""")
    opcion = input("Seleccione : ")
    if opcion == "0":
        titulo("Adios")
        break
    elif opcion == "1":
        titulo("Registar usuarios")
        nombre = input("Ingrese nombre de usuario : ").title()
        if nombre not in usuarios.values():
            usuarios[numero_usuario] = nombre
            numero_usuario+=100
            exito("Usuario registrado")
        else:
            error("Usuario ya registrado")
    elif opcion == "2":
        titulo("Reservar clase")
        codigo = int(input("Ingrese codigo de usuario : "))
        if codigo in usuarios:
            curso = input("Ingrese curso para inscribir : ").upper()
            cantinelacurso = False
            centinelacupos = False
            for c in clases:
                if c[0].upper() == curso:
                    centinelacurso = True
                    if c[2]>0:
                        centinelacupos = True
                        reservas.append([codigo,usuarios[codigo],c[0],c[1]])
                        exito("Reserva realizada")
                        #Descontar cupo
                        actualizacioncupo = (c[0],c[1],c[2]-1)
                        clases.remove(c)
                        clases.append(actualizacioncupo)
                        break
            if centinelacurso==False:
                error("No existe el curso")
            if centinelacupos==False:
                error("No existe el curso")
    elif opcion == "3":
        titulo("Consultar clase disponible")
    elif opcion == "4":
        titulo("Consultar clases del usuario")
    elif opcion == "5":
        titulo("Consultar usuario")
        if len(usuarios)>0:
            for u in usuarios:
                print(f"{u} : {usuarios[u]}")
    else:
        error("Opcion no valida")


    