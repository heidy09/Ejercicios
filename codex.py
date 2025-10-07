
number = int(input("Enter an integer: "))
total = 0


for i in range(1, number + 1):
    square = i * i
    total += square 

print(total)