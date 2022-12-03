class Cliente:
    def __init__(self, nome):
        self.nome = nome
    
# Colocar "@property" faz com que não seja nacessario a especifidade do () no final da utilização do metodo.
    @property
    def nome(self):
        return self.__nome.title()
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        return nome

        pass