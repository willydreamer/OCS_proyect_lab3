import requests
import time

url = "http://10.20.12.191:5000/get_subscriber_info"
params = {"msisdn": "51987654302"}

for i in range(500):
    try:
        response = requests.get(url, params=params, timeout=5)
        print(f"Intento {i + 1}: Estado {response.status_code}")
        if response.status_code == 200:
            print(response.json())  # O response.text si no es JSON
        else:
            print("Error al obtener respuesta")
    except requests.RequestException as e:
        print(f"Intento {i + 1}: Error de conexión - {e}")

    time.sleep(0.1)  # Pequeña pausa para no saturar el servidor (opcional)
