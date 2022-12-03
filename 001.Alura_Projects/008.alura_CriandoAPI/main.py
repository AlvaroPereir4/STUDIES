#criando API no python - uso da biblioteca requests.
import requests
from base import BuscaEndereco
cep = str(input("Digite o CEP: "))
busca = BuscaEndereco(cep)
info = busca.info_total()
print(info)

dados = busca.info_especificas()
print(dados)