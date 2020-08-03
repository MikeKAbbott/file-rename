import os
import pathlib
import re


def print_menu() -> None:
    current_directory = get_current_directory()
    user_input = ""
    while user_input != "quit" and user_input != "q":
        user_input = get_user_input("Enter Command: ")
        
        if user_input == "pwd":
            print(current_directory)
        
        if user_input == "ls":
            for filename in current_directory.iterdir():
                print(filename.name)
        
        if user_input == "h" or user_input == "help":
            help_menu()
        
        if user_input == "rn" or user_input == "rename":
            change = input("file to rename, new file name: ")
            change = change.split(",")
            current = change[0]
            new = change[1]
            rename_file(current,new)

        if user_input == "rn -r" or user_input == "rename -r":
            change = input("common file name theme, new file name: ")
            change = change.split(",")
            common_file_name = change[0]
            new_file_name = change[1]
            rename_multi_files(common_file_name,new_file_name)          

    
def help_menu() -> None:
    menu = "HELP MENU: \n"
    commands = ["pwd - list current directory",
    "ls - list all files in current directory",
    "rn,rename - rename a file",
    "rn -r, rename -r - rename multiple files"]
    for command in commands:
        menu += command + "\n"
    print(menu)
    

def get_current_directory() -> object:
    current_path = pathlib.Path((pathlib.Path().absolute()))
    return current_path

def get_user_input(text:str) -> str:
    return input(text)

def rename_multi_files(regex:str, new_file_name:str) -> None:
    pattern = re.compile(regex)
    for item in get_current_directory().iterdir():
        file_name = str(item.name)
        if pattern.search(file_name):
            new_name = re.sub(pattern,new_file_name,file_name)
            os.rename(item, new_name)
            print("File {old_name} renamed to {new_name}".format(old_name = file_name, new_name = new_name))

            

def rename_file(current_name:str, new_file_name:str) -> None:
    os.rename(current_name,new_file_name)
    print("File {current_name} renamed to {new_file_name}".format(current_name=current_name,new_file_name=new_file_name))


if __name__ == "__main__":
   print_menu()