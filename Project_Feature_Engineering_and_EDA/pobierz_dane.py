import requests
from datetime import datetime
import os

url = "https://api.dane.gov.pl/resources/43587,aktualne-dane-pomiarowe-w-postaci-pliku-csv/file"
folder = "C:/Users/sakla/OneDrive/Pulpit/Documents/dane_ML"
os.makedirs(folder, exist_ok=True)

filename = datetime.now().strftime("%Y-%m-%d_%H-%M") + ".csv"
filepath = os.path.join(folder, filename)

response = requests.get(url)
if response.status_code == 200:
    with open(filepath, "wb") as f:
        f.write(response.content)
    print(f"[OK] Zapisano dane do: {filepath}")
else:
    print(f"[BŁĄD] Nie udało się pobrać danych. Kod odpowiedzi: {response.status_code}")
