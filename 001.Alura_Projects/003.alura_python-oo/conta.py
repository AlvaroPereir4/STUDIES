# Para tornar um atributo privado, é necessario colocar 2 undercore antes da definição: self.__saldo

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O SALDO da conta de {} é: {}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel
        

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("Valor Invalido! O valor de {} ultrapassou o limite estabelecido.".format(valor))


# self acaba fazendo o papel de conta de origem.
    def tranfere(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)

# funcoes que retornam apenas os valores, sem nenhum tipo de string complementar:
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
# funcao para definir limite:
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
# criacao de metodo estatico
    @staticmethod
    def codigo_banco():
        return {"bb":"001", 'caixa':'104', 'bradesco':'237'}

    pass

