def menu():
    menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Usuário
[5] Sair


=>  """
    return input(menu)


def deposito(saldo, valor, extrato, /):

    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print('Depósito realizado com sucesso!')

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques): 

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print('Saque realizado com suceso!')

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(nome, nascimento, cpf, endereco):
    return CPF, endereco


def main():

    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    criar_usuário = []

    while True:

        opcao = menu()

        if opcao == "1":

            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)
            
        elif opcao == "2":
        
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques, 
            limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            nome = input('Nome: ')
            CPF = input('CPF: ')
            endereco = input('endereco: ')


        elif opcao == "5":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()