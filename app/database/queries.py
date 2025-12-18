'''Queries que serão ultilizadas no repositories'''
# ---------------------
# -- QUERIES STUDENT
# ---------------------

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

FIND_ALL_STUDENT = 'select * from tbl_aluno'

FIND_STUDENT_BY_ID = 'SELECT * FROM tbl_aluno WHERE id_aluno = %s'

FIND_STUDENT_BY_NAME = 'SELECT * FROM tbl_aluno WHERE nome = %s'

DELETE_STUDENT_BY_ID = '''DELETE FROM tbl_aluno WHERE id_aluno = %s'''

MATRICULATION = '''UPDATE tbl_aluno SET fk_turma = %s WHERE id_aluno = %s'''

# ----------------
# - QUERIES CLASS
# ----------------

#--------------------- READ ---------------------
SELECT_CLASS_ID =  '''SELECT * FROM tbl_turma WHERE id_turma = %s'''

SELECT_ALL_CLASS = '''SELECT * FROM tbl_turma'''

SELECT_CLASS_TEACHER = '''SELECT * FROM tbl_turma WHERE fk_professor = %s'''

SELECT_CLASS_SHIFT = '''SELECT * FROM tbl_turma WHERE turno = %s'''

SELECT_CLASS_COURSE = '''SELECT * FROM tbl_turma WHERE fk_curso = %s'''

SELECT_CLASS_BETWEEN_DATE = '''SELECT * FROM tbl_turma WHERE criado_em BETWEEN %s AND %s'''

#------------------ CREATE -----------------------
INSERT_CLASS = '''INSERT INTO tbl_turma(fk_professor, fk_curso, turno) Values
(%s,%s,%s)'''

#------------------- UPDATE ----------------------
UPDATE_CLASS = '''UPDATE tbl_turma SET fk_professor = %s WHERE id_turma = %s''' #definido que só poderemos mudar os dados de professor

#-------------------- DELETE --------------------
DELETE_CLASS = '''DELETE FROM tbl_turma WHERE id_turma = %s'''