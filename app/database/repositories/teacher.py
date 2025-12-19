from app.database.connection import *
from app.validations import validations as v
from app.utils.utils import *
from ..queries import *


#funções para manipular os dados da tabela tbl_professor | CRUD

def find_teacher(id_professor=None, nome=None):

    if id_professor is not None and nome is not None:
        raise ValueError('Informe um id_professor ou nome')
    
    with connect() as CONN:
        with CONN.cursor() as cur:
            try:
                if id_professor is not None:
                        cur.execute(SELECT_TEACHER_BY_ID, (id_professor,))
                        return cur.fetchone()
                    
                if nome is not None:
                        cur.execute(SELECT_TEACHER_BY_NAME, (nome,))
                        return cur.fetchone()
                    
            except Exception as e:
                print(f'Error: {e}')
                return


def find_all_teacher():
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(SELECT_ALL_TEACHER)
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return

def insert_teacher(nome,sobrenome,telefone, cpf, data_nascimento, salario):
     
     with connect() as CONN:
            with CONN.cursor() as cur:
                try:
                    v.validation_cpf(cpf)
                    v.validation_phone(telefone)
                    cur.execute(INSERT_TEACHER, (nome,sobrenome,telefone, cpf, convert_date(data_nascimento), salario))
                
                except Exception as e:
                    print(f'Error: {e}')
                    return
                
def update_teacher(nome,sobrenome,telefone, cpf, data_nascimento, salario, id_professor):
     
     with connect() as CONN:
            with CONN.cursor() as cur:
                try:
                    v.validation_cpf(cpf)
                    v.validation_phone(telefone)
                    cur.execute(UPDATE_TEACHER, (nome,sobrenome,telefone, cpf, convert_date(data_nascimento), salario))
                
                except(v.CpfException,v.PhoneException) as e:
                     print(e)
                
                except Exception as e:
                    print(f'Error: {e}')
                    return

def delete_professor(id_professor):
     
     with connect() as CONN:
          with CONN.cursor() as cur:
            try:
                cur.execute(DELETE_TEACHER(id_professor,))
                
            except Exception as e:
                    print(f'error: {e}')
     

