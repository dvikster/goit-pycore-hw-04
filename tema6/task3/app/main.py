import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama
init(autoreset=True)

def visualize_directory(path, indent=0):
    # Отримання об'єкта Path
    directory = Path(path)
    
    if not directory.exists() or not directory.is_dir():
        print(Fore.RED + f"Шлях не існує або не є директорією: {path}")
        return

    # Перебір елементів директорії
    for item in directory.iterdir():
        # Визначення відступу
        print(" " * indent, end="")

        if item.is_dir():
            print(Fore.BLUE + f"📂 {item.name}")  # Виведення директорій
            visualize_directory(item, indent + 4)  
        else:
            print(Fore.GREEN + f"📜 {item.name}")  # Виведення файлів

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Використання: python task3/app/main.py task3/app/folder")
        sys.exit(1)

    directory_path = sys.argv[1]
    visualize_directory(directory_path)

