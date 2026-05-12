alfabeto = "abcdefghijklmnñopqrstuvwxyz"

#Codificación
def vigenereCod(texto, palabra):
    print("*vigenereCod*")
    resultado = ""
    clave = 0

    for letra in texto:
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

#Decodificación
def vigenereDec(texto, palabra):
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

    return resultado
    
    
    

