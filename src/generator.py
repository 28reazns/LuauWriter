import datetime,textwrap
from src.config import DEFAULT_AUTHOR,DATE_FORMAT

# writing files
def write_template(fileName,fileDesc):
    date = datetime.datetime.now().strftime(DATE_FORMAT)
    template = f"""
--!strict
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

    with open(f"templates/{fileName}.lua","w") as file:
        file.write(template)
    
    print(f"Template 'templates/{fileName}.lua' has been written.")
    