def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip() # Видаляємо пробіли і символи нового рядка, розділяємо за комою
                if line:  # Переконуємося, що рядок не порожній
                    cat_id, name, age = line.split(',')
                    # Створюємо словник для кожного кота
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats.append(cat_info)
    except FileNotFoundError: #Опрацювуємо вийняток при роботі з файлами, такий як відсутність файлу.
        print("Файл не знайдено. Перевірте шлях до файлу.")

    return cats

# Приклад використання функції
cats_info = get_cats_info("task2/cats_file.txt")
print(cats_info)
