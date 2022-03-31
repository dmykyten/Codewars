def alphabet_position(text):
    result = []
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                result.append(str(ord(letter) - 64))
            else:
                result.append(str(ord(letter) - 96))
    return ' '.join(result)

#Finished