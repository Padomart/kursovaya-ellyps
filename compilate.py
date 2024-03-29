import os
import sys

# Получаем путь к каталогу, где находится исполняемый файл
base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

# Путь к файлу JSON
json_file_path = os.path.join(base_path, 'variants/data.json')

print(json_file_path)