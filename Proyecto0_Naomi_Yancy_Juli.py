def cesarCod(texto, desplazamiento):
    print("Código César")
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def cesarDec(texto, desplazamiento):
    print("*cesarDec*")

def monoCod(texto, palabra):
    print("*monoCod*")

def monoDec(texto, palabra):
    print("*monoDec*")

def vigenereCod(texto, palabra):
    print("*vigenereCod*")

def vigenereDec(texto, palabra):
    print("*vigenereDec*")

def playfairCod(texto, palabra):
    print("*playfairCod*")

def playfairDec(texto, palabra):
    print("*playfairDec*")

def railfenceCod(texto):
    print("*railfenceCod*")

def railfenceDec(texto):
    print("*railfenceDec*")

def escitalaCod(texto, lineas):
    print("*escitalaCod*")

def escitalaDec(texto, lineas):
    print("*escitalaDec*")

def main():
    print("1. Cesar")
    print("2. Mono")
    print("3. Vigenere")
    print("4. Playfair")
    print("5. Railfence")
    print("6. Escitala")
    cifrado = int(input("Elija una opción (del 1 al 6): "))

    if cifrado < 1 or cifrado > 6:
        print("ERROR: Ponga algo válido.")
        main()
    
    print("1. Codificar")
    print("2. Descodificar")
    accion = int(input("Elija una opción (1 o 2): "))
    while accion != 1 and accion != 2:
        print("ERROR: Ponga algo válido")
        accion = int(input("Elija una opción (1 o 2): "))
    
    print("Exprésenos que texto quiere codificar/descodificar: ")
    texto = input("Inserte su texto: ").lower()
    espacios = texto.replace(" ","")
    while espacios.isalpha() == False:
        print("Exprésenos algo legible")
        texto = input("Inserte su texto: ").lower()
        espacios = texto.replace(" ","")
 
    if cifrado == 1:
        if accion == 1:
            desplazamiento = input("Inserte su desplazamiento: ")
            cesarCod("texto", "desplazamiento")
        elif accion == 2:
            desplazamiento = input("Inserte su desplazamiento inverso: ")
            cesarDec("texto", "desplazamiento")
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
            escitalaCod("texto", "vueltas")
        else:
            escitalaDec("texto", "vueltas")

if __name__ == "__main__":
    main()
