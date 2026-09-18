
lista_objetivos=["deficit","superavit","mantenimiento"]
lista_usuario=[]

def ingresarDatos():
    peso=float(input("Su peso es: "))
    altura=float(input("Su altura es: "))
    objetivo=str(input("Su obejtivo es (Definicion/Superavit/mantenimiento):    ")

    for i in lista_objetivos:
        if i==lista_objetivos[0]:
            objetivo=str(lista_objetivos[0])
        elif  i==lista_objetivos[1]:
            objetivo=str(lista_objetivos[1])
        elif i==lista_objetivos[2]:
            objetivo=str(lista_objetivos[2])
        else:
            objetivo = str(input("No se cargó,su obejtivo es (Definicion/Superavit/mantenimiento):    ")

    lista_usuario.append(peso,altura,objetivo)

ingresarDatos()

