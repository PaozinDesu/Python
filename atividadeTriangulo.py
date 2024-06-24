def menu():
    print("Insira o primeiro lado do triângulo")
    num1 = int(input())
    print("Insira o segundo lado do triângulo")
    num2 = int(input())
    print("Insira o terceiro lado do triângulo")
    num3 = int(input())

    resultado = calculadora(num1, num2, num3)
    print("O resultado é:", resultado)


def calculadora (num1, num2, num3):
    if( num1, num2, num3 < 0):
        print("Essa opção não existe")
        menu()
    else:
        if(num1 == num2 and num2 == num3):
            return "O triângulo é equilatero"
        elif (num1 == num2 or num1 == num3 or num2 == num3):
            return "O triângulo é isósceles"
        else:
            return "O triângulo é escaleno"
        
menu()