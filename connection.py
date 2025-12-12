import os, psycopg as pg
from dotenv import load_dotenv


''' Este arquivo será responsável por fazer a conexão com o banco de dados.'''

#Carregar as variáveis variáveis de ambiente do arquivo .env
load_dotenv()

user = os.getenv('DATABASE_USER')
password = os.getenv('DATABASE_PASSWORD')
address = os.getenv('DATABASE_ADDRESS')
port = os.getenv('DATABASE_PORT')
dbname = os.getenv('DATABASE_NAME')

def connect():
    '''<h4> Retorna a conexão com o banco de dados </h4>'''
    try:
        connection = pg.connect(f"user={user} password={password} host={address} port={port} dbname={dbname}")
        print('log: Banco de dados conectados com sucesso')
        
        return connection
    except Exception as e:
        print('error: ', e )
        return None