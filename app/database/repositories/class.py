from app.database.connection import *
from app.validations import validations as v
from app.utils.utils import *
from ..queries import *


def find_class_by_id(id:int):
    '''Retorna as turmas pelo id'''

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(SELECT_CLASS_ID,(id,))
                    return cur.fetchone()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None
    
def find_all_class():
    '''Retorna todas as turmas cadastradas'''

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(SELECT_ALL_CLASS)
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None
def find_class_teacher(id_teacher):
    '''Retorna os turma por professores cadastrados'''

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(SELECT_CLASS_TEACHER, (id_teacher,))
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
    return 

def find_class_shift(id_shift):
    '''Retorna as turmas por turnos cadastrados'''

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(SELECT_CLASS_SHIFT, (id_shift,))
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
    return None

def find_class_by_course(id_course):
    '''Retorna as turmas por cursos cadastrados'''

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(SELECT_CLASS_COURSE, (id_course,))
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
    return None

def find_class_between_date(initial_date, final_date):
    '''Retorna as turma por data inicial e final'''

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(SELECT_CLASS_BETWEEN_DATE, (initial_date, final_date))
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
    return None

def insert_class(id_professor:int, id_course:int, shift: str):
    '''Cria uma nova "row" da tabela turma com uma nova turma onde terá: professor, curso e seu turno.'''

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(INSERT_CLASS, (id_professor, id_course, shift))
                    return None
                except Exception as e:
                    print(f'Error: {e}')
                    return None
    return None

def update_class_professor_by_class_id(id_professor:int, id_turma):
    '''Atualiza o professor, especificado pelo id, da turma também especificada pelo id'''
    
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(UPDATE_CLASS, (id_professor, id_turma))
                    return None
                except Exception as e:
                    print(f'Error: {e}')
                    return None
    return None

def delete_class(id_turma):
    '''Deleta da tabela de turmas a turma em que o id for passado como parâmetro'''

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(DELETE_CLASS, (id_turma,))
                    return None
                except Exception as e:
                    print(f'Error: {e}')
                    return None
    return None
