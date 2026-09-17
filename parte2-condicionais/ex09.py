media = float(input("Digite a média do aluno: "))
if media >= 6:
    print("Aprovado")  
elif media < 6 and media >= 4: 
    print("Recuperação")
else:
    print("Reprovado")