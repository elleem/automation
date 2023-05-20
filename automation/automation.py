from rich.console import Console
# from rich.prompt import Prompt
# from rich.table import Table
# import shutil
# import re
import os


def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"folder '{folder_name} created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")



def deleted_user():
    pass


def sort_documents():
    pass



def parse_errors():
    pass


def main():
    """Main function to run the CLI app
    input: user input
    return: None
    """




    pass



if __name__ == "__main__":
    new_folder_name = "new_stuff"
    create_folder(new_folder_name)
    console = Console()
    main()