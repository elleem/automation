## Project: Automation

Author: Lauren Main

Version 1.0

### Links and Resources

### Overview

#### Feature

- [x] Automate the creation of a folder. <br>
    write a script to create a new folder with a specified name


- [x] Handle a deleted user. <br>
    user2 is a deleted user and needs to move their docs from their folder to a temp folder. <br>
    Create a temporary folder, in order to delete the user from the system while maintaining a record of their documents. <br>

- [x] Sort documents into appropriate folders.<br> 
    Go through a given folder and sort docs into additional folders based on their file type.<br>
    Move log files into a `logs` folder. If folder doesn't exist, your script will create one.<br>
    Move email files into a `mail` folder. if folder doesn't exist, your script will create one.<br>

- [x] Parse a log file for errors and warnings.<br>
    After you have moved the `logs` files into the `logs` folder, now parse the log file for errors and warnings.<br>
    Create two separate log files in a target directory.<br>
    `errors.log`: contains all error messages<br>
    `warnings.log`: contains all warning messages<br>

- [x] Create a menu-driven application<br>
    Give the user a list of automation tasks (1-4) and let them choose to execute. <br>
    Customize your app by incorporating an additional automation task: <br>
        count the number of specific file types in a directory <br>
        rename files based on a specific pattern    <br>
        automatically back up specific folders <br>

### To initialize

`python3.11 -m venv .venv`

`source .venv/bin/activate`

`python automation.py`


### Tests