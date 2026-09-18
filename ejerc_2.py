import csv
try:
    with open("Estacion,Hora,Pasajeros,Capacidad.csv", mode="r", encoding="utf-8") as archivo:
        contenido=csv.DictReader(archivo)
        sumador=0
        contador=0
        for i in contenido:
            if int(i["Capacidad"])<int(i["Pasajeros"]):
                print("La estacion",i["Estacion"],"está llena")
            sumador=int(i["Pasajeros"])+sumador
            contador=contador+1
        if contador>0:
            promedio=sumador/contador
            print("El promedio es:", promedio)
        else:
            print("El Archivo esta vacío")
except FileNotFoundError:
    print("El archivo no existe")



