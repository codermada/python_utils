from os import getcwd
class File:
    def __init__(self, name):
        self.name = getcwd() + "/" + name
        self.file = open(self.name, 'w')
    def write(self, text):
        self.file.write(text)
        self.file.close()
    def read(self):
        with open(self.name, 'r') as f:
            return f.read()
    def append(self, text):
        with open(self.name, 'a') as f:
            return f.write(text)
file = File("test")
file.write("hey")
file.append("hey")
print(file.read())
print(getcwd())
