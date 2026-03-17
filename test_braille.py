from traductor_braille import braille_a_texto, texto_a_braille

# ── Casos de prueba ──────────────────────────────────────────────────────────

def test_letras_simples():
    resultado = braille_a_texto('⠓ ⠕ ⠇ ⠁')
    assert resultado == 'Texto traducido:\nhola', f"Falló: {resultado}"
    print("✅ test_letras_simples pasó")

def test_con_espacio():
    resultado = braille_a_texto('⠓ ⠕ ⠇ ⠁   ⠍ ⠥ ⠝ ⠙ ⠕')
    assert resultado == 'Texto traducido:\nhola mundo', f"Falló: {resultado}"
    print("✅ test_con_espacio pasó")

def test_con_numeros():
    resultado = braille_a_texto('⠼ ⠙ ⠃')
    assert resultado == 'Texto traducido:\n42', f"Falló: {resultado}"
    print("✅ test_con_numeros pasó")

def test_texto_y_numero_mezclados():
    resultado = braille_a_texto('⠓ ⠕ ⠇ ⠁   ⠼ ⠙ ⠃')
    assert resultado == 'Texto traducido:\nhola 42', f"Falló: {resultado}"
    print("✅ test_texto_y_numero_mezclados pasó")

def test_ida_y_vuelta():
    """Convierte a braille y luego regresa: el texto debe ser igual"""
    original = 'hola mundo'
    braille = texto_a_braille(original)
    # Extraemos solo la fila de símbolos braille (primera línea del resultado)
    fila_braille = braille.split('\n')[1]
    resultado = braille_a_texto(fila_braille)
    assert resultado == f'Texto traducido:\n{original}', f"Falló: {resultado}"
    print("✅ test_ida_y_vuelta pasó")

# ── Ejecutar todos ───────────────────────────────────────────────────────────

if __name__ == '__main__':
    test_letras_simples()
    test_con_espacio()
    test_con_numeros()
    test_texto_y_numero_mezclados()
    test_ida_y_vuelta()
    print("\n✅ Todas las pruebas pasaron")