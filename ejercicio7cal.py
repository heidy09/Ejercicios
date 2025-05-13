#Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. 
#Suppose the following input is supplied to the program: 8 Then, the output should be: 40320 Hints: In case of input data being supplied to the question,
#it should be assumed to be a console input.

start = input("type a number to calculate its factorial:")

if start.isdigit():
    number = int(start)

    factorialNumber = 1
    for operation in range(1, number + 1):
        print(factorialNumber, operation)
        factorialNumber *= operation # factorialNumber = factorialNumber * operation ////// factorialNumber = factorialNumber + operation
        print(f"---->{factorialNumber}")
    print(f"The factorial of {number} is: {factorialNumber}")
else:
    print("the entered argument is not an integer.")