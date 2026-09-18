import requests
try:
    respuesta=requests.get(url="https://jsonplaceholder.typicode.com/users", timeout=10)
    if respuesta.status_code == 200:
        respuesta = respuesta.json()
        for i in respuesta:
            print("Nombre: ", i["name"])
            print("Email: ", i["email"])
            print("Nombre de la Compania: ", i["company"]["name"])
    else:
        print("La concexión con la API no fue ejecutada correctamente")
except requests.exceptions.RequestException:
    #EL RequestException se usa por si falla la conexion a internet, o DNS o directamente tardo mas del tiempo
    #que le pusiste al timeout el requesta la api
    print("Lo sentimos, el servidor tardó demasiado en responder")


