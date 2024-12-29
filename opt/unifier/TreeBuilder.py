from Check import Check
import os

class TreeBuilder:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.check = Check(root_dir)

    def build_tree(self):
        tree_lines = []
        self._build_tree(self.root_dir, tree_lines, prefix="")
        return tree_lines

    def _build_tree(self, current_dir, tree_lines, prefix):
        entries = sorted(os.listdir(current_dir), key=lambda e: (not os.path.isdir(os.path.join(current_dir, e)), e.lower()))

        for i, entry in enumerate(entries):
            full_path = os.path.join(current_dir, entry)

            if self.check.is_hidden(full_path) or self.check.is_in_ignore(full_path):
                continue

            connector = "└── " if i == len(entries) - 1 else "├── "
            tree_lines.append(f"{prefix}{connector}{entry}")

            if os.path.isdir(full_path):
                sub_prefix = "    " if i == len(entries) - 1 else "│   "
                self._build_tree(full_path, tree_lines, prefix + sub_prefix)