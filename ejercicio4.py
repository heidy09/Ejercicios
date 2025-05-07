# Ejercicio 6. Definir la función
# maxTres : (int, int, int) -> int
# tal que maxTres(x, y, z) es el máximo de x, y y z



def variables(x, y, z):
    if not type(x) == int:
        print("el argumentos no es enteros.")
        return
    
    if not type(y) == int:
        print("el argumentos no es enteros.")
        return 
    
    if not type(z) == int:
        print("el argumentos no es enteros.")
        return 
    
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z
    
    
print("el máximo de x,y,z es:")
print(variables('a', 360, 150))             



