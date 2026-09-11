def pares():
    quantia = int(input('Digite a quantidade de pares: '))
    numero = 1
    if quantia <= 0:
        print('Quantidade inválida. Digite um número maior que zero.')
    else:
        while numero <= quantia:
            print(numero * 2)
            numero += 1

def impares():
    quantia = int(input('Digite a quantidade de ímpares: '))
    numero = 1
    if quantia <= 0:
        print('Quantidade inválida. Digite um número maior que zero.')
    else:
        while numero <= quantia:
            print(numero * 2 - 1)
            numero += 1

def somatorio():
    quantia = int(input('Digite a quantidade de números para somar: '))
    soma = 0
    numero = 1
    if quantia <= 0:
        print('Quantidade inválida. Digite um número maior que zero.')
    else:
        while numero <= quantia:
            soma += numero
            numero += 1
        print('O somatório é:', soma)

def fatorial():
    quantia = int(input('Digite a quantidade de numeros para multiplicar: '))
    numero = 1
    fatorial = 1
    if quantia <= 0:
        print ('Quantidade inválida. Digite um número maior que zero.')
    else:
        while numero <= quantia:
            fatorial *= numero
            numero += 1
        print('O fatorial é:', fatorial)

def somar():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print (num1, '+', num2, '=', num1 + num2)

def subtracao():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print (num1, '-', num2, '=', num1 - num2)

def multiplicacao():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print (num1, 'x', num2, '=', num1 * num2)

def divisao():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print (num1, '/', num2, '=', num1 / num2)

while True:
    print ('Calculadora')
    print ('1 - Adição')
    print ('2 - Subtração')
    print ('3 - Multiplicação')
    print ('4 - Divisão')
    print ('5 - Pares')
    print ('6 - Impares')
    print ('7 - Somatorio')
    print ('8 - Fatorial')
    print ('0 - Sair')

    opcao = input('Escolha uma opção (1/2/3/4/5/6/7/8/0): ')

    if opcao == '1':
        somar()

    elif opcao == '2':
        subtracao()

    elif opcao == '3':
        multiplicacao()

    elif opcao == '4':
        divisao()

    elif opcao == '5':
        pares()

    elif opcao == '6':
        impares()
    elif opcao == '7':
        somatorio()

    elif opcao == '8':
        fatorial()

    elif opcao == '0':
        print('Fechando o programa...')
        break
    else:
        print('Opção inválida. Tente novamente.')