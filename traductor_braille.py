braille = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵', ' ': ' ',
}

# Diccionario de números
numeros = {
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚',
}

#Prefijo para diferenciar un numero
PREFIJO_NUMERO = '⠼'

# AÑADIR después de la línea de PREFIJO_NUMERO
braille_a_letra  = {v: k for k, v in braille.items()}
braille_a_digito = {v: k for k, v in numeros.items()}

#Función de texto a braille
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
    
    return f"En Braille:\n{fila_braille}\n{fila_letras}"


def braille_a_texto(entrada_braille):
    tokens = entrada_braille.strip().split(' ')
    resultado = ''
    en_numero = False

    for token in tokens:
        if token == '':
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


# ====== Menú Principal ====

print("1. Texto a Braille")
print("2. Braille a Texto")
opcion = input("Elige una opción: ")

if opcion == '1':
    texto = input("Escribe un texto: ")
    resultado = texto_a_braille(texto)
    archivo_salida = "traduccion.txt"

elif opcion == '2':
    print("Pega el texto en Braille (simbolos separados por espacios):")

else:
    resultado = "Opcion no valida"
    archivo_salida = None

print(resultado)

if archivo_salida:
    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        archivo.write(resultado)

    print(f"Guardado en {archivo_salida}")