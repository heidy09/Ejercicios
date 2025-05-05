# Ejercicio 1. Definir la función
# media3 : (float, float, float) -> float

def media3(a: float, b: float, c: float)->float:
    return (a + b + c) / 3
 
resultado = media3(4.5, 4.0, 5.5)
print(resultado)  

#ejercicio 2

def media3(a, b, c):
    return (a + b + c) / 3

print(media3(1, 3, 8))    
print(media3(-1, 0, 7))  
print(media3(-3, 0, 3))
