from Check import Check
import os

class Extractor:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.check = Check(root_dir)

    def extract_content(self):
        content = []
        for dirpath, dirnames, filenames in os.walk(self.root_dir):
            dirnames[:] = [d for d in dirnames if not self.check.is_hidden(os.path.join(dirpath, d))]
            for file in sorted(filenames):
                full_path = os.path.join(dirpath, file)

                if self.check.is_hidden(full_path) or self.check.is_in_ignore(full_path) or self.check.is_binary(full_path):
                    continue

                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        file_content = f.read()
                    content.append(f"\n--- {os.path.relpath(full_path, self.root_dir)} ---\n{file_content}")
                except Exception as e:
                    content.append(f"\n--- {os.path.relpath(full_path, self.root_dir)} ---\n[ERROR: {e}]")
        return content
