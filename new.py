
lista_objetivos=["deficit","superavit","mantenimiento"]
def ingresarDatos():
    lista_usuario = {}
    while True:
        try:
            peso=float(input("Su peso es: "))
            break
        except ValueError:
            print("El valor ingresado no es un numero")
    while True:
        try:
            altura=float(input("Su altura es: "))
            break
        except ValueError:
            print("El valor ingresado no es un numero")
    lista_usuario["Peso"]=peso
    lista_usuario["Altura"]=altura
    while True:
        objetivo = input("Su objetivo es (deficit/superavit/mantenimiento): ").lower()
        if objetivo in lista_objetivos:
            lista_usuario["Objetivo"]=objetivo
            if(objetivo=="deficit"):
                proteina_deficit=0.3*peso
                carbohydrates_deficiit=1.5*peso
                lista_usuario["Proteina"]=proteina_deficit
                lista_usuario["Carbohydrates"]=carbohydrates_deficiit
            elif(objetivo=="superavit"):
                proteina_superavit=peso*0.75
                carbohydrates_superavit=1.5*peso
                lista_usuario["Proteina"] = proteina_superavit
                lista_usuario["Carbohydrates"] = carbohydrates_superavit
            else:
                proteina_mantenimiento=peso*0.97
                carbohydrates_mantenimiento=1.2*peso
                lista_usuario["Proteina"] = proteina_mantenimiento
                lista_usuario["Carbohydrates"] = carbohydrates_mantenimiento
            return lista_usuario
        else:
            print("Opción incorrecta. Por favor, escriba una de las 3 opciones.")
datos_finales=ingresarDatos()
print("La lista de Usuario es:",datos_finales)