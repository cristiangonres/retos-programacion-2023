'''/*
* Escribe un programa que reciba un texto y transforme lenguaje natural a
* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
*  se caracteriza por sustituir caracteres alfanuméricos.
* - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
*   con el alfabeto y los números en "leet".
*   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
*/'''

def transform_to_leet(text):
    leet_dict = {
    'a': '4', 'A': '4',
    'b': '13', 'B': '13',
    'c': '<', 'C': '<',
    'd': '|)', 'D': '|)',
    'e': '3', 'E': '3',
    'f': '|=', 'F': '|=',
    'g': '6', 'G': '6',
    'h': '|-|', 'H': '|-|',
    'i': '1', 'I': '1',
    'j': '_|', 'J': '_|',
    'k': '|<', 'K': '|<',
    'l': '|_', 'L': '|_',
    'm': '|\\/|', 'M': '|\\/|',
    'n': '|\\|', 'N': '|\\|',
    'o': '0', 'O': '0',
    'p': '|D', 'P': '|D',
    'q': '(,)', 'Q': '(,)',
    'r': '|2', 'R': '|2',
    's': '5', 'S': '5',
    't': '7', 'T': '7',
    'u': '|_|', 'U': '|_|',
    'v': '\\/', 'V': '\\/',
    'w': '\\/\\/', 'W': '\\/\\/',
    'x': '><', 'X': '><',
    'y': '`/', 'Y': '`/',
    'z': '2', 'Z': '2',
}
    for letter in text:
        if letter in leet_dict:
            text = text.replace(letter, leet_dict[letter])
    return text

text = transform_to_leet(input('Escribe tu texto: \n'))
print(text)

