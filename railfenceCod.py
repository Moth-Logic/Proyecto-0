"""Railfence Codificado"""

# Pedimos el texto al usuario
texto = input("Ingrese el mensaje: ")

# Siempre van a ser 3 rieles lmao
rieles = 3

# Creamos una lista vacía para guardar cada riel
# como son 3 rieles: ["", "", ""]
lista_rieles = []
for i in range(rieles):
    lista_rieles.append("")

print(lista_rieles)

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