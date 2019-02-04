import mysql.connector


# testa se a conexão está funcionando e fornece o caminho para o BD
def connect():

    try:
        conexao = mysql.connector.connect(host='localhost',
                                          user='root',
                                          password='giovani',
                                          database='dbwgpark')
        print("ok conectado")
        return conexao

    # se não estiver, retorna um erro
    except Exception as erro:
        print("Não foi possivel conectar", erro)
        return erro

# função que insere os dados na tbentrada
def insert_ent(placa, dia, horario):
    curl = connect()
    ordem = curl.cursor()
    query = "INSERT INTO tbentrada(placacarentr, dataentr, horaentr) VALUES(%s, %s, %s)"
    cadastro = (placa, dia, horario)
    ordem.execute(query, cadastro)
    curl.commit()
    print("ok inserido na tbentrada")

# função para inserir os dados na tbsaida
def insert_sd(placacarsd, dataentrsd, horaentrsd, datasd, horasd):

    curl = connect()
    ordem = curl.cursor()
    query = "INSERT INTO tbsaida(placacarsd, dataentrsd, horaentrsd, datasd, horasd) VALUES(%s, %s, %s, %s, %s)"
    cadastro = (placacarsd, dataentrsd, horaentrsd, datasd, horasd)
    ordem.execute(query, cadastro)
    curl.commit()
    print("ok inserido na tbsaida")

# função que fornece a leitura dos dados da tbentrada e retorna uma lista
def read_ent():
    curl = connect()
    ordem = curl.cursor()
    query = "SELECT pkcodentr, placacarentr, dataentr, horaentr FROM tbentrada"
    ordem.execute(query)
    lista = ordem.fetchall()
    return lista

# função que fornece a leitura dos dados da tbsaida e retorna uma lista
def read_sd():
    curl = connect()
    ordem = curl.cursor()
    query = "SELECT pkcodsd, placacarsd, dataentrsd, horaentrsd, datasd, horasd FROM tbsaida"
    ordem.execute(query)
    lista2 = ordem.fetchall()
    return lista2

# função que deleta dados do BD baseado na pkcodentr
def delete_ent(placa):
    curl = connect()
    ordem = curl.cursor()
    query = "DELETE FROM tbentrada where pkcodentr = %s" % placa
    ordem.execute(query)
    curl.commit()
    print("ok deletado do banco")

# função para criar usuario e senha no BD
def cadastro_usuario():
    curl = connect()
    ordem = curl.cursor()
    nomeusuario = input("Insira o nome do novo usuario:")
    senhausuario = input("Insira a nova senha:")
    query = "INSERT INTO tbusuario (nomeusuario, senhausuario) VALUES (%s, %s)"
    cadastro = (nomeusuario, senhausuario)
    ordem.execute(query, cadastro)
    curl.commit()
    print("ok inserido na tbusuario")

# função para verificar se existe determinado usuario cadastrado no bd
def check_usuario(usuario, senha):
    try:
        u = usuario
        s = senha
        curl = connect()
        ordem = curl.cursor()
        query = "SELECT nomeusuario, senhausuario FROM tbusuario WHERE nomeusuario = '%s' AND senhausuario = '%s'" % (u, s)
        ordem.execute(query)
        listasenha = ordem.fetchall()
        return listasenha
    except Exception as erro:
        print("Não foi possivel realizar a situação", erro)
        return erro
