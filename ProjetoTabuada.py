def tabuadaSoma():
    numMax = int(input("Inforne a quantidade de linhas da tabuada: "))
    numTab = int(input("Informe qual o nunero que quer gerar a tabuada: "))

    for i in range(numMax):
        print(f"{i} + {numTab} = {i + numTab}")





print("=============")
print("=  TABUADA  =")
print("=============")

print("\nEsse programa gera as seguintes tabuadas: Adição, Subtração, Multiplicação e Divisão \n\n")

print("1-Adição \n2-Subtracao \n3-Multiplicacao \n4-Divisao ")

opc_escolhida = int(input("\nEscolha a opção desejada da tabuada: "))

if opc_escolhida:
    if opc_escolhida == 1:
        tabuadaSoma()

    if opc_escolhida == 2:
        tabuadaSub()

    if opc_escolhida == 3:
        tabuadaSoma()

    if opc_escolhida == 4:
        tabuadaSoma()

    if opc_escolhida == 0:
        print("Exite")

    else:
        print("Digite uma opção valida")
