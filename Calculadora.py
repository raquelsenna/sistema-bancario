from estudos import Ven

#TESTE DE LÓGICA DA CALCULADORA NO TERMINAL

def somar(n1, n2, operacoes):
  resp = n1 + n2
  operacoes += f'{resp}\n'
  print(f'{n1} + {n2} = {resp}')
  return operacoes

def subtrair(n1, n2, operacoes):
  resp = n1 - n2
  operacoes += f'{resp}\n'
  print(f'{n1} - {n2} = {resp}')
  return operacoes

def multiplicar(n1, n2, operacoes):
  resp = n1 * n2
  operacoes += f'{resp}\n'
  print(f'{n1} * {n2} = {resp}')
  return operacoes

def dividir(n1, n2, operacoes):
  resp = n1 / n2
  operacoes += f'{resp}\n'
  print(f'{n1} / {n2} = {resp}')
  return operacoes

def armazenar(*, operacoes):
  print('Histórico de Operações')
  print(operacoes)
  

def main():
  while True:

    num1 = 0
    num2 = 0
    operacao = ''
    oper_totais = ''

    num1 = float(input('N1 -> '))
    operacao = input('Qual operação? (+, -, * ou /) -> ')
    num2 = float(input('N2 -> '))

    if operacao == '+':
      som = somar(num1, num2, oper_totais)
      print(som)

    elif operacao == '-':
      sub = subtrair(num1, num2)
      print(sub)  

    elif operacao == '*':
      mult = multiplicar(num1, num2)  
      print(mult)

    elif operacao == '/':
      div = dividir(num1, num2) 
      print(div) 

    resp = input('Ver operações? [s] [n] ')
    
    if resp == 's':
      hist = armazenar(
        operacoes=oper_totais
      )
      print(hist)

main()