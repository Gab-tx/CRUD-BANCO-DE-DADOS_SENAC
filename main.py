from app.utils.utils import *
        

def lista_estudantes() -> str:

    for i in st.find_all_students():

        print(f'''| Id: {i[0]}| Nome: {i[1]} {i[2]} | Idade: {i[3]} | Telefone: {i[4]} | CPF: {i[5]} | Data Nascimento: {i[6]} |
curso: {course.display_course_by_turma_id(i[8])} |''')        

def main():
    # insert_student('Manoel','Gomes', 56, '85999223343', '12345678911','1969-12-02')

    # lista_estudantes()

    # delete_student_by_Id(50)

    # st.register_course(1,24)

    lista_estudantes()
    # print(course.find_course_by_id(1))

    # print(st.find_all_students())
    
    # update_student('Manoel','Gomes', 56, '85900000000', '12345678911', '02/12/1969', 24)

if __name__ == '__main__':
    main()    