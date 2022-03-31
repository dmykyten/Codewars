def decode_morse(morse_code):
    word_counter = 0
    decoded_msg = []
    words = morse_code.split('   ')
    for word in words:
        if word == '':
            continue
        decoded_msg.append('')
        for char in word.split():
            decoded_msg[word_counter] += MORSE_CODE[char]
        word_counter += 1
    return ' '.join(decoded_msg)
