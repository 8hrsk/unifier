import os
import sys
from datetime import datetime
from TreeBuilder import TreeBuilder
from Extractor import Extractor

def main():
    # Получаем путь директории из аргументов или используем текущую
    root_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

    # Проверяем существование директории
    if not os.path.isdir(root_dir):
        print(f"Ошибка: {root_dir} не является директорией.")
        return

    # Генерация дерева
    tree_builder = TreeBuilder(root_dir)
    tree = tree_builder.build_tree()

    # Извлечение содержимого
    extractor = Extractor(root_dir)
    content = extractor.extract_content()

    # Форматирование результатов
    result = "\n".join([
        f"Проект: {root_dir}",
        "\n--- Структура директории ---\n",
        "\n".join(tree),
        "\n--- Содержимое файлов ---\n",
        "\n".join(content)
    ])

    # Сохранение в файл
    output_file = f"unite_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"Результат сохранён в файл: {output_file}")

if __name__ == "__main__":
    main()
