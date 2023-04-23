import time
import mysql.connector

from entities.Animais import Animais
from repositories.AnimaisRepository import *

menus = ['1 - Cadastrar Funcionários', '2 - Ver Funcionários', '3 - Listar Visitantes',
         '4 - Cadastro de Visitantes', '5 - Compra de Ingressos', '6 - Ver peixes',
         '7 - Ver mamíferos', '8 - Ver aves', '9 - Cadastrar Animais', '10 - Listar Animais',
         '11 - Excluir animal', '12 - Sair']

ingressos = ['1 - PASSEIO COMPLETO COM GUIAS E ALIMENTAÇÃO: R$ 100,00', '2 - PASSEIO COM GUIAS: R$ 70,00',
             '3 - PASSEIO SEM GUIAS: R$ 50,00']


def leia_int(msg):
    """
    Método para ler um número inteiro

    :param msg: recebe um número para verificação de menu
    :return: retorna 0
    """
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('Digite um número inteiro válido!')
            continue
        except KeyboardInterrupt:
            print('Usuário não digitou esse número')
            return 0
        else:
            return numero


def linha():
    """
    Método para criar uma separação de menu.

    :return: retorna o caractere " - " 50 vezes.
    """
    return '-' * 50


def cabecalho(txt):
    """
    Método para criar um cabeçalho organizado

    :param txt: Recebe uma frase para ser inserida no cabeçalho.
    :return: retorna a frase centralizada em exatamente 50 caracteres.
    """
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    """
    Método que organiza a criação de menus.

    :param lista: recebe a lista de opções.
    :return: retorna a opção escolhida pelo usuário
    """
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{item}')
        c += 1
    print(linha())
    opcao = leia_int('Sua opção: ')
    return opcao


def cadastrar_funcionarios():
    """
    Método para cadastrar funcionários e inserí-los no banco de dados 'zoologico'
    :return:
    """
    try:
        conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
        cursor = conexao.cursor()
        nome = input('Digite o nome do(a) funcionário(a): ').upper()
        idade = int(input('Digite a idade do(a) funcionário(a): '))
        cpf = int(input('Digite o CPF do(a) funcionário(a) (Somente números): '))
        matricula = int(input('Digite a Matrícula do(a) funcionário(a): '))
        comando = f"INSERT INTO funcionarios(func_nome, func_cpf, func_idade, func_matricula) VALUES ('{nome}', '{cpf}', '{idade}', '{matricula}');"
        cursor.execute(comando)
        conexao.commit()
        time.sleep(1)
        conexao.close()
    except ValueError:
        print('Erro! Digite valores numéricos para idade, CPF e Matrícula.')
    except KeyboardInterrupt:
        print('Dados não repassados')


def listar_funcionarios():
    """
    Método para listar os funcionários do zoológico

    :return: Retorna a lista 'Lista_funcionarios'
    """
    print('Lista de Funcionários: ')
    conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
    cursor = conexao.cursor()
    comando = 'SELECT * FROM zoo.funcionarios;'
    cursor.execute(comando)
    resposta = cursor.fetchall()
    for id, nome, cpf, idade, matricula in resposta:
        print(f'Nome: {nome}, CPF: {cpf}, {idade} anos, Nº da Matrícula: {matricula}')


def listar_visitantes():
    """
    Método para listar os funcionários do zoológico

    :return: Retorna a lista 'Lista_luncionarios'
    """
    print('Lista de Visitantes: ')
    conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
    cursor = conexao.cursor()
    comando = 'SELECT * FROM zoo.visitantes;'
    cursor.execute(comando)
    resposta = cursor.fetchall()
    for id, nome, cpf, idade, ingresso in resposta:
        print(f'ID: {id} - Nome: {nome}, CPF: {cpf}, {idade} anos')


def cadastrar_visitantes():
    try:
        conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
        nome = input('Digite o nome do(a) visitante: ').upper()
        idade = int(input('Digite a idade do(a) visitante: '))
        cpf = int(input('Digite o CPF do(a) visitante (Somente números): '))
        print(f'{nome} inserido com sucesso!')
        cursor = conexao.cursor()
        comando = f"INSERT INTO visitantes(vis_nome, vis_cpf, vis_idade, vis_ingresso) VALUES ('{nome}', '{cpf}', '{idade}', '{0}');"
        cursor.execute(comando)
        conexao.commit()
        time.sleep(1)
        conexao.close()
    except ValueError:
        print('Erro! Digite valores numéricos para idade e/ou CPF')
    except KeyboardInterrupt:
        print('Dados não repassados corretamente')


def compra_ingresso():
    valida = int(input('Digite seu CPF: '))
    try:
        conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
        cursor = conexao.cursor()
        comando = 'SELECT vis_nome, vis_cpf, vis_idade, vis_ingresso FROM zoo.visitantes;'
        cursor.execute(comando)
        banco = cursor.fetchall()
        if len(banco) == 0:
            print('Lista de Visitantes vazia! ')
            return
        for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
            if str(valida) == cpf_vis:
                print(f'Usuário {nome_vis} encontrado')
                resp = menu(ingressos)
                while resp != 1 or resp != 2 or resp != 3:
                    if resp == 1:
                        forma_pag = input('Forma de pagamento: ').upper()
                        if forma_pag == 'DINHEIRO':
                            recebido = int(input('Quantidade recebida: '))
                            if recebido == 100:
                                print('Pagamento concluído com sucesso! Aproveite o Passeio!')
                                comando = f"update visitantes set vis_ingresso = '{1}' where {str(valida)} = vis_cpf;"
                                cursor.execute(comando)
                                conexao.commit()
                                return
                            elif recebido > 100:
                                troco = recebido - 100
                                print(f'Troco: R${troco}')
                                comando = f"update visitantes set vis_ingresso = '{1}' where {str(valida)} = vis_cpf;"
                                cursor.execute(comando)
                                conexao.commit()
                                return
                            elif recebido < 100:
                                print('Dinheiro insuficiente!')
                                resp = 1
                        else:
                            print(f'Pagamento somente em Dinheiro!')
                            return
                    if resp == 2:
                        forma_pag = input('Forma de pagamento: ').upper()
                        if forma_pag == 'DINHEIRO':
                            recebido = int(input('Quantidade recebida: '))
                            if recebido == 70:
                                print('Pagamento concluído com sucesso! Aproveite o Passeio!')
                                comando = f"update visitantes set vis_ingresso = '{1}' where {str(valida)} = vis_cpf;"
                                cursor.execute(comando)
                                conexao.commit()
                                return
                            elif recebido > 70:
                                troco = recebido - 70
                                print(f'Troco: R${troco}')
                                print('Pagamento concluído com sucesso! Aproveite o Passeio!')
                                comando = f"update visitantes set vis_ingresso = '{1}' where {str(valida)} = vis_cpf;"
                                cursor.execute(comando)
                                conexao.commit()
                                return
                            elif recebido < 70:
                                print('Dinheiro insuficiente!')
                                resp = 2
                        else:
                            print(f'Pagamento somente em Dinheiro!')
                            return
                    if resp == 3:
                        forma_pag = input('Forma de pagamento: ').upper()
                        if forma_pag == 'DINHEIRO':
                            recebido = int(input('Quantidade recebida: '))
                            if recebido == 50:
                                print('Pagamento concluído com sucesso! Aproveite o Passeio!')
                                comando = f"update visitantes set vis_ingresso = '{1}' where {str(valida)} = vis_cpf;"
                                cursor.execute(comando)
                                conexao.commit()
                                return
                            elif recebido > 50:
                                troco = recebido - 50
                                print(f'Troco: R${troco}')
                                print('Pagamento concluído com sucesso! Aproveite o Passeio!')
                                comando = f"update visitantes set vis_ingresso = '{1}' where {str(valida)} = vis_cpf;"
                                cursor.execute(comando)
                                conexao.commit()
                                return
                            elif recebido < 50:
                                print('Dinheiro insuficiente!')
                                resp = 3
                        else:
                            print(f'Pagamento somente em dinheiro!')
                            return
        for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
            if str(valida) != cpf_vis:
                print('Faça o cadastro antes de comprar o ingresso!')
                return
    except ValueError:
        print('Digite um valor numérico inteiro e sem hífens, barras ou espaços para o CPF!')
    except KeyboardInterrupt as erro:
        print(erro)


def valida_entrada_peixes():
    try:
        conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
        cursor = conexao.cursor()
        comando = 'SELECT vis_nome, vis_cpf, vis_idade, vis_ingresso FROM zoo.visitantes;'
        cursor.execute(comando)
        banco = cursor.fetchall()
        cpf_valida = int(input('Digite seu CPF(somente números): '))
        for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
            if str(cpf_valida) == cpf_vis:
                if ingresso_vis == 1:
                    print('Visualizando Peixes')
                    print("Aqui vão algumas curiosidades sobre os peixes: ")
                    print("Os peixes usam suas cordas vocais para emitir sons e se comunicarem com seus pares. É isso\n"
                          "mesmo! Apesar de ser inaudível para nós, os peixes costumam se comunicar pela vocalização.\n")
                    print("Alguma vez você já se perguntou se os peixes sentem frio? A resposta é sim! Inclusive \n"
                          "quando a temperatura da água está extremamente baixa, o metabolismo desacelera \n e faz com "
                          "que o peixe se movimente mais lentamente e, por vezes, perca até o apetite. ")
                    return
                else:
                    print("Não tem ingresso, compre um antes de visitar os peixes!")
                    return
        for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
            if str(cpf_valida) != cpf_vis:
                print("CPF não encontrado, faça o cadastro antes de visitar os peixes!")
                break
    except ValueError:
        print('Digite um valor numérico inteiro e sem hífens, barras ou espaços para o CPF!')
    except KeyboardInterrupt as erro:
        print(erro)


def valida_entrada_mamiferos():
    try:
        conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
        cursor = conexao.cursor()
        comando = 'SELECT vis_nome, vis_cpf, vis_idade, vis_ingresso FROM zoo.visitantes;'
        cursor.execute(comando)
        banco = cursor.fetchall()
        cpf_valida = int(input('Digite seu CPF(somente números): '))
        for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
            if str(cpf_valida) == cpf_vis:
                if ingresso_vis == 1:
                    print('Visualizando Mamíferos, não são magníficos?')
                    print("Aqui vão algumas curiosidades sobre os mamíferos: ")
                    print("O morcego é o único mamífero capaz de voar. Esta habilidade foi desenvolvida ao longo do "
                          "tempo, visando à sobrevivência da espécie.\n")
                    print("Os mamíferos são os únicos animais que têm o corpo coberto de pelos, mas algumas espécies "
                          "possuem apenas resquícios de pelos e uma camada de gordura subcutânea para o aquecimento "
                          "do animal.")
                    return
                else:
                    print("Não tem ingresso, compre um antes de visitar os mamíferos!")
                    return
        for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
            if str(cpf_valida) != cpf_vis:
                print("CPF não encontrado, faça o cadastro antes de visitar os mamíferos!")
                break
    except ValueError:
        print('Digite um valor numérico para o CPF!')
    except KeyboardInterrupt as erro:
        print(erro)


def valida_entrada_aves():
    try:
        conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
        cursor = conexao.cursor()
        comando = 'SELECT vis_nome, vis_cpf, vis_idade, vis_ingresso FROM zoo.visitantes;'
        cursor.execute(comando)
        banco = cursor.fetchall()
        cpf_valida = int(input('Digite seu CPF(somente números): '))
        for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
            if str(cpf_valida) == cpf_vis:
                if ingresso_vis == 1:
                    print('Visualizando Aves, não são esplendorosos?')
                    print("Aqui vão algumas curiosidades sobre as aves: ")
                    print("As aves são diferentes de todos os outros animais porque elas têm penas, bico, duas asas e "
                          "não têm dentes.\n")
                    print("A maioria das aves pode voar. Algumas podem nadar como o pingüim, e correr como o avestruz.")
                    return
                else:
                    print("Não tem ingresso, compre um antes de visitar as aves!")
                    return
        for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
            if str(cpf_valida) != cpf_vis:
                print("CPF não encontrado, faça o cadastro antes de visitar as aves!")
                break
    except ValueError:
        print('Digite um valor numérico para o CPF!')
    except KeyboardInterrupt as erro:
        print(erro)


def zerar_ingressos():
    conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoo')
    cursor = conexao.cursor()
    comando = 'SELECT vis_nome, vis_cpf, vis_idade, vis_ingresso FROM zoo.visitantes;'
    cursor.execute(comando)
    banco = cursor.fetchall()
    for nome_vis, cpf_vis, idade_vis, ingresso_vis in banco:
        if ingresso_vis == 1:
            comando = f"update visitantes set vis_ingresso = '{0}' where vis_ingresso = '{1}';"
            cursor.execute(comando)
            conexao.commit()
            conexao.close()


class MyMethods:

    @staticmethod
    def cadastrar_animal():
        try:
            nome = input('Digite o nome do animal: ').upper()
            classe = input('Classe do animal: ').upper()
            idade = int(input('Idade: '))
            sexo = input('Sexo: ').upper()
            ani_cadastrar = Animais(nome, classe, idade, sexo)
            AnimaisRepository.create(ani_cadastrar)
        except ValueError as erro:
            print(erro)
        except KeyboardInterrupt as aviso:
            print(aviso)

    @staticmethod
    def listar_animais():
        """
        Método estático que deve solicitar que o repositorio realize uma consulta de todos os Produtos cadastrados
        no banco de dados. Listando cada produto e seu respectivo indice na lista de produtos recebida pelo repositorio.
        """
        AnimaisRepository.listar(AnimaisRepository._read())

    @staticmethod
    def excluir_animal():
        """
        Método estático que deve solicitar ao usuario o nome de um Produto, pedir que o repositorio busque por este
        produtro no banco, e caso o produto exista no banco de dados, deverá realize a remoção do produto no banco de
        dados. Este método deverá fazer o tratamento de exceções geradas através entrada inconsistente de dados pelo
        usuário (basta exibir o texto da exceção).
        """
        try:
            busca = input('Digite o nome do animal: ').upper()
            AnimaisRepository.delete(busca)
        except ValueError as erro:
            print(erro)
        except KeyboardInterrupt as erro:
            print(erro)
