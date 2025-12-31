import time
import sys

def fala(texto, velocidade=0.03):
    for palavra in texto:
        print(palavra, end="", flush=True)
        time.sleep(velocidade)
    print()