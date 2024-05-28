menu = """
=============== MENU ===============
      
      [0] Sacar
      [1] Depositar
      [2] Consultar Saldo
      [3] Extrato
      [4] Sair

====================================
=> """

saldoAtual = 0
limite = 300
numero_de_saques = 0
LIMITE_SAQUE = 3    
movimentacoes = ""

while True:

    opcao = input(menu)

    if opcao == "0":
        valorSaque = float(input("Digite o valor do saque: "))
        exedeSaldo = valorSaque > saldoAtual
        exedeLimite = valorSaque > limite
        exedeSaque = numero_de_saques >= LIMITE_SAQUE

        if exedeSaldo:
            print("Falha na operção, voce não tem saldo suficiente.")
        elif exedeLimite:
            print("Falha na operação, valor acima do limite diário.")
        elif exedeSaque:
            print("Falha na operação, voce atingiu o limite de saques diário.")   
        elif valorSaque > 0:
            saldoAtual -= valorSaque
            movimentacoes += f"Saque: R$ {valorSaque:.2F}\n"
            print(f"Saque no valor de: R$ {valorSaque:.2f} realizado com sucesso !")
            numero_de_saques += 1
            print("")
            print(f"Voce tem mais [{LIMITE_SAQUE - numero_de_saques}] saques restantes")
        else:
            print("Falha na operação, o valor informado é inválido. !")

    elif opcao == "1":
        valorDeposito = float(input("Digite o valor do depósito :"))
        if valorDeposito > 0:
            saldoAtual +=valorDeposito
            movimentacoes += f"Deposito: R$ {valorDeposito:.2f}\n"
        else:
            print("Falha na operação, o valor digitado está abaixo do mínimo permitido. !")

    elif opcao == "2":
        print(f"""
    =============== SALDO ===============
              
        Olá seja bem vindo!
        Seu saldo atual é:
              R$ {saldoAtual:.2f}

    ======================================
""")

    elif opcao == "3":
        print("\n============== EXTRATO ==============")
        print("Não foram realizadas movimentações. " if not movimentacoes else movimentacoes)
        print(f"\n Saldo: {saldoAtual:.2f}")
        print("=====================================")

    elif opcao == "4":
        break
    else:
        print("Operação inválida, por favor selecione uma das opções abaixo.")