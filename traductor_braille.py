braille = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵', ' ': ' ',
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚',
}

texto = input("Escribe un texto: ").lower()

fila_braille = ''
fila_letras = ''

for letra in texto:
    simbolo = braille.get(letra, letra)
    fila_braille += simbolo + ' '
    fila_letras += letra + ' '

resultado = f"En Braille:\n{fila_braille}\n{fila_letras}"
print(resultado)

with open("traduccion.txt", "w", encoding="utf-8") as archivo:
    archivo.write(resultado)

print("Guardado en traduccion.txt")