import mysql.connector
#testa se a conexão está funcionando
try:
    conexao = mysql.connector.connect(host='localhost',
                                      user='root',
                                      password='admin',
                                      database='wgpark')
    print("Conexao está ok")
#se não estiver, retorna um erro
except Exception as erro:
    print("Não foi possivel conectar", erro)

#indica o caminho até o banco de dados
ordem = conexao.cursor()
'''#comando sql para teste
comSql = "INSERT INTO carro(pkcodcar, placacar) VALUES(%s, %s)"
#valores que serão passados para o comando
cadastro = (1, 1233456)
#executa a ação no caminho informado
ordem.execute(comSql, cadastro)
##entrega para o banco de dados a ação realizada'''
comSql = "SELECT * FROM carro"
ordem.execute(comSql)
resultado = ordem.fetchall()
print(resultado)
