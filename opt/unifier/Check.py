import os

class Check:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.gitignore_patterns = self._load_ignore_file(".gitignore")
        self.unifier_ignore_patterns = self._load_ignore_file(".unifier.ignore")

    def _load_ignore_file(self, filename):
        ignore_file = os.path.join(self.root_dir, filename)
        if not os.path.exists(ignore_file):
            return []
        try:
            with open(ignore_file, "r", encoding="utf-8") as f:
                return [line.strip() for line in f if line.strip() and not line.startswith("#")]
        except Exception as e:
            print(f"Ошибка при чтении {filename}: {e}")
            return []

    def is_in_ignore(self, path):
        """Проверяет, находится ли путь в .gitignore или .unifier.ignore"""
        rel_path = os.path.relpath(path, self.root_dir)
        return any(self._match_pattern(rel_path, pattern) for pattern in self.gitignore_patterns + self.unifier_ignore_patterns)

    def _match_pattern(self, path, pattern):
        """Сопоставляет путь с шаблоном"""
        if pattern.endswith("/"):  # Директория
            return path.startswith(pattern.rstrip("/"))
        return path == pattern or path.startswith(pattern + "/")

    def is_hidden(self, path):
        """Проверяет, является ли файл или директория скрытым"""
        return os.path.basename(path).startswith(".")

    def is_binary(self, filepath):
        """Определяет, является ли файл бинарным"""
        try:
            with open(filepath, 'rb') as f:
                chunk = f.read(1024)  # Читаем первые 1024 байта
            if b'\0' in chunk:
                return True
            text_characters = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(32, 127)))
            non_text_bytes = sum(byte not in text_characters for byte in chunk)
            return non_text_bytes / len(chunk) > 0.3
        except Exception:
            return True
