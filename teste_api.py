import requests

url = "https://geocoding-api.open-meteo.com/v1/search?name=Campinas&count=1&language=pt&format=json"

resposta = requests.get(url)
dados = resposta.json()

print(resposta.status_code)
print(dados)