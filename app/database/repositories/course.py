from app.database.connection import *
from app.validations import validations as v
from app.utils.utils import *
from ..queries import *

def find_course_by_id(id_turma):
    sql ='''SELECT * FROM tbl_curso WHERE id_curso = %s'''
    
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(sql,(id_turma,))
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

