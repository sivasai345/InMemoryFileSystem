# cli.py

class CommandLineInterface:
    def __init__(self, file_system):
        self.file_system = file_system

    def run(self):
        while True:
            command = input(f"{self.file_system.current_path}> ").strip().split(" ", 1)
            if command[0] == 'exit':
                self.file_system.exit()
            elif command[0] == 'save_state':
                if len(command) > 1:
                    self.file_system.save_state(command[1])
                else:
                    print("Usage: save_state <path>")
            elif command[0] == 'load_state':
                if len(command) > 1:
                    self.file_system.load_state(command[1])
                else:
                    print("Usage: load_state <path>")
            else:
                operation = getattr(self.file_system, command[0], None)
                if operation is not None and callable(operation):
                    try:
                        operation(*command[1].split())
                    except TypeError:
                        print("Invalid arguments for the operation.")
                else:
                    print("Invalid command.")
