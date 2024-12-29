# 1.0
 - Standart utility functions. `unifier` to create .txt file.

# 1.1
 - Added .gitignore support by default. All files/directories in .gitignore are ignored automatically. | Use `unifier -g` to disable.
 - Added .unifier.ignore. Works like .gitignore. Ignores files/dirrectories listed in it.
 - Now you can create only a tree or only extract code. | `unifier -t` to create only tree. `unifier -c` to extract code.
 - All validation was moved to a separate file.

# Coming soon
 - ## 1.2
  - Markdown. Text file now is formatted in markdown.
  - HTML support. Text file can be created as HTML document with tags. | Use `unifier -html` to enable.
  - Binary files support. Binary files can be read and extracted. | Use `unifier -b` to enable.

 - ## 1.3
  - Github repos support. You can create a text file from an online repo in github. | Use `unifier -l <LINK>` to enable.
  - Windows build. Unifier windows CLI.