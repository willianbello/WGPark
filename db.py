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
    print('ok gerada a lista de entrada')
    return lista

# função que fornece a leitura dos dados da tbsaida e retorna uma lista
def read_sd():
    curl = connect()
    ordem = curl.cursor()
    query = "SELECT pkcodsd, placacarsd, dataentrsd, horaentrsd, datasd, horasd FROM tbsaida"
    ordem.execute(query)
    lista2 = ordem.fetchall()
    print('ok gerada a lista de saida')
    return lista2

# função que deleta dados do BD baseado na pkcodentr
def delete_ent(placa):
    curl = connect()
    ordem = curl.cursor()
    query = "DELETE FROM tbentrada where pkcodentr = %s" % placa
    ordem.execute(query)
    curl.commit()
    print("ok deletado do banco o cadastro de veículo")

# função para criar usuario e senha no BD
def cadastro_usuario(nomeusuario, senhausuario):
    curl = connect()
    ordem = curl.cursor()
    query = "INSERT INTO tbusuario (nomeusuario, senhausuario) VALUES (%s, %s)"
    cadastro = (nomeusuario, senhausuario)
    ordem.execute(query, cadastro)
    print(query)
    curl.commit()
    print("ok inserido cadastro na tbusuario")

# função para criar usuario e senha de ADM no BD
def cadastro_admin():
    curl = connect()
    ordem = curl.cursor()
    nomeadmin = input("Insira o nome do novo administrador:")
    senhaadmin = input("Insira a nova senha de administrador:")
    query = "INSERT INTO tbadmin (nomeadmin, senhaadmin) VALUES (%s, %s)"
    cadastro = (nomeadmin, senhaadmin)
    ordem.execute(query, cadastro)
    curl.commit()
    print("ok inserido cadastro na tbadmin")

# função para listar os usuarios cadastrados na tbusuario do BD para poder acessar a aplicação
def check_usuario(usuario, senha):
    try:
        u = usuario
        s = senha
        curl = connect()
        ordem = curl.cursor()
        query = "SELECT nomeusuario, senhausuario FROM tbusuario WHERE nomeusuario = '%s' AND senhausuario = '%s'" % (u, s)
        ordem.execute(query)
        lista_us = ordem.fetchall()
        return lista_us
    except Exception as erro:
        print("Não foi possivel realizar a solicitação de leitura de usuario", erro)
        return erro

# função para verificar se existe determinado admin cadastrado no bd
def check_admin(usuarioadmin, senhaadmin):
    try:
        ua = usuarioadmin
        sa = senhaadmin
        curl = connect()
        ordem = curl.cursor()
        query = "SELECT nomeadmin, senhaadmin FROM tbadmin WHERE nomeadmin = '%s' AND senhaadmin = '%s'" % (ua, sa)
        ordem.execute(query)
        lista_uasa = ordem.fetchall()
        return lista_uasa
    except Exception as erro:
        print("Não foi possivel realizar a solicitação de leitura de admin", erro)
        return erro

# função que fornece a leitura dos usuarios cadastrados pelos administradores
def read_usuario():
    curl = connect()
    ordem = curl.cursor()
    query = "SELECT pkcodusuario, nomeusuario FROM tbusuario"
    ordem.execute(query)
    listausuario = ordem.fetchall()
    print('ok feita a leitura dos usuarios cadastrados pelos administradores')
    return listausuario
