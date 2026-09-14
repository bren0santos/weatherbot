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

resultado = buscar_localizacao("Campinas")
print(resultado)

