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
    ' ': '/'
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

user_input = input("Please enter text to encrypt or Morse code to decode: ")
mode = input("Enter 'encrypt' to encrypt text or 'decode' to decode Morse code: ")

if mode.lower() == 'encrypt':
    encrypted_text = encrypt_morse_code(user_input.lower())
    print("Encrypted text:", encrypted_text)
elif mode.lower() == 'decode':
    decoded_text = decode_morse_code(user_input)
    print("Decoded text:", decoded_text)
else:
    print("Invalid mode. Please enter 'encrypt' or 'decode'.")
    
def decode_morse_code(morse_code):
    decoded_text = ''
    morse_code_words = morse_code.split(' ')
    for morse_code_word in morse_code_words:
        for key, value in morse_code_dict.items():
            if morse_code_word == value:
                decoded_text += key
                break
    return decoded_text
