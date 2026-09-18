
lista_objetivos=["deficit","superavit","mantenimiento"]
lista_usuario=[]

def ingresarDatos():
    peso=float(input("Su peso es: "))
    altura=float(input("Su altura es: "))

    while True:
        objetivo = str(input("Su obejtivo es (Definicion/Superavit/mantenimiento):    "))
        if objetivo in lista_objetivos:
            break
        else:
            objetivo = str(input("Su objetivo es (Definicion/Superavit/mantenimiento):    "))

    lista_usuario.append(peso)
    lista_usuario.append(altura)
    lista_usuario.append(objetivo)

ingresarDatos()
print("La lista de Usuario es:",lista_usuario)
print("Ahora si brother ")