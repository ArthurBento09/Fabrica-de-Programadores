# definindo e solicitando os valores das variáveis
altura = float(input("Digite sua Altura:"))
peso = float(input("Digite seu Peso: "))

# calculo do IMC
imc = peso / altura**2

# verificando se o IMC é >= 30 e exibindo a respectiva mensagem para o usuário 
if imc >= 30:
    print("Cuidado com a saúde!")
else:
    print("Tudo OK.")

# verificando o valor do IMC nas condições abaixo e mostrando a respectiva mensagem para o usuário
if imc <= 18.5: 
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso Normal")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade Grau I")
elif imc <= 39.9:
    print("Obesidade Grau II")
elif imc >= 40.0:
    print("Obesidade Mórbida")