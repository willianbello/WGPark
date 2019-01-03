import mysql.connector

#testa se a conexão está funcionando e fornece o caminho para o BD
def connect():

    try:
        conexao = mysql.connector.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='dbwgpark')
        return conexao
    # se não estiver, retorna um erro
    except Exception as erro:
        print("Não foi possivel conectar", erro)
        return erro

#função que insere os dados no bd
def insert_ent(placa, dia, horario):

    curl = connect()
    ordem = curl.cursor()
    query = "INSERT INTO tbentrada(placacarentr, dataentr, horaentr) VALUES(%s, %s, %s)"
    cadastro = (placa, dia, horario)
    ordem.execute(query, cadastro)
    curl.commit()
    print(query)


#função que fornece a leitura dos dados do BD e retorna uma lista
def read_ent():

    curl = connect()
    ordem = curl.cursor()
    query = "SELECT * FROM tbentrada"
    ordem.execute(query)
    lista = ordem.fetchall()
    return lista
