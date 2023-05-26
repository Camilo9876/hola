import urllib.parse
import requests
# Función para calcular la distancia entre dos ciudades utilizando la APi de MapQuest
def calculo_de_distancia (inicio, destino):
        url = f'https://www.mapquestapi.com/directions/v2/route?key=6t4vS5B2jTKaJxTweFkvvcozXf7C65Jd&from={inicio}&to={destino}'
        response = requests.get(url)
        data = response.json()
        distancia = data['route']['distance']
        return distancia

# Función para calcular la duración del viaje en horas, minutas y segundos
def calculo_de_duracion (inicio, destino):
        url = f'https://www.mapquestapi.com/directions/v2/route?key=6t4vS5B2jTKaJxTweFkvvcozXf7C65Jd&from={inicio}&to={destino}'
        response = requests.get(url)
        data = response.json()
        duracion = data['route']['formattedTime']
        return duracion

# Función para calcular el combustible requerido para el viaje en litro 
def calculo_de_combustible (distancia):
        litros_por_km = 0.12 # Consumo promedio de combustible por kilometro
        combustible = distancia * litros_por_km
        return combustible

# Función para imprimir la narrativa del viaje
def narrativa (inicio, destino, distancia, duración, combustible):
        print (f"Viaje de {inicio} a {destino}:")
        print (f"Distancia: {distancia:.2f} km")
        print (f"Duracion: {duracion}")
        print (f"Combustible requerido: {combustible:.2f} litros")

# programa principal 
inicio = input("Ciudad de Origen: ")
destino = input("Ciudad de Destino: ")

distancia = calculo_de_distancia (inicio, destino)
duracion = calculo_de_duracion (inicio, destino)
combustible = calculo_de_combustible (distancia)

narrativa (inicio, destino, distancia, duracion, combustible)
print ("=================================================================================================")
print ("Su viaje desde la ciudad de " + str(inicio), "hasta la ciudad de " + str(destino))
print ("tiene una distancia de " + str(distancia), "kilómetros", "y su viaje tiene una duración de " + str(duracion), "Horas")
print ("y va a consumir " + str(combustible), "Litros de combustible")
print ("=================================================================================================")
