## Project: Automation

Author: Lauren Main

Version 1.0

### Links and Resources

### Overview

#### Feature

-[] Automate the creation of a folder.
    write a script to create a new folder with a specified name


-[] Handle a deleted user. 
    user2 is a deleted user and needs to move their docs from their folder to a temp folder. 
    Create a temporary folder, in order to delete the user from the system while maintaining a record of their documents. 

-[] Sort documents into appropriate folders. 
    Go through a given folder and sort docs into additional folders based on their file type.
    Move log files into a `logs` folder. If folder doesn't exist, your script will create one.
    Move email files into a `mail` folder. if folder doesn't exist, your script will create one.

-[] Parse a log file for errors and warnings.
    After you have moved the `logs` files into the `logs` folder, now parse the log file for errors and warnings.
    Create two separate log files in a target directory.
    `errors.log`: contains all error messages
    `warnings.log`: contains all warning messages

-[] Create a menu-driven application
    Give the user a list of automation tasks (1-4) and let them choose to execute. 
    Customize your app by incorporating an additional automation task:
        count the number of specific file types in a directory
        rename files based on a specific pattern    
        automatically back up specific folders

### To initialize

`python3.11 -m venv .venv`

`source .venv/bin/activate`

`python automation.py`


### Tests