import requests

cep_requisitado = str(input("Digite um CEP: "))

url = "https://viacep.com.br/ws/{}/json/".format(cep_requisitado)

r = requests.get(url)
print(r.text)
#filtro utilizando o json.
print("O nome da sua rua é: ", r.json()['logradouro'])
