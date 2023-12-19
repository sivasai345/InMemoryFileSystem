# filesystem.py

import os
import json

class InMemoryFileSystem:
    def __init__(self):
        """
        Initialize an in-memory file system.
        """
        self.current_path = '/'
        self.file_system = {}

    def mkdir(self, directory_name):
        path = os.path.join(self.current_path, directory_name)
        if path not in self.file_system:
            # Creating an empty dictionary to represent the new directory
            self.file_system[path] = {}
        else:
            print(f"Directory '{directory_name}' already exists.")

    def cd(self, path):
        if path == '/':
            self.current_path = '/'
        elif path == '..':
            self.current_path = os.path.dirname(self.current_path)
        else:
            self.current_path = os.path.join(self.current_path, path)

    def ls(self, path="."):
        target_path = os.path.join(self.current_path, path)
        if target_path in self.file_system and isinstance(self.file_system[target_path], dict):
            contents = list(self.file_system[target_path].keys())
            print("\n".join(contents))
        else:
            print("Directory not found.")

    def touch(self, file_name):
        file_path = os.path.join(self.current_path, file_name)
        print(f"Debug: Attempting to create file at {file_path}")
        if file_path not in self.file_system:
            self.file_system[file_path] = ""
        else:
            print(f"File '{file_name}' already exists.")

    def echo(self, text, file_name):
        file_path = os.path.join(self.current_path, file_name)
        if file_path in self.file_system:
            self.file_system[file_path] = text
        else:
            print(f"File '{file_name}' not found.")

    def cat(self, file_name):
        file_path = os.path.join(self.current_path, file_name)
        if file_path in self.file_system:
            print(self.file_system[file_path])
        else:
            print(f"File '{file_name}' not found.")

    def mv(self, source, destination):
        source_path = os.path.join(self.current_path, source)
        dest_path = os.path.join(self.current_path, destination)
        if source_path in self.file_system:
            self.file_system[dest_path] = self.file_system.pop(source_path)
        else:
            print(f"Source '{source}' not found.")

    def cp(self, source, destination):
        source_path = os.path.join(self.current_path, source)
        dest_path = os.path.join(self.current_path, destination)
        if source_path in self.file_system:
            self.file_system[dest_path] = self.file_system[source_path]
        else:
            print(f"Source '{source}' not found.")

    def rm(self, target):
        target_path = os.path.join(self.current_path, target)
        if target_path in self.file_system:
            if isinstance(self.file_system[target_path], dict) and bool(self.file_system[target_path]):
                print(f"Directory '{target}' is not empty. Use 'rm -r' to remove non-empty directories.")
            else:
                self.file_system.pop(target_path)
        else:
            print(f"Target '{target}' not found.")

    def grep(self, pattern, file_name):
        file_path = os.path.join(self.current_path, file_name)
        if file_path in self.file_system:
            content = self.file_system[file_path]
            lines = content.split('\n')
            matching_lines = [line for line in lines if pattern in line]
            print("\n".join(matching_lines))
        else:
            print(f"File '{file_name}' not found.")

    def save_state(self, path):
        with open(path, 'w') as f:
            json.dump({'current_path': self.current_path, 'file_system': self.file_system}, f)

    def load_state(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
            self.current_path = data['current_path']
            self.file_system = data['file_system']

    def exit(self):
        print("Exiting the in-memory file system.")
        exit()
