menu = '''
-----------------
  [1] Depósito
  [2] Saque
  [3] Extrato
  [4] Sair

-> '''

saldo = 0
extrato = ''
limite = 500
LIMITE_SAQUE = 3
contador_limite = 0

while True: 

  opcao = int(input(menu))

  if opcao == 1:
    valor_deposito = float(input('\nValor do depósito: R$'))

    if valor_deposito > 0:
      saldo += valor_deposito
      extrato += f'Depósito de R${valor_deposito:.2f}\n'
    else: 
      print('\nValor do depósito inválido.')

  elif opcao == 2:
    saque = float(input('\nValor do saque: R$'))

    if saldo >= saque:

      if saque <= limite:
        
        if LIMITE_SAQUE > contador_limite:
          saldo -= saque
          extrato += f'Saque de R${saque:.2f}\n'
          contador_limite += 1
        else:
          print('\nLimite total de saques diários ultrapassado.')
        
      else:
        print('\nOperação inválida! Limite ultrapassado.')

    else:
      print('Não é possóvel sacar o valor por falta de saldo.')
  
  elif opcao == 3:
    if extrato == '':
      print(f'''
-------------------------         
         EXTRATO
    
Não houve movimentações.
-------------------------
      ''')
    
    else:
      print(f'''
---------------------          
       EXTRATO
    
{extrato}
---------------------
      ''')
    
  elif opcao == 4:
    print('Operação Finalizada!')
    break

      


  
  

