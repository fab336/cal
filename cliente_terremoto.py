import requests

def get_earthquake_data():
    # URL para solicitar eventos sísmicos de los últimos 30 días
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",  # Formato de respuesta
        "starttime": "2023-01-01",  # Fecha de inicio
        "endtime": "2023-12-31",    # Fecha de fin
        "minmagnitude": 6.0         # Magnitud mínima
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()  # Respuesta en formato JSON
        return data["features"]  # Lista de terremotos
    else:
        print("Error al obtener datos:", response.status_code)
        return []

# Ejecución del cliente
earthquakes = get_earthquake_data()
for earthquake in earthquakes[:5]:  # Mostrar los primeros 5 resultados
    properties = earthquake["properties"]
    print(f"Lugar: {properties['place']}")
    print(f"Magnitud: {properties['mag']}")
    print(f"Fecha y hora: {properties['time']}\n")
