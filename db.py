import mysql.connector


def connect():

    # testa se a conexão está funcionando
    try:
        conexao = mysql.connector.connect(host='localhost',
                                          user='root',
                                          password='giovani',
                                          database='dbwgpark')
        print("Conexao está ok", conexao)
        return conexao
    # se não estiver, retorna um erro
    except Exception as erro:
        print("Não foi possivel conectar", erro)
        return erro


def insert(placa):
    cod = 1
    curl = connect()
    ordem = curl.cursor()
    comSql = "INSERT INTO carro(pkcodcar, placacar) VALUES(%s, %s)"
    cadastro = (cod, placa)
    ordem.execute(comSql, cadastro)
    curl.commit()



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