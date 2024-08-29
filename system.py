import os
import shutil

class FileManager:
    def __init__(self, root_dir):
        self.current_dir = os.path.abspath(root_dir)
    
    def list_directory(self):
        print(f"\nCurrent directory: {self.current_dir}")
        with os.scandir(self.current_dir) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(f"[DIR]  {entry.name}")
                else:
                    print(f"       {entry.name}")
    
    def change_directory(self, dir_name):
        new_path = os.path.join(self.current_dir, dir_name)
        if os.path.isdir(new_path):
            self.current_dir = new_path
            print(f"Changed directory to {self.current_dir}")
        else:
            print(f"Directory {dir_name} does not exist.")
    
    def create_directory(self, dir_name):
        path = os.path.join(self.current_dir, dir_name)
        try:
            os.makedirs(path)
            print(f"Directory {dir_name} created.")
        except FileExistsError:
            print(f"Directory {dir_name} already exists.")
    
    def delete_directory(self, dir_name):
        path = os.path.join(self.current_dir, dir_name)
        try:
            shutil.rmtree(path)
            print(f"Directory {dir_name} deleted.")
        except FileNotFoundError:
            print(f"Directory {dir_name} does not exist.")
    
    def create_file(self, file_name, content=""):
        path = os.path.join(self.current_dir, file_name)
        with open(path, 'w') as file:
            file.write(content)
            print(f"File {file_name} created.")
    
    def read_file(self, file_name):
        path = os.path.join(self.current_dir, file_name)
        try:
            with open(path, 'r') as file:
                print(f"\nContent of {file_name}:")
                print(file.read())
        except FileNotFoundError:
            print(f"File {file_name} does not exist.")
    
    def write_to_file(self, file_name, content):
        path = os.path.join(self.current_dir, file_name)
        with open(path, 'a') as file:
            file.write(content)
            print(f"Content written to {file_name}.")
    
    def delete_file(self, file_name):
        path = os.path.join(self.current_dir, file_name)
        try:
            os.remove(path)
            print(f"File {file_name} deleted.")
        except FileNotFoundError:
            print(f"File {file_name} does not exist.")
    
    def copy_file(self, src_file_name, dest_file_name):
        src_path = os.path.join(self.current_dir, src_file_name)
        dest_path = os.path.join(self.current_dir, dest_file_name)
        try:
            shutil.copy(src_path, dest_path)
            print(f"File {src_file_name} copied to {dest_file_name}.")
        except FileNotFoundError:
            print(f"Source file {src_file_name} does not exist.")
    
    def move_file(self, src_file_name, dest_file_name):
        src_path = os.path.join(self.current_dir, src_file_name)
        dest_path = os.path.join(self.current_dir, dest_file_name)
        try:
            shutil.move(src_path, dest_path)
            print(f"File {src_file_name} moved to {dest_file_name}.")
        except FileNotFoundError:
            print(f"Source file {src_file_name} does not exist.")
    
    def rename_file(self, old_name, new_name):
        old_path = os.path.join(self.current_dir, old_name)
        new_path = os.path.join(self.current_dir, new_name)
        try:
            os.rename(old_path, new_path)
            print(f"File {old_name} renamed to {new_name}.")
        except FileNotFoundError:
            print(f"File {old_name} does not exist.")
    
    def start(self):
        print("Simple File Manager")
        while True:
            command = input("\nEnter command: ").strip().split()
            if not command:
                continue
            cmd = command[0].lower()
            args = command[1:]
            
            if cmd == "exit":
                print("Exiting File Manager.")
                break
            elif cmd == "ls":
                self.list_directory()
            elif cmd == "cd" and args:
                self.change_directory(args[0])
            elif cmd == "mkdir" and args:
                self.create_directory(args[0])
            elif cmd == "rmdir" and args:
                self.delete_directory(args[0])
            elif cmd == "touch" and args:
                self.create_file(args[0])
            elif cmd == "cat" and args:
                self.read_file(args[0])
            elif cmd == "write" and len(args) >= 2:
                self.write_to_file(args[0], ' '.join(args[1:]))
            elif cmd == "rm" and args:
                self.delete_file(args[0])
            elif cmd == "cp" and len(args) == 2:
                self.copy_file(args[0], args[1])
            elif cmd == "mv" and len(args) == 2:
                self.move_file(args[0], args[1])
            elif cmd == "rename" and len(args) == 2:
                self.rename_file(args[0], args[1])
            else:
                print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    root_directory = os.getcwd()  # Начальная директория — текущая рабочая директория
    manager = FileManager(root_directory)
    manager.start()
