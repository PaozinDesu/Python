def calculadora (num1, num2,operacao):
    if(operacao == "Soma"):
        return num1 + num2
    elif (operacao == "Subtração"):
        return num1 - num2
    elif (operacao == "Divisão"):
        return num1 / num2
    elif (operacao == "Multiplicação"):
        return num1 * num2
    else:
        return 0
    
teste = calculadora(10, 20, "Divisão")
print(str(teste))