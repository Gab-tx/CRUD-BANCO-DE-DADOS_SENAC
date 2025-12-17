from datetime import datetime as dt
from app.exceptions import exceptions as ex

#Função para converter data para padrão yyyy-mm-dd

def convert_date(date:str, date_format='%d/%m/%Y'):
    #Retorna uma data no padrão yyyy-mm-dd
    try:
        date_obj = dt.strptime(date.strip(), date_format)
        return date_obj.strftime('%Y-%m-%d')
    
    except ValueError as e:
        print(f'Data Inválida: {date}. Formato esperado {date_format}')

    except Exception as e:
        print(f'Error: {e}')