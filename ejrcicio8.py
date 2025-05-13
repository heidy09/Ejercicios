#Question: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting 
# them alphanumerically.Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then, the output should be: 
# again and hello makes perfect practice world Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 
# We use set container to remove duplicated data automatically and then use sorted() to sort the data


#entrance = "hello world and practice makes perfect and hello world again"


entrance =input("ingrese una variable:  ")
if entrance.isdigit():
    print("the argument is not str")
else:
    print("the argument is not an int")
    words = entrance.split(" ")
    print(words)
    counter = 0
    wordsIndexOne = []
    wordsGreaterThanOne = []
    for word in words:
        print(f"***{word}***")
        for validator in words :
            if word == validator:
                counter +=1
                print(f"    {word}--->{counter}")
        if counter == 1:
                wordsIndexOne.append(word)
        if counter > 1 and not word in wordsGreaterThanOne :
            wordsGreaterThanOne.append(word)
        counter = 0

    textWithoutDuplicates = wordsIndexOne + wordsGreaterThanOne
    filltext = " ".join(textWithoutDuplicates)

    print(words)
    print(wordsIndexOne)
    print(wordsGreaterThanOne)
    print(textWithoutDuplicates)
    print(filltext)