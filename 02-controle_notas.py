nome = input("Digite seu nome: ")
resposta = ['s', 'n']
notas = []
contador = 0

while True:
    nota = float(input("Digite sua nota: "))
    notas.append(nota)

    print ("deseja digitar outra nota? (s/n)")
    contador += 1
    resposta = input().lower()

    if resposta == "n":
        nota_final = sum(notas) / contador
        print (f"{nome} Sua média final é: {nota_final}")
        break