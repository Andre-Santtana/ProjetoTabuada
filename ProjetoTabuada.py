def tabuadaSoma():
    numMax = int(input("\nInforne a quantidade de linhas da tabuada: "))
    numTab = int(input("Informe qual o nunero que quer gerar a tabuada: "))

    for i in range(numMax):
        print(f"{i} + {numTab} = {i + numTab}")

def tabuadaSub():
    numMax = int(input("\nInforne a quantidade de linhas da tabuada: "))
    numTab = int(input("Informe qual o nunero que quer gerar a tabuada: "))

    for i in range(numMax):
        print(f"{i} - {numTab} = {i - numTab}")

def tabuadaMultip():
    numMax = int(input("\nInforne a quantidade de linhas da tabuada: "))
    numTab = int(input("Informe qual o nunero que quer gerar a tabuada: "))

    for i in range(numMax):
        print(f"{i} * {numTab} = {i * numTab}")

def tabuadaDiv():
    numMax = int(input("\nInforne a quantidade de linhas da tabuada: "))
    numTab = int(input("Informe qual o nunero que quer gerar a tabuada: "))

    for i in range(numMax):
        print(f"{i} / {numTab} = %1.2f" %(i / numTab))


print("=============")
print("=  TABUADA  =")
print("=============")

print("\nEsse programa gera as seguintes tabuadas: Adição, Subtração, Multiplicação e Divisão \n\n")

#adicionar uma função aqui para a opção valida
print("1-Adição \n2-Subtracao \n3-Multiplicacao \n4-Divisao \n0-Sair ")

opc_escolhida = int(input("\nEscolha a opção desejada da tabuada: "))

if opc_escolhida:
    if opc_escolhida == 1:
        tabuadaSoma()

    if opc_escolhida == 2:
        tabuadaSub()

    if opc_escolhida == 3:
        tabuadaMultip()

    if opc_escolhida == 4:
        tabuadaDiv()

    if opc_escolhida == 0:
        print("Até Mais")

    else:
        print("Digite uma opção valida")
