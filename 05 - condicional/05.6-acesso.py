# solicitando informções de acesso ao usuário
email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

# verificando se o email está cadastrado
if email == "teste@teste.com.br":
    print("email correto")
else:
    print("usuário não cadastrado")
    
# verificando se a senha está correta
if senha == "123456":
    print("Bem Vindo ao sitema da Fábrica")
else:
    print("Senha Incorreta")