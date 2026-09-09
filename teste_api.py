import requests

url = "https://geocoding-api.open-meteo.com/v1/search"
params = {
    "name": "Campinas",
    "count": 1,
    "language": "pt",
    "format": "json",
}
try:
    resposta = requests.get(url, params=params, timeout=10)
    resposta.raise_for_status()
    
    print(resposta.status_code)
    
    dados = resposta.json()
    
    print(dados["results"][0]["name"])
    print(dados["results"][0]["latitude"])
    print(dados["results"][0]["longitude"])
    
except (requests.exceptions.Timeout, requests.exceptions.HTTPError):
    print("A requisição excedeu o tempo limite")


