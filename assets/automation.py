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

    os.chdir("")

    user_folder_path = f"user-docs/{username}"
    temp_folder = "temporary-folder"

    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    files = os.listdir(user_folder_path)

    for file in files:
        file_path = os.path.join(user_folder_path, file)
        temp_file_path = os.path.join(temp_folder, file)
        shutil.move(file_path, temp_file_path)

    print (f"Successfully moved {len(files)} from {user_folder_path} to {temp_folder}.")

def sort_documents(folder_path):
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            _,file_extension = os.path.splitext(file)

            destination_folder = os.path.join(folder_path, file_extension[1:])
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            destination_path = os.path.join(destination_folder, file)
            shutil.move(file_path, destination_path)

    print(f"Documents sorted into appropriate folders in {folder_path}.")

user_directories = ["user1", "user2"]

print("Do you want to sort these user directories by file type?")
for directory in user_directories:
    print(directory)

user_folder = input("Enter the user directory: ")

if user_folder in user_directories:
    base_directory = os.path.dirname(os.path.abspath(__file__))
    folder_to_sort = f"assets/user-docs/{user_folder}"
    sort_documents(folder_to_sort)
else:
    print("Invalid user directory. Please try again.")


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