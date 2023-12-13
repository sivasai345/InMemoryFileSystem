# main.py

from filesystem import InMemoryFileSystem
from cli import CommandLineInterface

if __name__ == "__main__":
    file_system = InMemoryFileSystem()
    cli = CommandLineInterface(file_system)
    cli.run()
