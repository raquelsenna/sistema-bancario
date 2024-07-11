def menu():
  print('''
-----------------
  [1] Depósito
  [2] Saque
  [3] Criar Usuário
  [4] Criar Conta
  [5] Listar Contas
  [6] Extrato
  [7] Sair
 ''')
  return int(input("-> "))


def deposito(valor, saldo, extrato, /): 
  
  if valor > 0:
    saldo += valor
    extrato += f'Depósito: R${valor:.2f}\n'
    print('Depósito realizado com sucesso!')

  else: 
    print('\nValor do depósito inválido.')
  
  return saldo, extrato


def saque(*, valor, saldo, extrato, limite, limite_saque, contador_limite):
  if saldo >= valor:

    if valor <= limite:
        
      if limite_saque > contador_limite:
        saldo -= valor
        extrato += f'Saque: R${valor:.2f}\n'
        contador_limite += 1
        print('Saque realizado com sucesso!')

      else:
        print('\nOperação inválida! Limite total de saques diários ultrapassado.')
        
    else:
      print('\nOperação inválida! Limite ultrapassado.')

  else:
    print('Operação inválida! Saldo insulficiente..')

  return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):

  print('-----------EXTRATO----------\n')
  print('Não houve movimentações' if not extrato else extrato)
  print(f'\nSaldo: R${saldo:.2f}\n')
  print('----------------------------')


def criar_usuario(usuarios):
  cpf = int(input('Informe seu cpf: '))
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
      print("\n@@@ Já existe usuário com esse CPF! @@@")
      return

  nome = (input('Informe seu nome completo: '))
  data_nasci = (input('Informe sua data de nascimento (dd-mm-aaaa): '))
  endereco = (input('Informe seu endereço (logradouro, número - bairro - cidade/sigla): '))

  usuarios.append({'nome':nome, 'cpf':cpf, 'data_nasci':data_nasci, 'endereco':endereco})

  print('Usuário cadastrado com sucesso!')


def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None 


def criar_conta(agencia, numero_conta, usuarios):
  cpf = input('Informe o CPF do usuário: ')
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
      print('\nConta criada com sucesso!')
      return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

  print('\nUsuário não encontrado, fluxo de criação de conta encerrado!')


def listar_contas(contas):
  for conta in contas:
    linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
    """
    print('-' * 100)


def main():
  LIMITE_SAQUE = 3
  AGENCIA = '0001'

  saldo = 0
  extrato = ''
  limite = 500
  contador_limite = 0
  usuarios = []
  contas = []

  while True:
    opcao = menu()
    
    if opcao == 1:
      valor = float(input('Valor do Depósito: R$'))
      
      saldo, extrato = deposito(valor, saldo, extrato)

    elif opcao == 2:
      valor = float(input('\nValor do saque: R$'))

      saldo, extrato = saque(
        valor=valor,
        saldo=saldo,
        extrato=extrato,
        limite=limite,
        limite_saque=LIMITE_SAQUE,
        contador_limite=contador_limite,
      )
    
    elif opcao == 3:
      criar_usuario(usuarios)

    elif opcao == 4:
      numero_conta = len(contas) + 1
      conta = criar_conta(AGENCIA, numero_conta, usuarios)

      if conta:
        contas.append(conta)

    elif opcao == 5:
      listar_contas(contas)
      
    elif opcao == 6:
      exibir_extrato(saldo, extrato=extrato)

    elif opcao == 7:
      print('Operação Finalizada!')
      break


main()