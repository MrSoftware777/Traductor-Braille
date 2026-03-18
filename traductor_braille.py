braille = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵', ' ': ' ',
}

numeros = {
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚',
}

PREFIJO_NUMERO = '⠼'

braille_a_letra  = {v: k for k, v in braille.items()}
braille_a_digito = {v: k for k, v in numeros.items()}


def texto_a_braille(texto):
    fila_braille = ''
    fila_letras = ''
    en_numero = False

    for letra in texto.lower():
        if letra.isdigit():
            if not en_numero:
                fila_braille += PREFIJO_NUMERO + ' '
                en_numero = True
            fila_braille += numeros[letra] + ' '
            fila_letras += letra + ' '
        else:
            en_numero = False
            simbolo = braille.get(letra, letra)
            fila_braille += simbolo + ' '
            fila_letras += letra + ' '

    # Guarda solo la cadena braille, sin texto adicional
    with open("traduccion.txt", "w", encoding="utf-8") as archivo:
        archivo.write(fila_braille.strip())

    return f"En Braille:\n{fila_braille.strip()}\n{fila_letras.strip()}"



def braille_a_texto():
    # Lee directamente desde el archivo generado por texto_a_braille
    with open("traduccion.txt", "r", encoding="utf-8") as archivo:
        entrada_braille = archivo.read()

    tokens = entrada_braille.strip().split(' ')
    resultado = ''
    en_numero = False

    for token in tokens:
        if token == '':
            if resultado and resultado[-1] != ' ':
                resultado += ' '
            en_numero = False
            continue

        if token == PREFIJO_NUMERO:
            en_numero = True
            continue

        if en_numero:
            digito = braille_a_digito.get(token)
            if digito:
                resultado += digito
            else:
                en_numero = False
                letra = braille_a_letra.get(token, '?')
                resultado += letra
        else:
            letra = braille_a_letra.get(token, '?')
            resultado += letra

    return f"Texto traducido:\n{resultado}"


# ====== Menú Principal ======

print("1. Texto a Braille")
print("2. Braille a Texto")
opcion = input("Elige una opción: ")

if opcion == '1':
    texto = input("Escribe un texto: ")
    resultado = texto_a_braille(texto)          # el guardado ocurre dentro de la función
    print(resultado)
    print("Guardado en: traduccion.txt")

# DESPUÉS
elif opcion == '2':
    resultado = braille_a_texto()   # sin argumentos, lee del archivo directamente
    print(resultado)

else:
    print("Opción no válida")