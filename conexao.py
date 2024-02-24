import sqlite3

conexao = sqlite3.connect('SQL_exercicio')
cursor = conexao.cursor()

# 1 - CRIANDO TABELA
# cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2 - INSERINDO DADOS
# cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES (1,"André",20,"engenharia")')
# cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES (2,"Pedro",24,"arquitetura")')
# cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES (3,"Maria",22,"engenharia")')
# cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES (4,"Luiza",19,"direito")')
# cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES (5,"Lais",23,"engenharia")')

# 3 - CONSULTAS BÁSICAS
# consulta = cursor.execute('SELECT * FROM alunos')
# consulta = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20')
# consulta = cursor.execute('SELECT * FROM alunos WHERE curso = "engenharia" ORDER BY nome')
# consulta = cursor.execute('SELECT COUNT(*) FROM alunos')
# for aluno in consulta:
#     print(aluno)

# 4 - ATUALIZAÇÃO e REMOÇÃO
#cursor.execute('UPDATE alunos SET idade = "20" WHERE id=4')
#cursor.execute('DELETE FROM alunos WHERE id=5')

# 5 - NOVA TABELA
# cursor.execute('CREATE TABLE clientes (id INT, nome VARCHAR(100), idade INT, saldo FLOAT);')

#   - INSERINDO DADOS
# cursor.execute('INSERT INTO clientes (id,nome,idade,saldo) VALUES (1,"Camila",38,910.40)')
# cursor.execute('INSERT INTO clientes (id,nome,idade,saldo) VALUES (2,"Carlos",68,910.40)')
# cursor.execute('INSERT INTO clientes (id,nome,idade,saldo) VALUES (3,"Luiza",29,2210.55)')
# cursor.execute('INSERT INTO clientes (id,nome,idade,saldo) VALUES (4,"Maria",23,4000)')
# cursor.execute('INSERT INTO clientes (id,nome,idade,saldo) VALUES (5,"Paulo",33,320.82)')
# cursor.execute('INSERT INTO clientes (id,nome,idade,saldo) VALUES (6,"Felipe",42,743)')
# cursor.execute('INSERT INTO clientes (id,nome,idade,saldo) VALUES (7,"Joana",51,90.85)')

# 6 - CONSULTAS E FUNÇÃO AGREGADAS
# consulta = cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30')
# for cliente in consulta:
#     print(cliente)

# consulta = cursor.execute('SELECT ROUND (AVG(saldo),2) FROM clientes')
# resultado = cursor.fetchone()
# print("Saldo médio dos clientes:", resultado[0])

# cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')
# cliente_max_saldo = cursor.fetchone()
# print("Cliente com o saldo máximo:", cliente_max_saldo)

# consulta = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
# for cliente in consulta:
#   print(cliente)

# 7 - ATUALIZAÇÃO e REMOÇÃO com CONDIÇÕES
# cursor.execute('UPDATE clientes SET saldo = "1000.50" WHERE id=2')
# cursor.execute('DELETE FROM clientes WHERE id=7')

# 8 - JUNÇÃO DE TABELAS
# cursor.execute('CREATE TABLE compras (id INT, cliente_id INT, produto VARCHAR(100), valor FLOAT);')

# cursor.execute('INSERT INTO compras (id,cliente_id,produto,valor) VALUES (1,3,"caderno 10 matérias", 19.95)')
# cursor.execute('INSERT INTO compras (id,cliente_id,produto,valor) VALUES (2,5,"caderno 10 matérias", 19.95)')
# cursor.execute('INSERT INTO compras (id,cliente_id,produto,valor) VALUES (3,2,"caderno 10 matérias", 19.95)')
# cursor.execute('INSERT INTO compras (id,cliente_id,produto,valor) VALUES (4,1,"borracha", 3.40)')
# cursor.execute('INSERT INTO compras (id,cliente_id,produto,valor) VALUES (5,1,"caneta preta", 5.60)')
# cursor.execute('INSERT INTO compras (id,cliente_id,produto,valor) VALUES (6,5,"caneta preta", 5.60)')

# dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')
# for compra in dados:
#     print(compra)


conexao.commit()
conexao.close
