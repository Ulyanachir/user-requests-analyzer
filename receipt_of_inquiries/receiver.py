from analysis.classifier import *
#на вход подается текст.Создаем database.models.py объект ticket.
# Проверяем его категорию
def receiv(appeal):
    if appeal.category is None:
        appeal.category = definition_by_categories(appeal.message)
    else:
        appeal.category = test_category(appeal.category,definition_by_categories(appeal.message))