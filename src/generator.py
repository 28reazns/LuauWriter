import datetime
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
    {fileDesc}
    ]]

    -- Services

    -- Modules

    -- Variables

    -- Functions and Bindables

    -- Setup
"""

    with open(f"{fileName}.lua","a") as file:
        file.write(template)
    
    print(f"Template '{fileName}.lua' has been written.")
    