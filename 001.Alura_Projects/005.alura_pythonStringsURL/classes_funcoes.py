import re
class URL_ADD:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        print("Essa é a url: ", url)
        pass
#Sanitização da URL
#Ou poderia utilizar a função strip. Que remove os espaços em branco de strings.
    def sanitiza_url(self, url):
        self.url = url.replace(" ", "")
        return url

    def valida_url(self):
        if self.url == "":
            raise ValueError("Erro relacionado a URL de entrada. Ela está vazia.")
        #Segue forma de verificar o modelo da string de link que será analisada.
        padrao_rengex = re.compile('(http(s)?://)?(www.)?linkedin.com')
        padrao_rengex.match(self.url)
        teste = padrao_rengex.match(self.url)
        print(teste)
        if not teste:
            raise ValueError("A URL não é valida")

    def __len__(self):
        return len(self.url)

    def get_url_base(self):
        url_quebra = self.url.find("in/")
        url_base = self.url[0:url_quebra]
        print("\nURL base:", url_base, f"\nQtd. Char: {len(url_base)}")
        return url_base

    def url_parametros(self):
        url_quebra = self.url.find("in/")
        url_parametros = self.url[url_quebra:len(self.url)]
        print("\nURL Parametros:", url_parametros, f"\nQtd. Char: {len(url_parametros)}")
        return url_parametros

    def get_nome_usuario(self, url_parametros):
        #nome do usuario
        indice_inicial_usuario = url_parametros.find("in/")
        indice_final_usuario = url_parametros.find("-b")
        # find("string", "após")
        nome_usuario = url_parametros.find("alvaro-pereira", indice_inicial_usuario)

        if nome_usuario == -1:
            print("Este link não é de um usuário...")
        else:
            valor = url_parametros[nome_usuario:indice_final_usuario]
            print("\nNome do usuário:", valor, f"\nQtd. Char: {len(valor)}")

    