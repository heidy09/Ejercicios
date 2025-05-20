#Question: Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied to the program: 
# hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3 Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

prayer = input("Write a sentence: ")

if not prayer:
    print("The entry cannot be empty, Error.")
else:
    letters = 0
    digits = 0
    spaces = 0
    corrected = prayer
    notValid = [] # Cambiado a lista, lo cual hace que otros caracteres no sean validos
    #alphabet = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    invalidCharacterCount = 0

    for character in prayer:
        if character.isalpha():
            letters += 1
        elif character.isdigit():
            digits += 1
        elif character.isspace():
            spaces += 1
        else:
            invalidCharacterCount += 1
            if character not in notValid:
                notValid.append(character)
                corrected = corrected.replace(character,'')
    print("Corrected sentence:", corrected)
    print("LETTERS:", letters)
    print("DIGITS:", digits)
    print("SPACES:", spaces)
    if notValid:
        print("Invalid characters:", ''.join(notValid))
        print("total invalid characters: ", invalidCharacterCount )
    else:
        print("No invalid characters were found. It ran without errors.")
    
    print("Sentence entered:", prayer)


