from app.database.connection import *
from validations import validations as v
from utils.utils import *



#funções para manipular os dados da tabela tbl_aluno | CRUD

#-- Read
def find_student_by_id(id:int):
    '''Retornar um usuário pelo ID'''
    sql = 'SELECT * FROM tbl_aluno WHERE id_aluno = %s;'

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    #Executa a consulta SQL
                    cur.execute(sql, (id,))
                    return cur.fetchone()
                except Exception as e:
                    print(e)
                    return None

        return None

#-- Read
def find_all_students():

    sql = 'select * from tbl_aluno'

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(sql)
                    return cur.fetchall()
                except Exception as e:
                    print(e)
                    return None

        return None
    
#-- Read
def find_student_by_name(name:str):
    sql = '''SELECT * FROM tbl_aluno WHERE nome = %s;'''

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    cur.execute(sql, name)
                    return cur.fetchone()
                except Exception as e:
                    print(e)
                    return None

        return None
    
#-- Create 
def insert_student(nome:str,sobrenome:str,idade:int,telefone:str,cpf:str,data_nascimento:str):
    '''Inserir um novo aluno'''
    sql = f'''INSERT INTO tbl_aluno(nome,sobrenome,idade,telefone,cpf,data_nascimento)
    VALUES (%s, %s, %s, %s, %s, %s)'''

    
    with connect() as CONN:

        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    #Valida os valores dos argumentos
                    v.validation_age(idade)
                    v.validation_cpf(cpf)
                    v.validation_phone(telefone)
                    #executa a consulta SQL
                    cur.execute(sql, (nome, sobrenome, idade, telefone, cpf, convert_date(data_nascimento)))
                    print(f'Aluno {nome} inserido com sucesso')
                
                except (v.AgeException,v.CpfException,v.DateException,v.PhoneException) as e:
                    print(e)
                    return None
                
                except Exception as e:
                    print(f'Error: {e}')
                    return None

        return None

#-- Delete
def delete_student_by_Id(id: int):
    sql = '''DELETE FROM tbl_aluno WHERE id_aluno = %s'''

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    if find_student_by_id(id):
                        cur.execute(sql, (id,))
                    raise v.NotFoundStudent('Aluno não encontrado')
                except Exception as e:
                    print('error: ',e)
        return None
    
def delete_many_students_by_id(list):
    sql = '''DELETE FROM tbl_aluno WHERE id_aluno = %s'''

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    if find_student_by_id(id):
                        for i in list:
                            cur.execute(sql, (i,))
                    raise v.NotFoundStudent('Aluno não encontrado')
                except Exception as e:
                    print('error:', e)
        return None
    
#-- Update

def update_student(nome:str,sobrenome:str,idade:int,telefone:str,cpf:str,data_nascimento:str, id:int):

    sql = '''UPDATE tbl_aluno 
    SET nome=%s,
    sobrenome=%s,
    idade=%s,
    telefone=%s,
    cpf=%s,
    data_nascimento=%s
    WHERE id_aluno =%s'''

    with connect() as CONN:
     if CONN is not None:
         with CONN.cursor() as cur:
            try:
                if find_student_by_id(id):
                    #valida parâmetros
                    v.validation_age(idade)
                    v.validation_cpf(cpf)
                    v.validation_phone(telefone)
                #Executa a consulta SQL
                    cur.execute(sql, (nome,sobrenome,idade,telefone,cpf,convert_date(data_nascimento),id))
                    print('Aluno atualizado com sucesso!')
                    return None
                raise v.NotFoundStudent('Aluno não encontrado')

            except (v.AgeException,v.CpfException,v.PhoneException,v.NotFoundStudent) as e:
                print(e)

            except Exception as e:
                print(f'Error: {e}')