import sqlite3

db_name = "disciplinas.db"
table_name = "disciplina"

sql_create_table = f"CREATE TABLE disciplina (id INT IDENTITY PRIMARY KEY, nome VARCHAR (50), professor_id INT NOT NULL);"

def createTable(cursor, sql):
    cursor.execute(sql)

def popularDb(cursor, nome, professor_id):
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
