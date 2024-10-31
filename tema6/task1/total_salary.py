def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file: #встановлення кодування при відкриті файлів utf-8
            salaries = []
            
            for line in file:
                line = line.strip()  # Видаляємо пробіли і символи нового рядка, розділяємо за комою
                if line: # Переконуємося, що рядок не порожній
                    name, salary = line.strip().split(',')
                    salaries.append(float(salary)) #обираємо float при переведені зп з рядка в число, бо можуть бути копійки
                
            total = sum(salaries)
            average = total / len(salaries)
            return total, average

    except FileNotFoundError: #Опрацювуємо вийняток при роботі з файлами, такий як відсутність файлу.
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return 0, 0
    

# Приклад використання функції - файл поміщенно в папку salary для прикладу пошуку шляху для нього
total, average = total_salary("task1/salary/salary_file.txt") 
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

