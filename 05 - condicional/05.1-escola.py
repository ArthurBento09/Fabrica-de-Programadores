# criando variáveis
nome = input("Digite o nome do aluno:")
n1 = float(input("Digite a 1ª nota do aluno:"))
n2 = float(input("Digite a 2ª nota do aluno:"))
n3 = float(input("Digite a 3ª nota do aluno:"))
media = (n1 + n2 + n3) / 3

# verificando média
if media >= 7:
    print("Aprovado!")
elif media >= 4:
    print("Em recuperação")
else:
    print("Reprovado")
