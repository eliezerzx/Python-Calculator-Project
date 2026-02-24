# Modulo math para Raiz quadrada
import math

# menu da Calculadora
while True:
    print("===== Calculadora Python ====")
    print("\n1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Potencia")
    print("6 - Raiz quadrada")
    print("7 - Porcentagem")
    print("0 - Sair")
    opcao = int (input("Escolha uma das opcoes:"))

    # Menu/Conta das somas
    if opcao == 1:
        numeroSoma1 = float (input("Digite o primeiro numero:"))
        numeroSoma2 = float (input("Digite o segundo nuemro:"))
        resultadoSoma = (numeroSoma1 + numeroSoma2)
        print("\n======================================================")
        print(f"           CONTA: \n| {numeroSoma1:.2f} + {numeroSoma2:.2f} = {resultadoSoma:.2f} |")
        print("======================================================")

    elif opcao == 2:
        numeroSub1 = float (input("Digite o primeiro numero:"))
        numeroSub2 = float (input("Digite o segundo nuemro:"))
        resultadoSub = (numeroSub1 - numeroSub2)
        print("\n======================================================")
        print(f"           CONTA: \n| {numeroSub1:.2f} - {numeroSub2:.2f} = {resultadoSub:.2f} |")
        print("======================================================")

    elif opcao == 3:
        numeroMult1 = float (input("Digite o primeiro numero:"))
        numeroMult2 = float (input("Digite o segundo nuemro:"))
        resultadoMult = (numeroMult1 * numeroMult2)
        print("\n======================================================")
        print(f"           CONTA: \n| {numeroMult1:.2f} * {numeroMult2:.2f} = {resultadoMult:.2f} |")
        print("======================================================")

    elif opcao == 4:
        numeroDiv1 = float(input("Digite o primeiro numero: "))
        numeroDiv2 = float(input("Digite o segundo numero: "))

        if numeroDiv2 == 0:
            print("Erro: Divisão por zero não permitida!")
        else:
            resultadoDiv = numeroDiv1 / numeroDiv2
            print("\n======================================================")
            print(f"           CONTA: \n| {numeroDiv1:.2f} / {numeroDiv2:.2f} = {resultadoDiv:.2f} |")
            print("======================================================")
    
    elif opcao == 5:
        numeroPot1 = float (input("Digite o primeiro numero:"))
        numeroPot2 = float (input("Digite o segundo nuemro:"))
        resultadoPot = (numeroPot1 ** numeroPot2)
        print("\n======================================================")
        print(f"           CONTA: \n| {numeroPot1:.2f} ** {numeroPot2:.2f} = {resultadoPot:.2f} |")
        print("======================================================")

    elif opcao == 6:
        numeroRaiz = float(input("Digite o numero para calcular a raiz: "))

        if numeroRaiz < 0:
            print("Erro: Não existe raiz real de número negativo!")
        else:
            resultadoRaiz = math.sqrt(numeroRaiz)

            print("\n======================================================")
            print(f"           CONTA:")
            print(f"| √{numeroRaiz:.2f} = {resultadoRaiz:.2f} |")
            print("======================================================")

    elif opcao == 7:
        numeroPorc1 = float (input("Digite o primeiro numero:"))
        numeroPorc2 = float (input("Digite o segundo nuemro:"))
        resultadoPorc = (numeroPorc1 * numeroPorc2 ) / 100
        print("\n======================================================")
        print(f"           CONTA: \n| {numeroPorc1:.2f} % {numeroPorc2:.2f} = {resultadoPorc:.2f} |")
        print("======================================================")
    
    elif opcao == 0:
        break
    else:
        print ("!------!------!")
        print("valor invalido")
        print ("!------!------!")