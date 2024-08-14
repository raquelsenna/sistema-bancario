from abc import ABC


class Conta:
  def __init__(self, numero, cliente):
    self.__saldo = 0.0
    self.__numero = numero
    self.__agencia = "0001" #valor fixo
    self.__cliente = cliente
    self.__historico = Historico()

  @classmethod
  def nova_conta(cls, cliente, numero:int):
    return cls(cliente, numero)
  
  @property
  def saldo(self):
    return self.__saldo

  @property
  def numero(self):
    return self.__numero
  
  @property
  def agencia(self):
    return self.__agencia
  
  @property
  def cliente(self):
    return self.__cliente
  
  @property
  def historico(self):
    return self.__historico

  def sacar(self, valor):
    saldo = self.saldo
    excedeu_saldo = valor > saldo 

    if excedeu_saldo:
      print("Operação inválida! Falta de saldo para o saque.")
      
    elif valor > 0:
      self.saldo -= valor
      print("Saque realizado com sucesso!") 
      return True
    
    else:
      print("Operação inválida!.")

    return False

  def depositar(self, valor):
    if valor > 0:
      self.saldo += valor
      print("Depósito realizado com sucesso!")
      return True
    
    else:
      print("Operação inválida, tente novamente!")
      return False
    

class ContaCorrente(Conta):
  def __init__(self, cliente, numero, limite=500.00, limite_saques=3):
    super().__init__(numero, cliente)
    self.limite = limite
    self.limite_saques = limite_saques 

  def sacar(self, valor):
    numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

    excedeu_limite = valor > self.__limite
    excedeu_saques = numero_saques > self.limite_saques

    if excedeu_limite:
      print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
      print("Operação falhou! Número de saques diário ultrapassado.")

    else:
      return super().sacar(valor)
    
    return False
  
  def __str__(self):
    return f"""\
        Agência:\t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
     """


class Cliente:#armazena informações do cliente
  def __init__(self, endereco):
    self.endereco = endereco
    self.contas = []

  def realizar_transacao(self, conta, transacao):
    transacao.registrar(conta)

  def adicionar_conta(self, conta):
    self.contas.append(conta)


class PessoaFisica(Cliente):
  def __init__(self, cpf:str, nome:str, data_nascimento, endereco):
    super().__init__(endereco)
    self.__cpf = cpf
    self.__nome = nome
    self.__data_nascimento = data_nascimento


class Historico:#Armazena transações da conta
  def __init__(self):
    self.transacoes = []

  def adicionar_transacao(self, transacao):
    self.transacao.append(
      {
        "Tipo": transacao.__class__.__name__,
        "Valor": transacao.valor
      }
    )


class Transacao(ABC):
  @property
  def valor(self):
    pass

  @classmethod
  def registrar(self, conta):
    pass


class Saque(Transacao):
  def __init__(self, valor):
    self.valor = valor

  @property
  def valor(self):
    return self.valor
  
  def registrar(self, conta):
    sucesso_transação = conta.sacar(self.valor)

    if sucesso_transação:
      conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
  def __init__(self,valor):
    return self.valor
  
  def registrar(self, conta):
    sucesso_transacao = conta.depositar(self.valor)

    if sucesso_transacao:
      conta.historico.adicionar_transacao(self)
 