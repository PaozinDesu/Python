def perguntas():
    print("Insira seu nome:")
    nome = input()
    print("insira seu ano de nascimento:")
    anoNascimento = int(input())
    conferirIdade(anoNascimento, nome)
def conferirIdade(anoNascimento, nome):
    try:
        if (anoNascimento > 2022 or anoNascimento < 1922):
            print("Insira um data valida")
            perguntas()
        else:
            idade = 2024 - anoNascimento
            print(nome, "completa nesse ano", idade, "anos")
    except: 
        print("Dados inseridos de maneira incorreta")
perguntas()