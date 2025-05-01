import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

URL = "http://10.20.12.191:5000/get_subscriber_info"
PARAMS = {"msisdn": "51987654302"}
TPS = 124
DURATION_SECONDS = 5  # Cuántos segundos simular
TOTAL_REQUESTS = TPS * DURATION_SECONDS

def make_request(i):
    try:
        response = requests.get(URL, params=PARAMS, timeout=5)
        return f"[{i}] Status: {response.status_code}"
    except requests.RequestException as e:
        return f"[{i}] Error: {e}"

start_time = time.time()
with ThreadPoolExecutor(max_workers=TPS * 2) as executor:
    futures = [executor.submit(make_request, i) for i in range(TOTAL_REQUESTS)]

    for future in as_completed(futures):
        print(future.result())

elapsed = time.time() - start_time
print(f"Tiempo total: {elapsed:.2f} segundos")
