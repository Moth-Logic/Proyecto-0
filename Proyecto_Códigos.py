def cesarCod(texto, desplazamiento):
    """Cifrado César con soporte para Ñ"""
    alfabeto_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                           'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alfabeto_mayusculas = [letra.upper() for letra in alfabeto_minusculas]
    
    resultado = []
    
    for caracter in texto:
        if caracter in alfabeto_mayusculas:
            indice = alfabeto_mayusculas.index(caracter)
            nuevo_indice = (indice + desplazamiento) % 27
            resultado.append(alfabeto_mayusculas[nuevo_indice])
        elif caracter in alfabeto_minusculas:
            indice = alfabeto_minusculas.index(caracter)
            nuevo_indice = (indice + desplazamiento) % 27
            resultado.append(alfabeto_minusculas[nuevo_indice])
        else:
            resultado.append(caracter)
    
    texto_cifrado = ''.join(resultado)
    print(f"\nTexto cifrado: {texto_cifrado}")
    return texto_cifrado

def cesarDec(texto, desplazamiento):
    """Cifrado César con soporte para Ñ"""
    alfabeto_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                           'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alfabeto_mayusculas = [letra.upper() for letra in alfabeto_minusculas]
    
    resultado = []
    
    for caracter in texto:
        if caracter in alfabeto_mayusculas:
            indice = alfabeto_mayusculas.index(caracter)
            nuevo_indice = (indice - desplazamiento) % 27
            resultado.append(alfabeto_mayusculas[nuevo_indice])
        elif caracter in alfabeto_minusculas:
            indice = alfabeto_minusculas.index(caracter)
            nuevo_indice = (indice - desplazamiento) % 27
            resultado.append(alfabeto_minusculas[nuevo_indice])
        else:
            resultado.append(caracter)
    
    texto_descifrado = ''.join(resultado)
    print(f"\nTexto descifrado: {texto_descifrado}")
    return texto_descifrado


def monoCod(texto, palabra):
    print("*monoCod* (Por implementar)")


def monoDec(texto, palabra):
    print("*monoDec* (Por implementar)")


def vigenereCod(texto, palabra):
    print("*vigenereCod* (Por implementar)")


def vigenereDec(texto, palabra):
    print("*vigenereDec* (Por implementar)")


def playfairCod(texto, clave):
    print("*playfairCod* (Por implementar)")


def playfairDec(texto, clave):
    print("*playfairDec* (Por implementar)")


def railfenceCod(texto):
    print("*railfenceCod* (Por implementar)")


def railfenceDec(texto):
    print("*railfenceDec* (Por implementar)")


def escitalaCod(texto, lineas):
    print("*escitalaCod* (Por implementar)")


def escitalaDec(texto, lineas):
    print("*escitalaDec* (Por implementar)")


def presione_tecla():
    input("\nPresione Enter para continuar...")


def main():
    while True:
        
        print("        PROGRAMA DE CRIPTOGRAFÍA")
        print("  1. César")
        print("  2. Mono")
        print("  3. Vigenère")
        print("  4. Playfair")
        print("  5. Railfence")
        print("  6. Escítala")
        print("  7. Salir")
              
        try:
            cifrado = int(input("--->  Elija una opción (1-7): "))
            
            if cifrado == 7:
                print("\n¡Gracias por usar el programa!")
                print("Bai :3c")
                break
                
            if cifrado < 1 or cifrado > 7:
                print("\nError: Opción inválida. Elija un número entre 1 y 7.")
                presione_tecla()
                continue
                
        except ValueError:
            print("\nError: Debe ingresar un número entero.")
            presione_tecla()
            continue

        # Selección de acción (codificar/descodificar)
        try:
            accion = int(input("1. Codificar\n2. Descodificar\n Elija una opción (1 o 2): "))
            
            if accion != 1 and accion != 2:
                print("\nError: Debe elegir 1 o 2.")
                presione_tecla()
                continue
                
        except ValueError:
            print("\nError: Debe ingresar un número entero.")
            presione_tecla()
            continue

        # Entrada de texto
        while True:
            texto = input("\nInserte su texto: ").lower()
            espacios = texto.replace(" ", "")
            if espacios.isalpha() or espacios == "":
                break
            else:
                print("Error: Solo se permiten letras y espacios. Intente nuevamente.")

        # Procesar según el cifrado elegido
        if cifrado == 1:  # César
            if accion == 1:  # Codificar
                while True:
                    try:
                        desplazamiento = int(input("Inserte su desplazamiento: "))
                        break
                    except ValueError:
                        print("Error: El valor debe ser un número entero.")
                cesarCod(texto, desplazamiento)
            else:  # Decodificar
                while True:
                    try:
                        desplazamiento = int(input("Inserte su desplazamiento original: "))
                        break
                    except ValueError:
                        print("Error: El valor debe ser un número entero.")
                cesarDec(texto, desplazamiento)

        elif cifrado == 2:  # Mono
            while True:
                clave = input("Ingrese su clave (sin espacios): ").lower()
                if clave.isalpha() and clave != "":
                    break
                else:
                    print("Error: La clave debe contener solo letras.")
            if accion == 1:
                monoCod(texto, clave)
            else:
                monoDec(texto, clave)

        elif cifrado == 3:  # Vigenère
            while True:
                clave = input("Ingrese su clave (sin espacios): ").lower()
                if clave.isalpha() and clave != "":
                    break
                else:
                    print("Error: La clave debe contener solo letras.")
            if accion == 1:
                vigenereCod(texto, clave)
            else:
                vigenereDec(texto, clave)

        elif cifrado == 4:  # Playfair
            while True:
                clave = input("Ingrese su clave (sin espacios): ").lower()
                if clave.isalpha() and clave != "":
                    break
                else:
                    print("Error: La clave debe contener solo letras.")
            if accion == 1:
                playfairCod(texto, clave)
            else:
                playfairDec(texto, clave)

        elif cifrado == 5:  # Railfence
            if accion == 1:
                railfenceCod(texto)
            else:
                railfenceDec(texto)

        elif cifrado == 6:  # Escítala
            while True:
                try:
                    vueltas = int(input("Ingrese la cantidad de vueltas: "))
                    if vueltas > 1:
                        break
                    else:
                        print("Error: La cantidad de vueltas debe ser mayor que 1.")
                except ValueError:
                    print("Error: El valor debe ser un número entero.")
            if accion == 1:
                escitalaCod(texto, vueltas)
            else:
                escitalaDec(texto, vueltas)

        presione_tecla()


if __name__ == "__main__":
    main()
