import mysql.connector;

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'poasul2013',
    database = 'library'
)

cursor = conexao.cursor()

id_livro = 1
titulo = "Volta ao Mundo em Oitenta dias"
autor = "Júlio Verne"
editora = "Melhoramentos"
paginas = 182

comando = f'INSERT INTO biblioteca (id_livro, titulo, autor, editora, paginas) VALUES ({id_livro}, {titulo}, {autor}, {editora}, {paginas})'
cursor.execute(comando)
conexao.commit() # Caso eu editar o bando de dados

# resultado = cursor.fetchall() # Caso eu vá ler o banco de dados abc


cursor.close()
conexao.close