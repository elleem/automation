from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
import shutil
import re
import os


def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        console.print(f"[pink3]folder '{folder_name}' created successfully.[/pink3]")
    except FileExistsError:
        console.print(f"[pink3]Folder '{folder_name}' already exists.[/pink3]")



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

    console.print (f"[orange3]Successfully moved {len(files)} from {user_folder_path} to {temp_folder}.[/orange3]")

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

    console.print(f"[green4]Documents sorted into new file extension folders in {folder_path}.[/green4]")


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
    console.print ("[deep_sky_blue1]Log file parsed successfully![/deep_sky_blue1]")


def rename_files(directory, old_name, new_name):
    files = os.listdir(directory)
    renamed_files = 0

    for file in files:
        if file == old_name:
            old_file_path = os.path.join(directory, file)
            new_file_path = os.path.join(directory, new_name)
            os.rename(old_file_path, new_file_path)
            renamed_files += 1
    console.print(f"[purple]Renamed {renamed_files} file(s) from {old_name} to {new_name}.[/purple]")

def main():
    """Main function to run the CLI app
    input: user input
    return: None
    """

    while True:
        console.print("\n[pink3]1. Create folder[/pink3]\n[orange3]2. Delete user[/orange3]\n[green4]3. Sort documents[/green4]\n[deep_sky_blue1]4. Parse error logs[/deep_sky_blue1]\n[purple]5. Rename files[/purple]")
        choice = Prompt.ask("Choose a menu number. Selecting 6 will exit the program.)", choices=['1','2','3','4','5','6'])

        if choice =='1':
            folder_name = Prompt.ask("[pink3]Enter the folder name[/pink3]")
            if os.path.exists(folder_name):
                console.print("[red]Folder already exists. Please choose a different folder name[/red]")
            else:
                create_folder(folder_name)
        elif choice =='2':
            username = Prompt.ask("[orange3]Enter the username to handle the deleted user[/orange3]")
            if not os.path.exists(username):
                console.print("[red]Username does not exist in the file structure. Please try another username.[/red]")
            else:
                handle_deleted_user(username)
        elif choice == '3':
            folder_path = Prompt.ask("[green4]Enter the folder path to sort documents[/green4]")
            if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
                console.print("[red]Invalid folder path. Please try again.[/red]")
            else:
                sort_documents(folder_path)
        elif choice == '4':
            log_file_path = Prompt.ask("[deep_sky_blue1]Enter the log file path[/deep_sky_blue1]")
            target_directory = Prompt.ask("[deep_sky_blue1]Enter the target directory to save the parsed logs[/deep_sky_blue1]")
            if not os.path.isfile(log_file_path) or not os.path.exists(target_directory) or not os.path.isdir(target_directory):
                console.print("[red]Invalid log file path or target directory. Please try another entry.[/red]")
            else:
                parse_errors(log_file_path,target_directory)
        elif choice == '5':
            directory_path = Prompt.ask("[purple]Enter the directory path to rename the files:[/purple]")
            old_name = Prompt.ask("[purple]Enter the old file name:[/purple]")
            new_name = Prompt.ask("[purple]Enter the new file name:[/purple]")
            rename_files(directory_path, old_name, new_name)

        elif choice == '6':
            break

        else:
            console.print("[red]Invalid choice. Please try again.[/red]")



if __name__ == "__main__":
    console = Console()
    main()