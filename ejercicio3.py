#tresIguales : (int, int, int) -> bool
# tal que tresIguales(x, y, z) se verifica si los elementos x, y y z son
# iguales. Por ejemplo,
# tresIguales(4, 4, 4) == True
# tresIguales(4, 3, 4) == False

def threeEqualVariables(x:int, y:int, z:int):
    if not type (x) == int:
        print("el argumentos no es enteros.")
        return 
    if not type (y) == int:
        print("el argumentos no es enteros.")
        return 
    if not type (z) == int:
        print("el argumentos no es enteros.")
        return 
    
    return x == y == z 

print(threeEqualVariables(4, 4, 4))  
print(threeEqualVariables(4, 3, 4))  
