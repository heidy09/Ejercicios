import random 
#Ruleta

#para generar numeros aleatorios 

def girar_ruleta( ):
    numero_ganador = random.randint(0,10)
    return numero_ganador

resultado = girar_ruleta( )

print(f"el numero ganador es: {resultado}")

