# 🔡 Traductor-Braille

Un traductor de consola en Python capaz de convertir texto en español a lenguaje Braille y viceversa, con soporte para letras, espacios y números.

---

## 📋 Descripción general

Este proyecto nació como una herramienta educativa para facilitar la comprensión del sistema de escritura Braille. Permite a cualquier usuario traducir texto escrito en español hacia sus símbolos Braille equivalentes, y también realizar el proceso inverso: interpretar una cadena de símbolos Braille y convertirla de regreso a texto legible.

---

## ⚙️ Funcionalidades

| Función | Descripción |
|---|---|
| `texto_a_braille(texto)` | Convierte una cadena de texto en español a símbolos Braille separados por espacios |
| `braille_a_texto(entrada)` | Convierte una cadena de símbolos Braille de vuelta a texto en español |
| Modo numérico | Detecta dígitos y antepone el prefijo `⠼` para diferenciarlos de las letras |
| Guardado automático | El resultado de cada traducción se guarda en `traduccion.txt` |

---

## 🧠 ¿Cómo funciona internamente?

### Diccionarios de traducción
- `braille` — mapea cada letra del alfabeto español y el espacio a su símbolo Braille.
- `numeros` — mapea los dígitos `0–9` a sus símbolos Braille.
- `braille_a_letra` y `braille_a_digito` — versiones inversas generadas automáticamente con dict comprehension para la traducción de vuelta.

### El prefijo numérico `⠼`
Las letras `a–j` y los dígitos `1–0` comparten los mismos símbolos Braille. Para resolver esta ambigüedad, el estándar Braille utiliza el prefijo `⠼` antes de cualquier secuencia numérica. El programa activa una bandera `en_numero` al detectarlo y la desactiva al encontrar una letra o espacio.

---

## 🚀 Cómo ejecutarlo

### Requisitos
- Python 3.x
- Terminal con soporte UTF-8 (para visualizar los símbolos Braille correctamente)

### Instalación
```bash
git clone https://github.com/MrSoftware777/Traductor-Braille.git
cd Traductor-Braille
```

### Uso
```bash
python traductor_braille.py
```

Se mostrará el menú:
```
1. Texto a Braille
2. Braille a Texto
Elige una opción:
```

#### Ejemplo — Texto a Braille
```
Escribe un texto: hola 42

En Braille:
⠓ ⠕ ⠇ ⠁   ⠼ ⠙ ⠃
h o l a   4 2
```

#### Ejemplo — Braille a Texto
```
Pega el texto en Braille: ⠓ ⠕ ⠇ ⠁   ⠼ ⠙ ⠃

Texto traducido:
hola 42
```

---

## 🧪 Pruebas

El proyecto incluye un archivo de pruebas unitarias:
```bash
python test_braille.py
```

Cubre los siguientes casos:
- Letras simples
- Palabras con espacios
- Secuencias numéricas
- Texto mezclado con números
- Prueba de ida y vuelta (texto → braille → texto)

---

## 📁 Estructura del proyecto
```
Traductor-Braille/
│
├── traductor_braille.py   # Lógica principal y menú
├── test_braille.py        # Pruebas unitarias
├── traduccion.txt         # Archivo de salida generado automáticamente
├── README.md
└── LICENSE
```

---

## 🌿 Ramas y flujo de trabajo

| Rama | Propósito |
|---|---|
| `main` | Código estable y revisado |
| `ajusteDocumento` | Reorganización del archivo y creación del menú — PR #1 mergeado |
| `feature/braile_a_texto` | Implementación de la función de traducción inversa |

---


## 👥 Autores

| Usuario | Rol |
|---|---|
| [@MrSoftware777](https://github.com/MrSoftware777) | Creador y mantenedor |
| [@BraSanchez](https://github.com/BraSanchez) | Colaborador |
| [@Yarisa-crypto](https://github.com/Yarisa-crypto) | Colaborador |
| [@EnmanuelVelasquez](https://github.com/EnmanuelVelasquez) | Colaborador |

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT** — consulta el archivo [LICENSE](LICENSE) para más detalles.