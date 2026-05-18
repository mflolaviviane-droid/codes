#Programa Calculadora
while True:

    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 + num2

        print("Resultado:", resultado)

    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 - num2

        print("Resultado:", resultado)

    elif opcao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 * num2

        print("Resultado:", resultado)

    elif opcao == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Não existe divisão por zero!")

    elif opcao == 5:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")

    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 + num2

        print("Resultado:", resultado)

    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 - num2

        print("Resultado:", resultado)

    elif opcao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 * num2

        print("Resultado:", resultado)

    elif opcao == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Não existe divisão por zero!")

    elif opcao == 5:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")
