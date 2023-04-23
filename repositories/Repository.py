class Repository():
    """
    Classe que será utilizada como modelo para outros repositórios.
    """
    @staticmethod
    def create():
        """
        Deverá ser sobrescrito nas classes que herdarem de Repository.
        Recebe como parametro uma entidade (objeto intanciado de uma classe) e faz o cadastro dela no banco de dados.
        :return: vazio
        """
        pass

    @staticmethod
    def _read():
        """
        Deverá ser sobrescrito nas classes que herdarem de Repository.
        Método oculto, deve ser usado somente dentro da classe.
        Não recebe parametro. Realiza uma consulta no banco de dados, retornando uma lista de tuplas com os dados de cada
        registro da tabela.
        :return: Lista de Tuplas
        """
        pass

    @staticmethod
    def delete():
        """
        Deverá ser sobrescrito nas classes que herdarem de Repository.
        Recebe como parametro uma entidade (objeto intanciado de uma classe) e faz a remoção dela no banco de dados.
        :return: vazio
        """
        pass

    @staticmethod
    def update():
        """
        Deverá ser sobrescrito nas classes que herdarem de Repository.
        Recebe como parametro uma entidade (objeto intanciado de uma classe) e faz um update dela no banco de dados.
        :return:
        """
        pass

    @staticmethod
    def listar():
        """
        Deverá ser sobrescrito nas classes que herdarem de Repository.
        Não recebe parametro. Chama o método interno _read() e converto o retorno deste método em uma lista de objetos.
        :return: Lista de Objetos
        """
        pass

    @staticmethod
    def buscar():
        """
        Deverá ser sobrescrito nas classes que herdarem de Repository.
        Recebe como parametro uma informação (refetente a alguma coluna da tabela) e realiza uma busca no banco para
        encontrar um registro referente à aquela informação. Por fim, instancia um objeto com as informações coletadas
        e o retorna.
        :return: Objeto
        """
        pass
