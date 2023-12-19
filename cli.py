# cli.py

class CommandLineInterface:
    def __init__(self, file_system):
        self.file_system = file_system

    def run(self):
        while True:
            command = input(f"{self.file_system.current_path}> ").strip().split(" ", 1)
            if not command:
                continue  # Skip empty commands

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
                    args = command[1].split() if len(command) > 1 else []  # Check if there are arguments
                    if command[0] == 'cd':
                        args = [command[1]]  # Ensure 'cd' has one argument (the path)
                    operation(*args)
                else:
                    print("Invalid command.")
