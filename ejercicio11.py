# Se tiene una mochila de capacidad de peso  y una lista de  objetos
# para colocar en la mochila. Cada objeto  tiene un peso  y un
# valor en pesos. Considerando la posibilidad de colocar el mismo objeto
# varias veces en la mochila, el problema consiste en determinar la
# forma de colocar los objetos en la mochila sin sobrepasar la
# capacidad de la mochila colocando el máximo valor posible.


def mochila(objetos, capacidad):
    # Ordenamos objetos por valor descendente
    objetos.sort(key=lambda expresion: expresion['valor'], reverse=True)
    mayorValor = 0
    nombreDeObjetos = []
    for objetosOrdenados in objetos:
        if objetosOrdenados['peso'] <= capacidad:
            capacidad -= objetosOrdenados['peso']
            mayorValor += objetosOrdenados['valor']
            nombreDeObjetos.append(objetosOrdenados['nombre'])
        else:
            print(f"\n{objetosOrdenados['nombre']} no cabe en la mochila, no se puede llevar.")
    return mayorValor, nombreDeObjetos
iniciaElProceso = int(input("¿Cuántos objetos deseas ingresar?: "))# Preguntar cuántos objetos ingresará el usuario
objetos = []
objetosDuplicados = {}
for enumerar in range(iniciaElProceso):
    nombre = input(f"Nombre del objeto #{enumerar+1}: ")
    peso = int(input(f"Peso de {nombre}: "))
    valor = int(input(f"Valor de {nombre}: "))
    clave = (nombre.lower(), peso, valor)
    if clave in objetosDuplicados:
        objetosDuplicados[clave] += 1
        print(f"\n¡Has ingresado el objeto! '{nombre}' más de una vez con el mismo peso y valor.")
        print(f"Este objeto ha sido ingresado {objetosDuplicados[clave]} veces.")
    else:
        objetosDuplicados[clave] = 1
        if nombre.lower() in objetosDuplicados:
                print(f"\nHas ingresado el mismo objeto '{nombre}' con un valor o peso diferente. Se permitirá.")
        else:
            objetosDuplicados[nombre.lower()] = 1
    objetos.append({'nombre': nombre, 'peso': peso, 'valor': valor})
capacidad = int(input("Capacidad de la mochila: "))
valor, nombreDeObjetos = mochila(objetos, capacidad)
print("\nObjetos seleccionados:")
for nombre in nombreDeObjetos:
    print("-", nombre)
print(f"Valor total en la mochila: {valor}")      
