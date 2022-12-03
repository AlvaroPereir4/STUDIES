class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title() # .title() no final faz com que a string comece com letra maiuscula. 
        self.ano = ano
        self._likes = 0
    @property
    def likes(self):
        return self._likes
    def DarLikes(self):
        self._likes += 1
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    def __str__(self):
        return "{} - Ano: {} - Likes: {}".format(self._nome, self.ano, self._likes)

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) #usa-se essa linha de codigo para chamar metodos de uma classe mãe. Se usa o init para ele se sobsescrever no que foi definido.
        self.duracao = duracao
        self._likes = 0
        self.info = print("Filme: {} - Ano: {} - Duração: {} - Likes: {}".format(self._nome, self.ano, self.duracao, self._likes))
    def __str__(self):
        return "{} - Ano: {} - Duração: {} - Likes: {}".format(self._nome, self.ano, self.duracao, self._likes)

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        self._likes = 0
        self.info = print("Serie: {} - Ano: {} - Temporadas: {} - Likes: {}".format(self._nome, self.ano, self.temporadas, self._likes))
    def __str__(self):
        return "{} - Ano: {} - Temporadas: {} - Likes: {}".format(self._nome, self.ano, self.temporadas, self._likes)

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)
