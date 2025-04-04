import sys
import os
import shutil

import datetime,textwrap,os,json

#get directory 
script_dir = os.path.dirname(os.path.abspath(__file__))

# default configs
default_config = {
    "author": "Default Author",
    "date-format": "%m/%d/%Y"
}

# Get the path to the config.json in AppData (or other location depending on platform)
def get_config_path():
    if getattr(sys, 'frozen', False):  # If running as an executable
        # Check if the config is already in AppData, otherwise copy it there
        appdata_path = os.path.join(os.getenv('APPDATA'), 'LuauWriter', 'config.json')
        if not os.path.exists(appdata_path):
            # Copy the bundled config.json to AppData if it doesn't exist
            config_path = os.path.join(sys._MEIPASS, 'config.json')
            shutil.copy(config_path, appdata_path)  # Copy the bundled file to AppData
        return appdata_path
    else:
        # If running as a regular Python script, use the same directory as the script
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')

# load the config
with open(get_config_path(), "r") as f:
    config = json.load(f)

DEFAULT_AUTHOR = config["author"]
DATE_FORMAT = config["date-format"]

# writing files
def write_template(fileName,fileDesc):
    if getattr(sys,'frozen',False): # check if EXE
        try:
            os.mkdir(os.path.join(os.getenv('APPDATA'), 'LuauWriter',"Templates"))
        finally:
            filePath = os.path.join(os.getenv('APPDATA'), 'LuauWriter',"Templates",f"{fileName}.lua")
    else:
        filePath = f"templates/{fileName}.lua"
    date = datetime.datetime.now().strftime(DATE_FORMAT)
    template = f"""--!strict
--[[
    {fileName}.lua
    Author: {DEFAULT_AUTHOR}
    Created: {date}
    Last Modified: {date}
----------------------------------------------
    {textwrap.fill(text=fileDesc,width=50,subsequent_indent="   ")}
]]

-- Services

-- Modules

-- Variables

-- Functions and Bindables

-- Setup
"""

    with open(filePath ,"w") as file:
        file.write(template)
    
    print(f"{filePath}' has been written.")
    