# Unifier

Unifier is a Python-based utility that generates a detailed textual representation of a directory structure and extracts the content of files in a project. It is designed to respect `.gitignore` and `.unifier.ignore` files, skip hidden files and directories, and avoid processing binary files.

## Features

- **Directory Tree Generation:** Produces a tree-like structure of the project directory.
- **File Content Extraction:** Reads and outputs the content of files in the directory.
- **Ignore Rules:** Supports `.gitignore` and `.unifier.ignore` for customizable exclusion.
- **Binary File Detection:** Automatically skips binary files to avoid unnecessary resource usage.
- **Hidden Files Handling:** Skips hidden files and directories unless explicitly allowed (e.g., `.gitignore`).

## Requirements

- Python 3 or higher.

## Installation

1. Download .deb fie from releases.
2. `apt install ./unifier.deb` to install package.

After installation, the utility can be run using the `unifier` command.

## Usage

### Command-line Usage

To run the utility:
```bash
unifier [directory]
```

- If no directory is specified, the utility will use the current working directory.
- The output will be saved in a file named `unite_<timestamp>.txt`.

### Output Example

The output includes:
1. A tree representation of the directory structure.
2. The content of files.

Example:
```
Project: /path/to/project

--- Directory Tree ---
├── file1.txt
├── dir1
│   └── file2.txt
└── file3.txt

--- File Contents ---
--- file1.txt ---
<content of file1.txt>

--- dir1/file2.txt ---
<content of file2.txt>
```

## Configuration

You can customize the behavior of the utility using two files:
- `.gitignore`: Standard gitignore rules.
- `.unifier.ignore`: Custom rules specific to this utility.

### `.unifier.ignore` Example

```
# Ignore temporary files
*.tmp

# Ignore specific directories
logs/
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## Contact

For questions, suggestions, or support, contact [8hoursking](mailto:insanitykape@gmail.com) or create an issue.