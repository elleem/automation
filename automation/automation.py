from rich.console import Console
# from rich.prompt import Prompt
# from rich.table import Table
import shutil
# import re
import os


def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"folder '{folder_name} created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")



def handle_deleted_user(username):

    os.chdir("../assets")

    user_folder = f"user-docs/{username}"
    temp_folder = "temporary-folder"

    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    files = os.listdir(user_folder)

    for file in files:
        file_path = os.path.join(user_folder, file)
        temp_file_path = os.path.join(temp_folder, file)
        shutil.move(file_path, temp_file_path)

    print (f"Successfully moved {len(files)} from {user_folder} to {temp_folder}.")

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
    deleted_user = "user2"
    handle_deleted_user(deleted_user)
    console = Console()
    main()