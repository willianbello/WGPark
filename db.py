import mysql.connector

#testa se a conexão está funcionando e fornece o caminho para o BD
def connect():

    try:
        conexao = mysql.connector.connect(host='localhost',
                                          user='black',
                                          password='admin',

                                          database='dbwgpark')
        print("Conexao está ok", conexao)

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



'''#indica o caminho até o banco de dados
curl = connect()
ordem = curl.cursor()

#comando sql para teste
comSql = "INSERT INTO carro(pkcodcar, placacar) VALUES(%s, %s)"
#valores que serão passados para o comando
cadastro = (1, 1233456)
#executa a ação no caminho informado
ordem.execute(comSql, cadastro)
##entrega para o banco de dados a ação realizada'
curl.commit()
comSql = "SELECT * FROM carro"
ordem.execute(comSql)
resultado = ordem.fetchall()
print(resultado)'''

#função que fornece a leitura dos dados do BD e retorna uma lista
def read_ent():

    curl = connect()
    ordem = curl.cursor()
    query = "SELECT * FROM tbentrada"
    ordem.execute(query)
    lista = ordem.fetchall()
    return lista


class Cadastro:

    def __init__(self, placa, dia, horario):
        self.placa = placa
        self.dia = dia
        self.horario = horario

    # função que insere os dados no bd
    def insert_ent(self, placa, dia, horario):
        curl = connect()
        ordem = curl.cursor()
        query = "INSERT INTO tbentrada(placacarentr, dataentr, horaentr) VALUES(%s, %s, %s)"
        cadastro = (placa, dia, horario)
        ordem.execute(query, cadastro)
        curl.commit()

    # função que fornece a leitura dos dados do BD e retorna uma lista
    def read_ent(self):
        curl = connect()
        ordem = curl.cursor()
        query = "SELECT pkcodentr, placacarentr, dataentr, horaentr FROM tbentrada"
        ordem.execute(query)
        lista = ordem.fetchall()
        return lista

    def delete_ent(self, id):
        curl = connect()
        ordem = curl.cursor()
        query = "DELETE FROM tbentrada where pkcodentr = %d" %id
        ordem.execute(query)
        curl.commit()

