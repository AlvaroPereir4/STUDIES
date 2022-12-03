from re import X


url = "aoaooaoa"
print(url)

url = url.replace("a", "e")
print("\nnova url:", url)

url = https://www.linkedin.com/in/alvaro-pereira-b5b2a8227/
padrao_rengex = re.compile('(http(s)?://)?(www.)?linkedin.com')
padrao_rengex.match(url)
print(padrao_rengex.match(url))
