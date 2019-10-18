import sqlite3

db_name = "disciplinas.db"
table_name = "disciplina_aluno"

sql_create_table = f"CREATE TABLE disciplina_aluno (id INT IDENTITY PRIMARY KEY, disciplina INT NOT NULL, aluno_id INT NOT NULL);"

def createTable(cursor, sql):
    cursor.execute(sql)

def popularDb(cursor, disciplina, aluno_id):
    pass

def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_table)
    try:
        popularDb(cursor, "Desenvolvimento de aplic. distribuidas", 1)
        popularDb(cursor, "Estrutura de dados", 2)
        popularDb(cursor, "LPT 1", 3)
    except:
        pass
    cursor.close()
    connection.commit()
    connection.close()
    
init()
