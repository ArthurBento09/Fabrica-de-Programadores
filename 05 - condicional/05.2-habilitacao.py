# Criando as variáveis
nome = input("Qual é o seu nome?")
idade = int(input("Qual é sua idade?"))

# Verificando a condição da idade
if idade >= 18:
    carteira_motorista = input("Possui carteira de motorista?\n(1-sim / 2-não)")
    if carteira_motorista == "1":
        print("Pode dirigir")
    else:
        print("Não pode digirir")
else:
    print("Menor de idade")  