from conta import Conta
from cliente import Cliente
    
conta1 = Conta(1, "Alvaro", 200, 300)
conta2 = Conta(2, "Leticia", 250, 500)

# a seguir, demonstracao de uso de um atributo privado:
print("\nO titular desta conta é {} e possui o limite de {}\n".format(conta1._Conta__titular, conta1._Conta__limite))

conta1.extrato() # É desta maneira que se chama um metodo criado. Metodo de exibir extrato da conta.

# teste de metodos de deposito e saque.
# print("apos deposito")

conta1.deposita(100)
print("\nApós deposito:")
conta1.extrato()

conta1.sacar(200)
print("\nApós saque:")
conta1.extrato()

## Transferencia entre duas contas:
print("\nHouve uma transferencia entre contas, agora o salto atual da conta1 e conta2 são:\n\n")
conta1.tranfere(50, conta2)
conta1.extrato()
conta2.extrato()

print(conta1.saldo)

print("Antigo limte!", conta1.limite)
conta1.limite = 100
print("Novo limite! ",conta1.limite)

# teste do da classe cliente:

cliente = Cliente("Alvaro2")
cliente.nome = "Joao"
print(cliente.nome)

# teste do setter limite:
conta2.limite = 1000
print(conta2.limite)

# teste de metodos de controle de saque
conta1.sacar(2000)

# teste de metodo estatico + lista de codigo dos bancos
codigos = Conta.codigo_banco()
print(codigos['bb'])
