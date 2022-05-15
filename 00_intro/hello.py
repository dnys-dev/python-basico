#!/usr/bin/env python3

"""Hello World Multi Linguas.

Dependendo da linha configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar: 

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python hellopy
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Daviny Vidal"
__license__ = "GNU v3"

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "olá, Mundo"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "bonjour Monde"

# Este programa imprime Hello World
print(msg)