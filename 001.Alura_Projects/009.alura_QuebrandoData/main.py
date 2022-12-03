data = str(input("Digite uma data de aniversário: "))
data_quabrada = data.split("/")
dia_nascimento = data_quabrada[0]
mes_nascimento = data_quabrada[1]
ano_nascimento = data_quabrada[2]
ano_atual = 2022



print("Este é a idade da pessoa:",(ano_atual - int(ano_nascimento)))
print("Esse é o dia de nascimento: ", dia_nascimento)
print("Esse é o mes de nascimento: ", mes_nascimento)

