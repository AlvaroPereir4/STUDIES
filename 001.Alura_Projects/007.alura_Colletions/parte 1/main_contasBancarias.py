from abc import ABCMeta, abstractclassmethod 

class Conta(metaclass=ABCMeta): # Objeto construtor de conta corrente. 
    def __init__(self, codigo): # Definição de parametros, codigo da conta.
        self._codigo = codigo
        self._saldo = 500 # saldo inicial, para testes
    def deposita(self, valor): # Definição de parametros, valor do deposito.
        self._saldo += valor
    def __eq__(self, outro):
        if type(outro) != Conta:
            return False
    @abstractclassmethod
    def passaMes(self):
        pass
    def __str__(self): # Return do valor.
        return "[>> Codigo {} Saldo {} <<]".format(self._codigo, self._saldo)

class ContaCorrente(Conta):
    def passaMes(self):
        self._saldo -= 2 #tarifa mensal do banco

class ContaPoupanca(Conta):
    def passaMes(self):
        self._saldo *= 1.01
        self._saldo -= 3


contaCorrenteTeste = ContaCorrente(1)
#contaCorrenteTeste.passaMes()
#print("Exemplo, conta corrente:\n", contaCorrenteTeste)

contaPoupancaTeste = ContaPoupanca(2)
#contaPoupancaTeste.passaMes()
#print("Exemplo, conta poupança:\n", contaPoupancaTeste)

contas = [contaCorrenteTeste, contaPoupancaTeste]
for conta in contas:
    conta.passaMes() # Uso de duck typing
    print(conta)