from receipt_of_inquiries.receiver import receiv
from receipt_of_inquiries.console_input import get_appeal
def main():
    while True:
        receiv(get_appeal())
    pass

#def menu():
    # print("Добро пожаловать в программу для хранения, обработки и анализа обращений пользователей.\n")
    # print(f'''Выберите действие:
    # 1 - просмотр списка обращений;
    # 2 - формирование аналитического отчета;
    # 3 - поиск и фильтрация данных;''')
    #
    # choice = int(input())


if __name__ == '__main__':
    main()
