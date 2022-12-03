class ContaEsp:

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        pass


# Como é padrão deixar o limite em 1000.0, quando for criar novo objeto não precisa definir. 
# Apenas se o limite for diferente, é apenas especificar o limite que ele adiciona.