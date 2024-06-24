def menu():
    print("Insira o primeiro numero")
    num1 = int(input())
    print("Insira o segundo número")
    num2 = int(input())

    print("Insira o tipo da operação")
    print("1 = Soma")
    print("2 = Subtração")
    print("3 = Divisão")
    print("4 = Multiplicação")
    print("0 = Sair")
    operacao = int(input())
    resultado = calculadora(num1, num2, operacao)
    print("O resultado é:", resultado)


def calculadora (num1, num2,operacao):
    if( operacao > 4 or operacao < 0):
        print("Essa opção não existe")
        menu()
    else:
        if(operacao == 1):
            return num1 + num2
        elif (operacao == 2):
            return num1 - num2
        elif (operacao == 3):
            return num1 / num2
        elif (operacao == 4):
            return num1 * num2
        elif (operacao == 0):
            exit()
        else:
            return 0
    
menu()