class Animais:
    def __init__(self, nome, classe, idade, sexo):
        self.nome = nome
        self._classe = classe
        self.idade = idade
        self.sexo = sexo

    @property
    def nome_animal(self):
        """
        Método que modifica o nome da pessoa.
        """
        return self.nome

    @nome_animal.setter
    def nome_animal(self, nome):
        """
        Método que modifica o nome do animal.
        """
        self.nome = nome

    @property
    def classe_animal(self):
        """
        Método que modifica o nome da pessoa.
        """
        return self._classe

    @classe_animal.setter
    def classe_animal(self, classe):
        """
        Método que modifica o nome do animal.
        """
        self._classe = classe

    @property
    def idade_animal(self):
        """
        Método que modifica o nome da pessoa.
        """
        return self.idade

    @idade_animal.setter
    def idade_animal(self, idade):
        """
        Método que modifica o nome do animal.
        """
        self.idade = idade

    @property
    def sexo_animal(self):
        """
        Método que modifica o nome da pessoa.
        """
        return self.sexo

    @sexo_animal.setter
    def sexo_animal(self, sexo):
        """
        Método que modifica o nome do animal.
        """
        self.sexo = sexo
