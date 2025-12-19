-- COMANDOS DDL: LINGUAGEM DE DEFINIÇÃO DE DADOS
/*
	-CREATE: CRIAR;
	-ALTER: ALTERAR/MODIFICAR;
	-DROP: EXCLUIR

	
	CONSTRAINTS:

	-PRIMARY KEY;
	-NOT NULL;
	-DEFAULT
	-CURRENT_DATE
	-UNIQUE
*/

-- TABELA PARA REPRESENTAR ALUNO

CREATE TABLE tbl_aluno(
	id_aluno SERIAL PRIMARY KEY,
	nome VARCHAR(25) NOT NULL,
	sobrenome VARCHAR(25) NOT NULL,
	idade INT NOT NULL,
	telefone VARCHAR(11) NOT NULL,
	cpf VARCHAR(11) NOT NULL,
	data_nascimento DATE NOT NULL,
	criado_em DATE DEFAULT CURRENT_DATE
);
-- TABELA PARA REPRESENTAR PROFESSOR

CREATE TABLE tbl_professor(
	id_professor SERIAL PRIMARY KEY,
	nome VARCHAR(25) NOT NULL,
	sobrenome VARCHAR(25) NOT NULL,
	idade INT NOT NULL,
	telefone VARCHAR(25) NOT NULL,
	cpf VARCHAR(11) NOT NULL,
	data_nasc DATE NOT NULL,
	data_admissao DATE DEFAULT CURRENT_DATE,
	salario DECIMAL(10, 2) NOT NULL
);

CREATE TABLE tbl_curso(
	id_curso SERIAL PRIMARY KEY,
	nome VARCHAR(25) NOT NULL,
	descricao TEXT DEFAULT 'Sem informações adicionais',
	carga_horaria INT NOT NULL
	criado_em DATE DEFAULT CURRENT_DATE
)

--TABELA PARA REPRESENTAR TURMA
CREATE TABLE tbl_turma(
	id_turma SERIAL PRIMARY KEY,
	fk_professor INT NOT NULL,
	fk_curso INT NOT NULL,
	turno VARCHAR(10) NOT NULL,
	criado_em DATE DEFAULT CURRENT_DATE,
	FOREIGN KEY (fk_professor) REFERENCES tbl_professor(id_professor),
	FOREIGN KEY (fk_curso) REFERENCES tbl_curso(id_curso)
);

--Adicionar uma nova coluna em tbl_aluno por nome fk_turma
ALTER TABLE tbl_aluno ADD COLUMN fk_turma INT REFERENCES tbl_turma(id_turma)

-- ALTERAR AS TABELAS ADICIONANDO UNIQUE PARA AS COLUNAS CPF

ALTER TABLE tbl_aluno ADD CONSTRAINT tbl_aluno_uniqueCpf
UNIQUE (cpf);

ALTER TABLE tbl_professor ADD CONSTRAINT tbl_professor_uniqueCpf
UNIQUE (cpf);

ALTER TABLE tbl_curso 
ALTER COLUMN descricao TYPE TEXT;

ALTER TABLE tbl_curso 
ALTER COLUMN descricao 
SET DEFAULT 'Sem informações adicionais';

-- COMANDOS DML: LINGUAGEM DE MANIPULAÇÃO DE DADOS
/*
	INSERT INTO: Cadastrar instâncias de dados nas tabelas
	UPDATE SET: Atualizar os dados
	DELETE FROM: Excluir os dados
*/

-- INSERÇÃO DE DADOS NA TABELA

INSERT INTO tbl_curso(nome,descricao,carga_horaria) VALUES 
('Analista de dados', NULL, 240),
('Formação python', 'Se torne um desenvolvedor expert em Python', 156),
('Power BI com copilot', 'Aprenda a criar dashboards interativos com IA', 40);

SELECT * FROM tbl_curso;

INSERT INTO tbl_aluno(nome,sobrenome,idade,telefone,cpf,data_nascimento) VALUES
--('Gabriel', 'Gomes', 21, '85999247249', '66403877472', '040209' ),
('Jeremias', 'Do mousse', 18, '8599324942', '72846258912', '060722'),
('ana', 'Gomes', 26, '8599729932', '67349859281', '990209' ),
('maria', 'Da Silva', 72, '8599925625', '98532865412', '530722'),
('joão', 'Do gás', 43, '8599445443', '02638564832', '820722')

SELECT * FROM tbl_aluno;

-- Alterar idade da maria de 2053 para 1953
UPDATE tbl_aluno
SET data_nascimento = '19530722'
WHERE id_aluno = 5; -- Condição para alterar apenas uma linha (crucial!)






