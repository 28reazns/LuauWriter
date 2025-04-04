# Lua Style Generator

A python script to generate structured Luau script templates easily.

## Features

- Easy to use CLI interface
- Customizable Name/Date
## Installation
- Clone this repository.

## Usage
```bat
python main.py
Enter luau file name: 'fileName'
Enter file description: 'fileDesc'
Template 'templates/fileName.lua' has been written.
```
### Luau File Example:
```luau
--!strict
--[[
    test_script.lua
    Author: Your Name
    Created: 03/30/2025
    Last Modified: 03/30/2025
----------------------------------------------
    Lorem ipsum dolor sit amet, consectetur adipiscing
   elit, sed do eiusmod tempor incididunt ut
   labore et dolore magna aliqua. Ut enim ad minim
   veniam, quis nostrud exercitation ullamco
   laboris nisi ut aliquip ex ea commodo
   consequat. Duis aute irure dolor in
   reprehenderit in voluptate velit esse cillum
   dolore eu fugiat nulla pariatur. Excepteur sint
   occaecat cupidatat non proident, sunt in culpa
   qui officia deserunt mollit anim id est
   laborum.
]]

-- Services

-- Modules

-- Variables

-- Functions and Bindables

-- Setup

```

## Building (Compiling to .exe)
Using PyInstaller, run:
```python
python -m PyInstaller --onefile --icon=icon.ico --name="Luau Writer" --add-data "src/config.json;." --add-data "requirements.txt;." main.py
```
A build will be provided, however.

## How to edit Config.
1. Find `%AppData%/Roaming/LuauWriter`
2. Find `config.json`
3. Change `Default Author` in: 
    ```json 
        "author": "Default Author"
    ```
    to whatever you'd like. *(You can also edit date-format)*
4. Save your changes, and next time you create a template, it will use the information input there.