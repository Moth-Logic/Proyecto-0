texto = input("Texto: ")
clave = input("Clave: ")

alfabeto = list("abcdefghijklmnñopqrstuvwxyz")
    extras = list("123")

    claveunica = []
    for letra in clave:
        if letra not in claveunica:
            claveunica.append(letra)
    print(claveunica)

    for letra in alfabeto:
        if letra not in claveunica:
            claveunica.append(letra)
    print(claveunica)

    claveunica = claveunica + extras
    print(claveunica)

    matriz = []
    for i in range(6):
        fila = claveunica[i*5:(i+1)*5]
        matriz.append(fila)
    print(matriz)

    contador = 0

    for letra in texto:
        while contador < (len(texto)):
            print(texto[contador-(len(texto)+1)])
            contador += 1

    mensaje = input("Pon tu mensaje: ")
    mensaje2 = ""

    for i in range(len(mensaje)):
        if i < len(mensaje) - 1 and mensaje[i] == mensaje[i + 1]:
            mensaje2 += mensaje[i] + "1"
        else:
            mensaje2 += mensaje[i]
    print(mensaje2)
