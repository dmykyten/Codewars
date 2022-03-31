#https://www.codewars.com/kata/546f922b54af40e1e90001da
def alphabet_position(text):
    result = []
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                result.append(str(ord(letter) - 64))
            else:
                result.append(str(ord(letter) - 96))
    return ' '.join(result)
