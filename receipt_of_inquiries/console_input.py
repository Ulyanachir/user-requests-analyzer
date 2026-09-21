from database.models import Ticket

def get_appeal():
    category = input("Bведите категорию(финансы/техника).Для автоматического определения оставьте поле пропущенным: ")
    message = input("Введите обращение")
    appeal = Ticket (message=message, category=category)
    return appeal