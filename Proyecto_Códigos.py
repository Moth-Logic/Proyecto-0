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
    print("*vigenereCod*")
    resultado = ""
    clave = 0

    for letra in texto:
        alfabeto = "abcdefghijklmnñopqrstuvwxyz"
        if letra == " ":
            resultado += " "
            continue
        posicionTexto = alfabeto.index(letra)
        letraClave = palabra[clave % len(palabra)]
        posicionClave = alfabeto.index(letraClave)
        posicion2 = (posicionTexto + posicionClave) % len(alfabeto)
        resultado += alfabeto[posicion2]
        clave += 1

    print("Texto codificado: ", resultado)
    return resultado

def vigenereDec(texto, palabra):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    print("*vigenereDec*")
    resultado = ""
    clave = 0

    for letra in texto:
        if letra == " ":
            resultado += " "
            continue
        posicionTexto = alfabeto.index(letra)
        letraClave = palabra[clave % len(palabra)]
        posicionClave = alfabeto.index(letraClave)
        posicion2 = (posicionTexto - posicionClave) % len(alfabeto)
        resultado += alfabeto[posicion2]
        clave += 1

    print("Texto descifrado: ", resultado)
    return resultado
    

def playfairCod(texto, clave):
    print("*playfairCod*")
    # Alfabeto completo: a-z, ñ, y dígitos 1,2,3 (total 30 caracteres)
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz123")
    
    # Construir clave única (primero los caracteres de la clave en orden, luego el resto del alfabeto)
    claveunica = []
    for letra in clave:
        if letra not in claveunica:
            claveunica.append(letra)
    for letra in alfabeto:
        if letra not in claveunica:
            claveunica.append(letra)
    
    # Crear matriz 6x5 a partir de la clave única
    matriz = [claveunica[i*5:(i+1)*5] for i in range(6)]
    
    # Preprocesar el texto: insertar '1' entre letras duplicadas y añadir '1' al final si la longitud es impar
    mensaje2 = []
    for i in range(len(texto)):
        if i < len(texto)-1 and texto[i] == texto[i+1]:
            mensaje2.append(texto[i])
            mensaje2.append('1')
        else:
            mensaje2.append(texto[i])
    if len(mensaje2) % 2 != 0:
        mensaje2.append('1')
    
    # Dividir en pares de caracteres
    pares = [mensaje2[i:i+2] for i in range(0, len(mensaje2), 2)]
    
    # Función auxiliar para buscar la posición de una letra en la matriz
    def buscar(letra):
        for i in range(6):
            for j in range(5):
                if matriz[i][j] == letra:
                    return i, j
        raise ValueError(f"Carácter '{letra}' no encontrado en la matriz")
    
    # Cifrar cada par según las reglas de Playfair
    cifrado = []
    for a, b in pares:
        fa, ca = buscar(a)
        fb, cb = buscar(b)
        if fa == fb:               # misma fila -> desplazar derecha
            cifrado.append(matriz[fa][(ca+1)%5])
            cifrado.append(matriz[fb][(cb+1)%5])
        elif ca == cb:             # misma columna -> desplazar abajo
            cifrado.append(matriz[(fa+1)%6][ca])
            cifrado.append(matriz[(fb+1)%6][cb])
        else:                      # rectángulo -> intercambiar columnas
            cifrado.append(matriz[fa][cb])
            cifrado.append(matriz[fb][ca])

    resultadoplayfair = "".join(cifrado)
    print(resultadoplayfair)


def playfairDec(texto, clave):
    print("*playfairDec*")
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz123")
    
    # Matriz de la clave
    claveunica = []
    for letra in clave:
        if letra not in claveunica:
            claveunica.append(letra)
    for letra in alfabeto:
        if letra not in claveunica:
            claveunica.append(letra)
    
    matriz = [claveunica[i*5:(i+1)*5] for i in range(6)]
    
    # Es par? referencia a flowgorithm
    if len(texto) % 2 != 0:
        raise ValueError("El texto cifrado debe tener longitud par")
    
    pares = [texto[i:i+2] for i in range(0, len(texto), 2)]
    
    def buscar(letra):
        for i in range(6):
            for j in range(5):
                if matriz[i][j] == letra:
                    return i, j
        raise ValueError(f"Carácter '{letra}' no encontrado en la matriz")
    
    # Descifrar cada par: reglas inversas
    descifrado = []
    for a, b in pares:
        fa, ca = buscar(a)
        fb, cb = buscar(b)
        if fa == fb:               # misma fila desplazar izquierda
            descifrado.append(matriz[fa][(ca-1)%5])
            descifrado.append(matriz[fb][(cb-1)%5])
        elif ca == cb:             # misma columna desplaza arriba
            descifrado.append(matriz[(fa-1)%6][ca])
            descifrado.append(matriz[(fb-1)%6][cb])
        else:                      # rectángulo intercammbiar columnas
            descifrado.append(matriz[fa][cb])
            descifrado.append(matriz[fb][ca])
    
    # quitar 1
    resultado = []
    i = 0
    while i < len(descifrado):
        if descifrado[i] == '1':
            # Si es 1 interno y está entre dos letras iguales, lo saltamos
            if i > 0 and i < len(descifrado)-1 and descifrado[i-1] == descifrado[i+1]:
                i += 1
                continue
            # Si es 1 al final, lo saltamos
            if i == len(descifrado)-1:
                i += 1
                continue
        # en el whateevr
        resultado.append(descifrado[i])
        i += 1
    
    resultadoplayfair = "".join(resultado)
    print(resultadoplayfair)


def railfenceCod(texto):
    print("*railfenceCod*")
    # Siempre van a ser 3 rieles lmao
    rieles = 3

# Creamos una lista vacía para guardar cada riel

    lista_rieles = []
    for i in range(rieles):
        lista_rieles.append("")

# Que riel estamos
    fila = 0          
    direccion = 1   

# cada letra del texto
    for letra in texto:
        lista_rieles[fila] = lista_rieles[fila] + letra
        if fila == 0:
            direccion = 1
        elif fila == rieles - 1:
            direccion = -1
        fila = fila + direccion

# Unimos todo
    cifrado = ""
    for riel in lista_rieles:
        cifrado = cifrado + riel

# Mostramos los rieles
    print("\nRieles:")
    for i in range(rieles):
        print("Riel", i + 1, ":", lista_rieles[i])

# final
    print("\nTexto cifrado:", cifrado)

def railfenceDec(texto):
    print("*railfenceDec*")

    # Always 3 rails
    rieles = 3

    # - "rieles" filas
    # - len(texto) columnas

    matriz = []
    for i in range(rieles):
        fila = []
        for j in range(len(texto)):
            fila.append("")
        matriz.append(fila)

    # pasito a pasito suve suavecito

    fila = 0
    direccion = 1

    for columna in range(len(texto)):
        matriz[fila][columna] = "*"

        if fila == 0:
            direccion = 1
        elif fila == rieles - 1:
            direccion = -1

        fila = fila + direccion

    # cambiar * por el texto

    indice = 0

    for i in range(rieles):
        for j in range(len(texto)):
            if matriz[i][j] == "*":
                matriz[i][j] = texto[indice]
                indice = indice + 1

    # Leer la matriz siguiendo el zigzag original

    resultado = ""

    fila = 0
    direccion = 1

    for columna in range(len(texto)):
        resultado = resultado + matriz[fila][columna]

        if fila == 0:
            direccion = 1
        elif fila == rieles - 1:
            direccion = -1

        fila = fila + direccion

    # Mostrar matriz lmao
    print("\nMatriz reconstruida:")
    for i in range(rieles):
        print(matriz[i])

    #show ur super cool text
    print("\nTexto descifrado:", resultado)


def escitalaCod(texto, lineas):
    print("*escitalaCod* (Por implementar)")


def escitalaDec(texto, lineas):
    print("*escitalaDec* (Por implementar)")


def presione_tecla():
    input("\nPresione Enter para continuar...")


def main():
    # Menú. Uno escoje del 1 al 6 para cifrado. 7 para salir. 
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
            print("Atención: Si su escogencia es Playfair, solo se permiten letras. Sin espacios")
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
