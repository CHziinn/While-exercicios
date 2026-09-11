nome = input("Digite seu nome: ")
nome_cadastrado = nome
senha_digitada = input("Digite sua senha: ") 
senha_cadastrado = input("Confirme sua senha: ")
tentativas = 2

while senha_digitada != senha_cadastrado or nome_cadastrado != nome:
    print("A esta senha ou nome esta incorreto. Tente novamente.")
    senha_digitada = input("Digite sua senha: ")
    if tentativas == 0:
        print("Número máximo de tentativas atingido. Acesso negado.")
        break
    tentativas -= 1

print("Senha correta! Bem-vindo,", nome)