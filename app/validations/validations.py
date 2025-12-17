from app.exceptions.exceptions import *

def validation_age(idade:int):
    '''Validação se a idade corresponde ao limite permitido. 0 - 150'''
    if not (idade > 0 and idade < 150):
        raise AgeException('Idade não corresponde ao limite')

def validation_phone(telefone:str):
    '''Validar se o telefone corresponde ao padrão de 11 digitos'''
    if not (telefone.isdigit() and len(telefone) == 11):
        raise PhoneException('Telefone não corresponde ao padrão')

def validation_cpf(cpf:str):
    '''Validar se o cpf corresponde ao padrão de 11 digitos'''
    if not (cpf.isdigit() and len(cpf) == 11):
        raise CpfException('Cpf não corresponde ao padrão')

def validation_date(date:str):
    '''Validar a data de nascimento'''
    date_format = date.split('-')
    length_date_month = len(date_format[1])
    length_date_year = len(date_format[0])
    length_date_day = len(date_format[2])

    if length_date_year > 4 or length_date_year < 2:
        raise DateException('formato de data errado. Padrão correto (yyyy-mm-dd)')

    elif  length_date_month != 2:
        raise DateException('formato de data errado. Padrão correto (yyyy-mm-dd)')
    
    elif  length_date_day != 2:
        raise DateException('formato de data errado. Padrão correto (yyyy-mm-dd)')
    
    if date.isdigit():
        raise DateException('Digite números')
    

