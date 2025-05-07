# Ejercicio 7. Definir la función
# rota1 : (List[A]) -> List[A]
# tal que rota1(xs) es la lista obtenida poniendo el primer elemento de
# xs al final de la lista

def list1(element):
    if type(element) == list:
        print("crea una lista.")
        return


def list1(element):
    first = element[0]
    element = element[1:]
    element.append(first)#primer
    return element

print(list1([1, 2, 3, 4, 5]))  
print(list1(['a', 'b', 'c','d','e'])) 
