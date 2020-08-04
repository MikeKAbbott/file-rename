import os
import pathlib
import re

class Rename:
    
    def __init__(self):
        self.directory = self.get_current_directory()
        self.files = [item for item in self.directory.iterdir()]
        self.commands = {
            "pwd": self.directory,
            "ls": self.list_files,
            "h": self.help_menu,
            "help": self.help_menu,
            "rn":self.rename_file,
            "rename":self.rename_file,
            "rn -r":self.rename_multi_files,
            "rename -r":self.rename_multi_files
        }

    def main_menu(self) -> None:
        user_input = ""
        while user_input != "quit" and user_input != "q":
            user_input = self.get_user_input("Enter Command: ")

            if user_input in self.commands:
                if user_input == "pwd":
                    print(self.commands[user_input])
                else:
                    self.commands[user_input]()
       

    def help_menu(self) -> None:
        menu = "HELP MENU: \n"
        commands = ["pwd - list current directory",
        "ls - list all files in current directory",
        "rn,rename - rename a file",
        "rn -r, rename -r - rename multiple files"]
        for command in commands:
            menu += command + "\n"
        print(menu)

    def list_files(self):
        for filename in self.files:
            print(filename.name)

    def get_current_directory(self) -> object:
        current_path = pathlib.Path((pathlib.Path().absolute()))
        return current_path

    def get_user_input(self,text:str) -> str:
        return input(text)

    def rename_multi_files(self) -> None:
        file_change = self.get_user_input("Bulk files to change, new file name: ")
        file_change = file_change.split(",")
        regex = file_change[0]
        new_file_name = file_change[1]
        pattern = re.compile(regex)
        for item in self.files:
            file_name = str(item.name)
            if pattern.search(file_name):
                new_name = re.sub(pattern,new_file_name,file_name)
                os.rename(item, new_name)
                print("File {old_name} renamed to {new_name}".format(old_name = file_name, new_name = new_name))     

    def rename_file(self) -> None:
        file_change = self.get_user_input("file to rename, new file name: ")
        file_change = file_change.split(",")
        current_name = file_change[0]
        new_name = file_change[1]
        os.rename(current_name,new_name)
        print("File {current_name} renamed to {new_name}".format(current_name=current_name,new_name=new_name))


if __name__ == "__main__":
    rename = Rename()
    rename.main_menu()