def cesarCod(texto, desplazamiento):
    """Cifrado César con soporte para Ñ. Mueve las letras dependiendo del dezplazamiento
    Entradas y Restricciones: 
    Texto: un string, puede incluir espacios Y guiones.
    Restricciones: No se permiten otros caracteres raros.
    Salidas: Su texto cifrado."""
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
    """Descifrado César con soporte para Ñ. Mueve las letras dependiendo del dezplazamiento
    Entradas y Restricciones: 
    Texto: un string, puede incluir espacios Y guiones.
    Restricciones: No se permiten otros caracteres raros.
    Salidas: Su texto descifrado."""
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
    """"""
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print("*monoalfabeticoCod*")
    sinRepetir = ""

    for letra in palabra.lower():
        if letra not in sinRepetir:
            sinRepetir += letra
    
    alfabetoClave=sinRepetir
    for letra in alfabeto:
        if letra not in alfabetoClave:
            alfabetoClave += letra
            
    #sustitucion por posicion        
    mensajeCifrado = ""
    for letra in texto.lower():
        if letra in alfabeto:
            posicion= alfabeto.index(letra)
            mensajeCifrado += alfabetoClave[posicion]
        else:
            mensajeCifrado += letra

    print(mensajeCifrado)
    return mensajeCifrado


def monoDec(texto, palabra):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print("*monoDec*")

    sinRepetir=""
    for letra in palabra.lower():
        if letra not in sinRepetir and letra in alfabeto:
            sinRepetir += letra

    alfabetoClave = sinRepetir
    for letra in alfabeto:
        if letra not in alfabetoClave:
            alfabetoClave += letra

    mensajeDescifrado = ""
    for letra in texto.lower():
        if letra in alfabetoClave:
            posicion = alfabetoClave.index(letra)
            mensajeDescifrado += alfabeto[posicion]
        else:
            mensajeDescifrado += letra

    print(mensajeDescifrado)
    return mensajeDescifrado

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
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz123")
    
    claveunica = []
    for letra in clave:
        if letra not in claveunica:
            claveunica.append(letra)
    for letra in alfabeto:
        if letra not in claveunica:
            claveunica.append(letra)
    
    matriz = [claveunica[i*5:(i+1)*5] for i in range(6)]
    
    mensaje2 = []
    for i in range(len(texto)):
        if i < len(texto)-1 and texto[i] == texto[i+1]:
            mensaje2.append(texto[i])
            mensaje2.append('1')
        else:
            mensaje2.append(texto[i])
    if len(mensaje2) % 2 != 0:
        mensaje2.append('1')
    
    pares = [mensaje2[i:i+2] for i in range(0, len(mensaje2), 2)]
    
    def buscar(letra):
        for i in range(6):
            for j in range(5):
                if matriz[i][j] == letra:
                    return i, j
        raise ValueError(f"Carácter '{letra}' no encontrado en la matriz")

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
        else:                      # diferente todo -> intercambiar columnas
            cifrado.append(matriz[fa][cb])
            cifrado.append(matriz[fb][ca])

    resultadoplayfair = "".join(cifrado)
    print(resultadoplayfair)


def playfairDec(texto, clave):
    print("*playfairDec*")
    alfabeto = list("abcdefghijklmnñopqrstuvwxyz123")
    
    claveunica = []
    for letra in clave:
        if letra not in claveunica:
            claveunica.append(letra)
    for letra in alfabeto:
        if letra not in claveunica:
            claveunica.append(letra)
    
    matriz = [claveunica[i*5:(i+1)*5] for i in range(6)]
    
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
        else:                      # diferente todo intercammbiar columnas
            descifrado.append(matriz[fa][cb])
            descifrado.append(matriz[fb][ca])
    
    resultado = []
    i = 0
    while i < len(descifrado):
        if descifrado[i] == '1':
            if i > 0 and i < len(descifrado)-1 and descifrado[i-1] == descifrado[i+1]:
                i += 1
                continue
            if i == len(descifrado)-1:
                i += 1
                continue
        resultado.append(descifrado[i])
        i += 1
    
    resultadoplayfair = "".join(resultado)
    print(resultadoplayfair)


def railfenceCod(texto):
    print("*railfenceCod*")
    rieles = 3

    lista_rieles = []
    for i in range(rieles):
        lista_rieles.append("")

    fila = 0          
    direccion = 1   

    for letra in texto:
        lista_rieles[fila] = lista_rieles[fila] + letra
        if fila == 0:
            direccion = 1
        elif fila == rieles - 1:
            direccion = -1
        fila = fila + direccion

    cifrado = ""
    for riel in lista_rieles:
        cifrado = cifrado + riel

    print("\nRieles:")
    for i in range(rieles):
        print("Riel", i + 1, ":", lista_rieles[i])

    print("\nTexto cifrado:", cifrado)

def railfenceDec(texto):
    print("*railfenceDec*")

    rieles = 3

    matriz = []
    for i in range(rieles):
        fila = []
        for j in range(len(texto)):
            fila.append("")
        matriz.append(fila)

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

    print("\nMatriz reconstruida:")
    for i in range(rieles):
        print(matriz[i])

    print("\nTexto descifrado:", resultado)


def escitalaCod(texto, lineas):
    print("*escitalaCod*")
    
    while len(texto) % lineas != 0:
        texto += " "

    texto = texto.replace(" ", "-")

    filas = [""] * lineas

    for i, letra in enumerate(texto):
        fila = i % lineas
        filas[fila] += letra
    
    textoCodificado = ''.join(filas)
    
    resultado = ''
    for i in range(0, len(textoCodificado), 5):
        separar = ''.join(textoCodificado[i:i+5])
        resultado += separar + ' '

    print(resultado)
    return resultado



def escitalaDec(texto, lineas):
    print("*escitalaDec*")
    
    texto = texto.replace(" ", "")

    columnas = len(texto) // lineas

    filas = []
    inicio = 0
    for i in range(lineas):
        fin = inicio + columnas
        filas.append(texto[inicio:fin])
        inicio = fin

    resultado = ""
    for c in range(columnas):
        for f in range(lineas):
            resultado += filas[f][c]

    resultado = resultado.replace("-", " ")
    print(resultado.rstrip())


def presione_tecla():
    input("\nPresione Enter para continuar...")


def main():
    """PROGRAMA DE CRIPTOGRAFIA: Un programa hecho por Naomi Amador, Yancy Jiron y Julián Solórzano.
       Contiene 6 estilos de criptografía: (César, Mono, Vigenére, Playfair, Railfence y Escítala)
       
       Para usarlo existe un menú que tiene 7 opciones, la última es para Salir del Programa.
       Después de escoger el cifrado, te va a pedir si quiere cifrar o descifrar, y de ahí 
       te pedirá texto y algun otro valor necesario para el cifrado. Lindo Día! :3"""
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
            print("\nAtención: Si su escogencia es Playfair, solo se permiten letras. Sin espacios")
            texto = input("Inserte su texto: ").lower()
            espacios = texto.replace(" ", "")
            if espacios.isalpha() or espacios == "" or (char.isdigit() for char in texto):
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