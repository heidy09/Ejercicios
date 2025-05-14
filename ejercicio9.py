#Definir, por recursión, la función potencia : (int, int) -> int tal que potencia(x, n) es x elevado al número natural n. Por ejemplo, potencia(2, 3) == 8
def power(Ximena, natural):
    if natural == 0:
        return 1
    else:
        print(Ximena, natural - 1)
        result =  Ximena * power(Ximena, natural - 1)
        print(f"    {result}")
        return result

def start():
    try:
        firstNatural = input("Enter the first number (natural): ")
        secondNatural = input("Enter the second number (natural): ")
        # Intentar convertir a enteros
        firstNatural = int(firstNatural)
        secondNatural = int(secondNatural)
        # Verificar si son naturales
        if firstNatural < 0 or secondNatural < 0:
            print("Error: Numbers must be natural (a 0).")
            return
        print(f"The number entered is: {firstNatural}")
        print(f"The second number entered is: {secondNatural}")
        result = power(firstNatural, secondNatural)
        print(f"{firstNatural} elevado a {secondNatural} es: {result}")
        print("The operation was successful.")
    except ValueError:
        print("one of the values joined not is a number whole valid.")
print(start())


