def the_biggest_search_keys(*keys):
    if not keys:  # Если нет ключей
        return "''"

    max_length = max(len(key) for key in keys)  # Находим максимальную длину
    max_keys = sorted([key for key in keys if len(key) == max_length])  # Сортируем по алфавиту

    # Форматируем вывод с кавычками
    return ", ".join(f"'{key}'" for key in max_keys)