def cesarCod(texto, desplazamiento):
    print("*cesarCod*")
    print(f"Codificando: {texto} con desplazamiento {desplazamiento}")

def cesarDec(texto, desplazamiento):
    print("*cesarDec*")
    print(f"Descodificando: {texto} con desplazamiento {desplazamiento}")

def monoCod(texto, palabra):
    print("*monoCod*")
    print(f"Codificando: {texto} con palabra clave {palabra}")

def monoDec(texto, palabra):
    print("*monoDec*")
    print(f"Descodificando: {texto} con palabra clave {palabra}")

def vigenereCod(texto, palabra):
    print("*vigenereCod*")
    print(f"Codificando: {texto} con palabra clave {palabra}")

def vigenereDec(texto, palabra):
    print("*vigenereDec*")
    print(f"Descodificando: {texto} con palabra clave {palabra}")

def playfairCod(texto, palabra):
    print("*playfairCod*")
    print(f"Codificando: {texto} con palabra clave {palabra}")

def playfairDec(texto, palabra):
    print("*playfairDec*")
    print(f"Descodificando: {texto} con palabra clave {palabra}")

def railfenceCod(texto):
    print("*railfenceCod*")
    print(f"Codificando: {texto}")

def railfenceDec(texto):
    print("*railfenceDec*")
    print(f"Descodificando: {texto}")

def escitalaCod(texto, lineas):
    print("*escitalaCod*")
    print(f"Codificando: {texto} con {lineas} líneas")

def escitalaDec(texto, lineas):
    print("*escitalaDec*")
    print(f"Descodificando: {texto} con {lineas} líneas")

def main():
    print("1. Cesar")
    print("2. Mono")
    print("3. Vigenere")
    print("4. Playfair")
    print("5. Railfence")
    print("6. Escitala")
    cifrado = int(input("Elige un número: "))
    
    print("1. Codificar")
    print("2. Descodificar")
    accion = int(input("Elige 1 o 2: "))
    
    if cifrado == 1:
        if accion == 1:
            cesarCod("texto", 3)
        else:
            cesarDec("texto", 3)
    elif cifrado == 2:
        if accion == 1:
            monoCod("texto", "clave")
        else:
            monoDec("texto", "clave")
    elif cifrado == 3:
        if accion == 1:
            vigenereCod("texto", "clave")
        else:
            vigenereDec("texto", "clave")
    elif cifrado == 4:
        if accion == 1:
            playfairCod("texto", "clave")
        else:
            playfairDec("texto", "clave")
    elif cifrado == 5:
        if accion == 1:
            railfenceCod("texto")
        else:
            railfenceDec("texto")
    elif cifrado == 6:
        if accion == 1:
            escitalaCod("texto", 3)
        else:
            escitalaDec("texto", 3)

if __name__ == "__main__":
    main()
