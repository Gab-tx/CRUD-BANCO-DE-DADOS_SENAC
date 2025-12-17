'''Queries que serão ultilizadas no repositories'''

#QUERIES STUDENT

INSERT_STUDENT = '''INSERT INTO tbl_aluno(nome,sobrenome,idade,telefone,cpf,data_nascimento)
    VALUES (%s, %s, %s, %s, %s, %s)'''

UPDATE_STUDENT = '''UPDATE tbl_aluno 
    SET nome=%s,
    sobrenome=%s,
    idade=%s,
    telefone=%s,
    cpf=%s,
    data_nascimento=%s
    WHERE id_aluno =%s'''

# def find_all_students():

#     sql = 'select * from tbl_aluno'

FIND_ALL_STUDENT = 'select * from tbl_aluno'

FIND_STUDENT_BY_ID = 'SELECT * FROM tbl_aluno WHERE id_aluno = %s'

FIND_STUDENT_BY_NAME = 'SELECT * FROM tbl_aluno WHERE nome = %s'

DELETE_STUDENT_BY_ID = '''DELETE FROM tbl_aluno WHERE id_aluno = %s'''