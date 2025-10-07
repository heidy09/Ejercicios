mes = int(input("Ingresa el número del mes (1-12): "))

if mes == 1 or mes == 2 or mes == 3:
    print('Invierno ')
elif mes == 4 or mes == 5 or mes == 6:
    print('Primavera ')
elif mes == 7 or mes == 8 or mes == 9:
    print('Verano ')
elif mes == 10 or mes == 11 or mes == 12:
    print('Otoño ')
else:
    print('Inválido')