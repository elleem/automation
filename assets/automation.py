from rich.console import Console
from rich.prompt import Prompt
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
    folder_to_sort = os.path.join(base_directory, "user-docs", user_folder)

    temp_folder = os.path.join(base_directory, "temporary-folder")
    files_in_temp = os.listdir(temp_folder)

    if user_folder == "user2" and files_in_temp:
        print("Files already in temporary-folder. Sorting without moving.")
        sort_documents(temp_folder)
    else:
        print("Sorting files in user2 folder.")
        sort_documents(folder_to_sort)
else:
    print("Invalid user directory. Please try again.")


def parse_errors(log_file_path, target_directory):
    if not os.path.exists(log_file_path):
        print(f"Log file '{log_file_path}' does not exist.")
        return
    errors_log = os.path.join(target_directory, "errors.log")
    warnings_log = os.path.join(target_directory, "warnings.log")

    with open (log_file_path, "r") as file:
        for line in file:
            if "error" in line.lower():
                with open(errors_log, "a") as errors_file:
                    errors_file.write(line)
            elif "warning" in line.lower():
                with open(warnings_log, "a") as warnings_file:
                    warnings_file.write(line)
    print ("Log file parsed successfully")


def rename_files(directory, old_name, new_name):
    files = os.listdir(directory)
    renamed_files = 0

    for file in files:
        if file == old_name:
            old_file_path = os.path.join(directory, file)
            new_file_path = os.path.join(directory, new_name)
            os.rename(old_file_path, new_file_path)
            renamed_files += 1
    print(f"Renamed {renamed_files} file(s) from {old_name} to {new_name}.")

def main():
    """Main function to run the CLI app
    input: user input
    return: None
    """

    while True:
        console.print("\n1. Create folder\n2. Delete user\n3.Sort documents\n4.Parse error logs\n5. Rename files")
        choice = Prompt.ask("Choose a task(Enter the number)", choices=['1','2','3','4','5','6'], default='6')

        if choice =='1':
            folder_name = Prompt.ask("Enter the folder name")
            create_folder(folder_name)
        elif choice =='2':
            username = Prompt.ask("Enter the username to handle the deleted user")
            handle_deleted_user(username)
        elif choice == '3':
            folder_path = Prompt.ask("Enter the folder path to sort documents")
            sort_documents(folder_path)
        elif choice == '4':
            log_file_path = Prompt.ask("Enter the log file path")
            target_directory = Prompt.ask("Enter the target directory to save the parsed logs")
            parse_errors(log_file_path,target_directory)
        elif choice == '5':
            directory = Prompt.ask("Enter the directory path to rename the files")
            old_name = Prompt.ask("Enter the old file name")
            new_name = Prompt.ask("Enter the new file name")
            rename_files(directory, old_name, new_name)

        elif choice == '6':
            break

        else:
            console.print("Invalid choice. Please try again.")



if __name__ == "__main__":
    console = Console()
    main()