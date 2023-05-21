from rich.console import Console
from rich.prompt import Prompt
# from rich.table import Table
import shutil
import re
import os


def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"folder '{folder_name}' created successfully.")
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


def parse_errors(log_file_path, target_directory):

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    error_regex = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}, ERROR:.*')
    warning_regex = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}, WARNING:.*')

    with open(log_file_path, 'r') as log_file:
        lines = log_file.readlines()

    errors_log_path = os.path.join(target_directory, "errors.log")
    warnings_log_path = os.path.join(target_directory, "warnings.log")

    with open (errors_log_path, "w") as errors_log_file:
        with open(warnings_log_path, 'w') as warning_log_file:
            for line in lines:
                if re.match(error_regex, line):
                    errors_log_file.write(line)
                elif re.match(warning_regex, line):
                    warning_log_file.write(line)
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
            directory_path = Prompt.ask("Enter the directory path to rename the files")
            old_name = Prompt.ask("Enter the old file name")
            new_name = Prompt.ask("Enter the new file name")
            rename_files(directory_path, old_name, new_name)

        elif choice == '6':
            break

        else:
            console.print("Invalid choice. Please try again.")



if __name__ == "__main__":
    console = Console()
    main()