morse_code_dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': ' '
}

def encrypt_morse_code(text):
    encrypted_text = ''
    for char in text:
        if char in morse_code_dict:
            encrypted_text += morse_code_dict[char] + ' '
        else:
            print(f"Unsupported character: {char}")
    return encrypted_text

def decode_morse_code(morse_code):
    decoded_text = ''
    morse_code_words = morse_code.split(' ')
    for morse_code_word in morse_code_words:
        for key, value in morse_code_dict.items():
            if morse_code_word == value:
                decoded_text += key
                break
    return decoded_text
