# Variáveis
op = 1
operacao = []
valor = []
saldo = 0 
saques = 3

while(op != '0'):
    print("===================")
    print("[1] - Depósito")
    print("[2] - Saque ")
    print("[3] - Extrato ")
    print("[0] - Sair")
    print("====================")
    op = input()

    if(op == '1'):

        v = int(input("Quanto deseja depositar? "))
        
        if(v <= 0):
            print("Valor inválido... ")
        else:
            print("Depósito efetuado... ")
            saldo = saldo + v
            operacao.append('1')
            valor.append(v)

    elif(op == '2'):

        if(saques == 0):
            print("Número de saques excedido... ")

        else:

            v = int(input("Quanto deseja sacar? "))

            if((v > 0 and v <= 500) and saldo >= v):
                print("Saque efetuado... ")
                saldo = saldo - v
                operacao.append('2')
                valor.append(v)
                saques = saques - 1
            else:
                print("Saque não efetuado... ")

    elif(op == '3'):

        for i in range(0,len(operacao)):
            if(operacao[i] == '1'):
                print("Depósito: R$"+str(valor[i]))
            else:
                print("Saque: R$"+str(valor[i]))
        print("")
        print("Saldo: R$"+str(saldo))

    elif(op == '0'):
        print("Finalizando...")

    else: 
        print("Opção inválida...")    