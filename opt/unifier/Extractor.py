import os

class Extractor:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def extract_content(self):
        content = []
        for dirpath, dirnames, filenames in os.walk(self.root_dir):
            # Исключаем скрытые директории
            dirnames[:] = [d for d in dirnames if not d.startswith('.')]
            for file in sorted(filenames):
                if not file.startswith('.') or file == ".gitignore":
                    filepath = os.path.join(dirpath, file)
                    if not self._is_binary(filepath):
                        try:
                            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                                file_content = f.read()
                            content.append(f"\n--- {os.path.relpath(filepath, self.root_dir)} ---\n{file_content}")
                        except Exception as e:
                            content.append(f"\n--- {os.path.relpath(filepath, self.root_dir)} ---\n[ERROR: {e}]")
        return content

    def _is_binary(self, filepath):
        """Определяет, является ли файл бинарным"""
        try:
            with open(filepath, 'rb') as f:
                chunk = f.read(1024)  # Читаем первые 1024 байта
            # Если есть NULL-байт, файл считается бинарным
            if b'\0' in chunk:
                return True
            # Проверяем соотношение читаемых символов к нечитаемым
            text_characters = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(32, 127)))
            non_text_bytes = sum(byte not in text_characters for byte in chunk)
            return non_text_bytes / len(chunk) > 0.3  # Если более 30% нечитаемых символов, файл бинарный
        except Exception:
            return True  # Ошибки при чтении файла трактуем как бинарный
