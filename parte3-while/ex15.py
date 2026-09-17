while True:
    numero = int(input("Digite um número (0 para sair): "))
    contador_positivos = 0

    if numero == 0:
        break
    elif numero > 0:
        contador_positivos = contador_positivos + 1

print("Quantidade de números positivos digitados: ", contador_positivos)
