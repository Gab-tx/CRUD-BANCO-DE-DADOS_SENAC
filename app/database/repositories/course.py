from app.database.connection import *
from app.validations import validations as v
from app.utils.utils import *
from ..queries import *

def find_course_by_id(id_turma):
    
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(SELECT_COURSE_ID,(id_turma,))
                    return cur.fetchone()
                except Exception as e:
                    print(f'Error: {e}')


def display_course_by_turma_id(id_turma):
    sql = '''SELECT * FROM tbl_turma WHERE id_turma = %s'''
    
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(sql, (id_turma,))
                    turma_dados = cur.fetchone()
                    
                    return find_course_by_id(turma_dados[2])
                except Exception as e:
                    print(f'Error: {e}')

def find_course_by_name(nome:str):

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(SELECT_COURSE_BY_NAME,(nome,))
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')

def find_course_by_workload(carga_horaria:int):

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(SELECT_COURSE_BY_WORKLOAD,(carga_horaria,))
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')

def find_all_courses():

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(SELECT_ALL_COURSE)
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')

def insert_course(nome, descricao, carga_horaria):

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(INSERT_COURSE, (nome, descricao, carga_horaria))
                    return None
                except Exception as e:
                    print(f'Error: {e}')
        return None
    
def update_course(id_curso, nome=None, descricao=None, carga_horaria=None):

    with connect() as CONN:
        if CONN is None:
            return 
        
        with CONN.cursor() as cur:
            try:
                if nome is not None:
                    cur.execute(UPDATE_COURSE_NAME, (nome,id_curso))

                if descricao is not None: 
                    cur.execute(UPDATE_COURSE_DESCRIPTION, (descricao, id_curso))

                if carga_horaria is not None:
                    cur.execute(UPDATE_COURSE_WORKLOAD, (carga_horaria,id_curso))

            except Exception as e:
                print(f'Error: {e}')

def delete_course_by_id(id_curso):

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(DELETE_COURSE_BY_ID, (id_curso))
                    return None
                except Exception as e:
                    print(f'Error: {e}')
        return None
