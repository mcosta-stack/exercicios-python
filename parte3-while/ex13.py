contador = input("Digite sua senha: ")

while contador != "senha123":
    print("Senha incorreta. Tente novamente.")
    contador = input("Digite sua senha: ")
print("Senha correta!")