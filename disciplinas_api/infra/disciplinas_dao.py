import sqlite3
from model.disciplina import Disciplina
from contextlib import closing

db_name = "disciplinas.db"
model_name = "disciplina"
model_name_relationship = "disciplina_aluno"

def con():
    return sqlite3.connect(db_name)

def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT id, nome, professor_id FROM {model_name}")
        rows = cursor.fetchall()
        registros = []
        for (id, nome, professor_id) in rows:
            registros.append(Professor.criar({"id": id, "nome": nome, "professor_id":professor_id}))
        return registros

def consultar(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT id, nome, professor_id FROM {model_name} WHERE id = ?", (int(id),))
        row = cursor.fetchone()
        if row == None:
            return None
        return Professor.criar({"id": row[0], "nome": row[1], "professor_id":row[2]})

def consultar_por_nome(nome):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT id, nome, professor_id FROM {model_name} WHERE nome = ?", (nome,))
        row = cursor.fetchone()
        if row == None:
            return None
        return Professor.criar({"id": row[0], "nome": row[1], "professor_id":row[2]})

def cadastrar(disciplina):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (nome, professor_id) VALUES (?, ?)"
        result = cursor.execute(sql, (disciplina.nome, disciplina.professor_id))
        connection.commit()
        if cursor.lastrowid:
            disciplina.associar_id(cursor.lastrowid)
            return disciplina
        else:
            return None

def alterar(disciplina):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET nome = ? WHERE id = ?"
        cursor.execute(sql, (disciplina.nome, disciplina.id))
        connection.commit()

def remover(disciplina):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name} WHERE id = ?"
        cursor.execute(sql, f"{disciplina.id}")
        connection.commit()

#Disciplina-aluno

def cadastrar_aluno(disciplina, aluno_id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name_relationship} (disciplina_id, aluno_id) VALUES (?, ?)"
        result = cursor.execute(sql, (disciplina.id, aluno_id))
        connection.commit()
        if cursor.lastrowid:
            disciplina.associar_id(cursor.lastrowid)
            return disciplina
        else:
            return None
            
def remover_aluno(disciplina, aluno_id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name} WHERE aluno_id = ?"
        cursor.execute(sql, f"{disciplina.aluno_id}")
        connection.commit()
    
def consultar_alunos(disciplina):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT id, disciplina, aluno_id FROM {model_name} WHERE disciplina = ?", (disciplina,))
        row = cursor.fetchone()
        if row == None:
            return None
        return Professor.criar({"id": row[0], "disciplina": row[1], "aluno_id":row[2]})
    