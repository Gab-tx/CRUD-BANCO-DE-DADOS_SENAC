from querys import *

def format_findAllStudents() -> str:

    for i in find_all_students():
        print(f'''| Id: {i[0]}| Nome: {i[1]} {i[2]} | Idade: {i[3]} | Telefone: {i[4]} | CPF: {i[5]} | Data Nascimento: {i[6]} |''')
        

def main():
    insert_student('Manoel','Gomes', 56, '85999223343', '12345678911','1969-12-02')

    format_findAllStudents()

    delete_many_students_by_id(list=[1,3,4])

    format_findAllStudents()

if __name__ == '__main__':
    main()    