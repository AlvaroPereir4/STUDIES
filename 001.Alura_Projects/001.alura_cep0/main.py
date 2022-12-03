# Programa que busca o CEP em um grupo de informações, relacionadas a um endereço.
import re
# import re --> Regular Expressions/RegEx
endereco = "Rua: Rua Beto, Numero: 101, Complemente: Casa 2, Bairro: Jardim Presidente Dutra, Cidade: Guarulhos, Estado: SP, CEP:07171-260"
# O colchetes após os quadrantes, demonstra quantas vezes serão adicionadas informações.
padrao_cep = re.compile("[0-9]{5}[-]{0, 1}[0-9]{3}")
busca = padrao_cep.search(endereco) # Search é uma função de busca
if busca:
    cep = busca.group()
    print(cep)
