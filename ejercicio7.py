entrada = "hello world and practice makes perfect and hello world again"
palabras = entrada.split(" ")
print(palabras)
contador = 0
palabrasIndiceUno = []
palabrasMayorAuno = []
for palabra in palabras:
    print(f"***{palabra}***")
    for validador in palabras :
        if palabra == validador:
            contador +=1
            print(f"    {palabra}---->{contador}")
    if contador == 1: 
        palabrasIndiceUno.append(palabra)
    if contador > 1 and not palabra in palabrasMayorAuno :
        palabrasMayorAuno.append(palabra)
    contador = 0
TextoSinDuplicados = palabrasIndiceUno + palabrasMayorAuno
textorelleno = " ".join(TextoSinDuplicados)
print(palabras)
print(palabrasIndiceUno)
print(palabrasMayorAuno)
print(TextoSinDuplicados)
print(textorelleno)


