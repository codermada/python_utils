from os import getcwd

class File:
    def __init__(self, dir, name):
        self.name = dir + "/" + name
    def write(self, text):
        with open(self.name, 'w') as f:
            f.write(text)
    def read(self):
        with open(self.name, 'r') as f:
            return f.read()
    def append(self, text):
        with open(self.name, 'a') as f:
            return f.write(text)

file = File(getcwd(), "test")
file.write("hey")
file.append("hey")
print(file.read())
print(getcwd())
