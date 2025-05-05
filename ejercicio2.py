#Escriba un programa que encuentre todos los números que son divisibles por 7 pero que no son múltiplos de 5, 
# entre 2000 y 3200 (ambos incluidos). Los números obtenidos deben imprimirse en una secuencia separada por comas en una sola línea.

lista = []
num = 2000

while num <= 3200:
  if num % 7 == 0 and num % 5 != 0:
    lista.append(str(num))
  num += 1

print(",".join(lista))

