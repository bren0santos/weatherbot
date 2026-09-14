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
        print(clima)
else:
    print("Mensagem não reconhecida!")
    
