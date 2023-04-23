import mysql.connector
from repositories.Repository import *


class AnimaisRepository(Repository):
    @staticmethod
    def create(Animal):
        """
        Deverá ser sobrescrito nas classes que herdarem de Repository.
        Recebe como parametro uma entidade (objeto intanciado de uma classe) e faz o cadastro dela no banco de dados.
        :return: vazio
        """
        conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
        cursor = conexao.cursor()
        comando = f"INSERT INTO animais(ani_nome, ani_classe, ani_idade, ani_sexo) VALUES ('{Animal.nome_animal}', " \
                  f" '{Animal.classe_animal}', '{Animal.idade_animal}', '{Animal.sexo_animal}');"
        cursor.execute(comando)
        conexao.commit()
        conexao.close()

    @staticmethod
    def _read():
        conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
        cursor = conexao.cursor()
        comando = 'SELECT * FROM zoo.animais;'
        cursor.execute(comando)
        resposta = cursor.fetchall()
        return resposta

    @staticmethod
    def listar(read):
        conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
        resposta = AnimaisRepository._read()
        for mostrar in resposta:
            print(mostrar)
        conexao.close()

    @staticmethod
    def delete(nome_animal):
        conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM zoo.animais")
        banco = cursor.fetchall()
        for id, nome, classe, idade, sexo in banco:
            if nome == nome_animal.upper():
                comando = f"DELETE FROM animais WHERE ani_id = '{id}'"
                cursor.execute(comando)
        conexao.commit()
        cursor.close()
