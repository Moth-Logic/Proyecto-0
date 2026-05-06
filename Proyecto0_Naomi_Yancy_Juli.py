def cesarCod(texto, desplazamiento):
    print("Código César")
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesarDec(texto, desplazamiento):
    print("Descifrado César")
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def monoCod(texto, palabra):
    print("*monoCod*")

def monoDec(texto, palabra):
    print("*monoDec*")
    

def vigenereCod(texto, palabra):
    print("*vigenereCod*")
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def vigenereDec(texto, palabra):
    print("*vigenereDec*")
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   
def playfairCod(texto, clave):
    print("*playfairCod*")

def playfairDec(texto, clave):
    print("*playfairDec*")

def railfenceCod(texto):
    print("*railfenceCod*")

def railfenceDec(texto):
    print("*railfenceDec*")

def escitalaCod(texto, lineas):
    print("*escitalaCod*")

def escitalaDec(texto, lineas):
    print("*escitalaDec*")

def presione_tecla():
    input("\nPresione enter para continuar...")

def main():
    while True:
        print("\n=== CRIPTOGRAFÍA ===")
        print("1. Cesar")
        print("2. Mono")
        print("3. Vigenere")
        print("4. Playfair")
        print("5. Railfence")
        print("6. Escitala")
        print("7. Salir")
        
def main():
    while True:
        try:
            cifrado = int(input("Elija una opción (del 1 al 7): "))
            if cifrado == 7:
                print("Bai :3c")
                break
            if cifrado < 1 or cifrado > 7:
                print("Error: Opción inválida. Elija un número entre 1 y 7.")
                presione_tecla()
                continue
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            presione_tecla()
            continue

        try:
            accion = int(input("1. Codificar\n2. Descodificar\nElija una opción (1 o 2): "))
            if accion != 1 and accion != 2:
                print("Error: Debe elegir 1 o 2.")
                presione_tecla()
                continue
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            presione_tecla()
            continue

        while True:
            texto = input("Inserte su texto: ").lower()
            espacios = texto.replace(" ", "")
            if espacios.isalpha() or espacios == "":
                break
            else:
                print("Error: Solo se permiten letras y espacios. Intente nuevamente.")

        if cifrado == 1:
            if accion == 1:
                while True:
                    try:
                        desplazamiento = int(input("Inserte su desplazamiento: "))
                        break
                    except ValueError:
                        print("Error: El valor debe ser un número entero. Intente nuevamente.")
                cesarCod(texto, desplazamiento)
            elif accion == 2:
                while True:
                    try:
                        desplazamiento = int(input("Inserte su desplazamiento inverso: "))
                        break
                    except ValueError:
                        print("Error: El valor debe ser un número entero. Intente nuevamente.")
                cesarDec(texto, desplazamiento)

        elif cifrado == 2:
            while True:
                clave = input("Ingrese su clave (sin espacios): ").lower()
                if clave.isalpha() and clave != "":
                    break
                else:
                    print("Error: La clave debe contener solo letras (sin números, espacios ni símbolos). Intente nuevamente.")
            if accion == 1:
                monoCod(texto, clave)
            else:
                monoDec(texto, clave)

        elif cifrado == 3:
            while True:
                clave = input("Ingrese su clave (sin espacios): ").lower()
                if clave.isalpha() and clave != "":
                    break
                else:
                    print("Error: La clave debe contener solo letras (sin números, espacios ni símbolos). Intente nuevamente.")
            if accion == 1:
                vigenereCod(texto, clave)
            else:
                vigenereDec(texto, clave)

        elif cifrado == 4:
            while True:
                clave = input("Ingrese su clave (sin espacios): ").lower()
                if clave.isalpha() and clave != "":
                    break
                else:
                    print("Error: La clave debe contener solo letras (sin números, espacios ni símbolos). Intente nuevamente.")
            if accion == 1:
                playfairCod(texto, clave)
            else:
                playfairDec(texto, clave)

        elif cifrado == 5:
            if accion == 1:
                railfenceCod(texto)
            else:
                railfenceDec(texto)

        elif cifrado == 6:
            while True:
                try:
                    vueltas = int(input("Ingrese la cantidad de vueltas: "))
                    if vueltas > 1:
                        break
                    else:
                        print("Error: La cantidad de vueltas debe ser mayor que 1. Intente nuevamente.")
                except ValueError:
                    print("Error: El valor debe ser un número entero. Intente nuevamente.")
            if accion == 1:
                escitalaCod(texto, vueltas)
            else:
                escitalaDec(texto, vueltas)

        presione_tecla()


if __name__ == "__main__":
    main()
