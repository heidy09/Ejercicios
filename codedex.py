calificacion= float(input("digita la calificacion:  "))

if calificacion >= 4.5:
    print("Extraordinario")
elif calificacion >= 4.0:
    print("Excelente")
elif calificacion >= 3.0:
    print("Bueno")
elif calificacion >= 2.0:
    print("Regular")
else:
    print("Malo")