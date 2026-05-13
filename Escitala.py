import math

#Codificación
def escitalaCod(texto, lineas):

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

    return resultado
    print(resultado)

#Decodificación
def escitalaDec(texto, lineas):

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
    

