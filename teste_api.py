import requests

def buscar_localizacao(cidade):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": cidade,
        "count": 1,
        "language": "pt",
        "format": "json",
    }
    try:
        resposta = requests.get(url, params=params, timeout=10)
        resposta.raise_for_status()
               
        dados = resposta.json()

        if "results" in dados and dados["results"]:  
            localizacao = {
                "name": dados["results"][0]["name"],
                "latitude": dados["results"][0]["latitude"],
                "longitude": dados["results"][0]["longitude"]
            }
            return localizacao
        else:
            return None
        
    except requests.exceptions.Timeout:
        print("A requisição excedeu o tempo limite")
    except requests.exceptions.HTTPError:
        print("A API retornou um erro HTTP.")

def buscar_clima(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,weather_code"
    }

    try:
        resposta = requests.get(url, params=params, timeout=10)
        resposta.raise_for_status()

        dados = resposta.json()
        print(dados)
        
        if "current" in dados and dados["current"]:
            clima = {
                "temperature_2m": dados["current"]["temperature_2m"],
                "wind_speed_10m": dados["current"]["wind_speed_10m"],
                "weather_code": dados["current"]["weather_code"]
            }
            
            return clima
        else:
            return None
    
    except requests.exceptions.Timeout:
        print("A requisição excedeu o tempo limite")
    except requests.exceptions.HTTPError:
        print("A API retornou um erro HTTP.")         


resultado_localizacao = buscar_localizacao("Campinas")
print(resultado_localizacao)

if resultado_localizacao is not None:
    latitude = resultado_localizacao["latitude"]
    longitude = resultado_localizacao["longitude"]
    resultado_clima = buscar_clima(latitude, longitude)
    print(resultado_clima)
else:
    print("Coordenadas não encontradas!")



