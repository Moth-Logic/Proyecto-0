alfabeto = "abcdefghijklmnñopqrstuvwxyz"

def monoalfabeticoCod(texto, clave):
    """Codifica con cifrado moalfabético con la palabra clave brindada.
    Entradas: Clave, texto
    Salidas: texto codificado
    Restrincciones: La clave no puede ser vacia"""
    print("*monoalfabeticoCod*")
    sinRepetir = ""

    for letra in clave.lower():
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

    return mensajeCifrado

mensaje= input("Ingrese el texto a codificar ")
claveUsada= input("Ingrese la clave a usar ")

print(monoalfabeticoCod(mensaje, claveUsada))
        
        
def monoalfabeticoDec(texto, clave):
    """Decodifica el texto con clave en monoalfabetico.
    Entradas: Clave, texto
    Salidas: texto decodificado
    Restrincciones: La clave no puede ser vacia"""
    print("*monoalfabeticoDec*")

    sinRepetir=""
    for letra in clave.lower():
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

    return mensajeDescifrado


mensaje= input("Ingrese el texto a decodificar ")
claveUsada= input("Ingrese la clave a usar ")

print(monoalfabeticoDec(mensaje, claveUsada))

      

      
    
    
            
    
    

    
