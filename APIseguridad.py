from shodan import Shodan

def apifuncion():

    api = Shodan('bCrBWBdYmIrth9lEkCfNiLTZcRyg33bC')

    ipinfo = api.host('8.8.8.8')
    print("\n\n\n A continuación se ingresa a la API de Shodan \n\n\n")
    #Recorrer e imprimir el diccionario que se creó con los datos
    for ip in ipinfo:
        print(ip, ":", ipinfo[ip])
    print("\n\n\n")