from os import getcwd

import re
import os

def is_valid_filename(filename):
    if not filename or filename.strip() == "":
        return False

    # No path separators (prevents directory traversal too)
    if "/" in filename or "\\" in filename:
        return False

    # Avoid names that are just dots or spaces
    if filename.strip(". ") == "":
        return False

    # Length check (255 is a safe cross-platform max for a single filename)
    if len(filename) > 255:
        return False

    # Control characters (invalid on most systems)
    if re.search(r'[\x00-\x1f]', filename):
        return False

    # Windows reserved names (still worth blocking cross-platform)
    reserved = {
        "CON", "PRN", "AUX", "NUL",
        *(f"COM{i}" for i in range(1, 10)),
        *(f"LPT{i}" for i in range(1, 10)),
    }
    name_only = os.path.splitext(filename)[0].upper()
    if name_only in reserved:
        return False

    return True

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
