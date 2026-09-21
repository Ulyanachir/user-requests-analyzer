def definition_by_categories(message):
    # Category(таблица
    # в
    # БД)
    # ├── id
    # ├── name(название)
    # └── keywords(ключевые
    # слова)
    #
    # classifier.py
    # ├── читает
    # Category
    # из
    # БД
    # ├── разбирает
    # keywords
    # └── ищет
    # совпадения
    # в
    # тексте
    ...

def test_category(category, new_category):
    if category != new_category:
        return new_category
    return category