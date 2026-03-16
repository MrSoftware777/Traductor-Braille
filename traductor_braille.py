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
# Diccionario de números
numeros = {
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚',
}

#Prefijo para diferenciar un numero
PREFIJO_NUMERO = '⠼'

#Función de texto a braille
def texto_a_braille(texto):
    fila_braille = ''
    fila_letras = ''
    en_numero = False

    for letra in texto.lower():
        if letra.isdigit():
            if not en_numero:
                fila_braille += PREFIJO_NUMERO
                en_numero = True
            fila_braille += numeros[letra] + ' '
            fila_letras += letra + ' '
        
        else:
            en_numero = False
            simbolo = braille.get(letra, letra)
            fila_braille += simbolo + ' '
            fila_letras += letra + ' '
    
    return f"En Braille:\n{fila_braille}\n{fila_letras}"


#Función de braille a texto


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