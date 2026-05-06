from os import getcwd

import re
def is_valid_filename(filename):
    if not filename or filename.strip() == "":
        return False

    # Forbidden characters (Windows-safe rule set)
    forbidden_chars = r'[<>:"/\\|?*]'
    if re.search(forbidden_chars, filename):
        return False
    
    # Avoid names that are just dots or spaces
    if filename.strip(". ") == "":
        return False
    
    # Length check (common filesystem limit)
    if len(filename) > 255:
        return False
    
    return True

import os
def is_readable_writable_dir(path):
    return (
        os.path.isdir(path) and
        os.access(path, os.R_OK) and   # readable
        os.access(path, os.W_OK)       # writable
    )

class File:
    def __init__(self, dir, name):
        self.name = dir + "/" + name
        self.isValid = is_valid_filename(name) and is_readable_writable_dir(dir)
    def write(self, text):
        if (not self.isValid):
            return
        with open(self.name, 'w') as f:
            f.write(text)
    def read(self):
        if (not self.isValid):
            return
        with open(self.name, 'r') as f:
            return f.read()
    def append(self, text):
        if (not self.isValid):
            return
        with open(self.name, 'a') as f:
            return f.write(text)

file = File(getcwd(), "test")
file.write("hey")
file.append("hey")
print(file.read())
print(getcwd())
