# Descifrado Rail Fence

# Pedimos el texto cifrado
texto = input("Ingrese el mensaje cifrado: ")

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