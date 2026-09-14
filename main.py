from teste_api import buscar_clima, buscar_localizacao

mensagem = input("Você: ")

print("Mensagem recebida: ", mensagem)

def interpretar_mensagem(mensagem):
    if mensagem.lower().startswith("clima em"):
        # print("A mensagem começa com 'clima em' ")
        resultado = mensagem[8:].strip()   
        return resultado
    else:
        print("A mensagem não começa com 'clima em' ")
        return None

cidade = interpretar_mensagem(mensagem)
print("Cidade identificada: ", cidade) 

if cidade is not None:
    localizacao = buscar_localizacao(cidade)
    if localizacao is not None:
        latitude = localizacao["latitude"]
        longitude = localizacao["longitude"]
        clima = buscar_clima(latitude, longitude)
else:
    print("Mensagem não reconhecida!")
    
def interpretar_weather_code(codigo):
    if codigo == 0:
        return "céu limpo"
    elif 1 <= codigo <= 3:
        return "diferentes condições de céu nublado"
    elif 45 <= codigo <= 48:
        return "neblina"
    elif 51 <= codigo <= 57:
        return "garoa"
    elif 61 <= codigo <= 67:
        return "chuva"
    elif 71 <= codigo <= 77:
        return "neve"
    elif 80 <= codigo <= 82:
        return "pancadas de chuva"
    elif 95 <= codigo <= 99:
        return "tempestade"
    else:
        return "código desconhecido"

def resposta_usuario(cidade, clima):
        
    temperatura = clima["temperature_2m"]
    velocidade_vento = clima["wind_speed_10m"]
    codigo = clima["weather_code"]
    
    condicao_climatica = interpretar_weather_code(codigo)
    
    return f'O clima em {cidade} está com {str(temperatura).replace(".",",")}°C. \nCondição: {condicao_climatica}.\nVento: {str(velocidade_vento).replace(".",",")} km/h'

print(resposta_usuario(cidade, clima))
