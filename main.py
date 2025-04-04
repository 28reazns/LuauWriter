import sys, os
import importlib.util
import subprocess
from src.generator import write_template
# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
requirements_path = os.path.join(script_dir,"requirements.txt")

# Try different encodings
required_modules = []
encodings = ["utf-8", "utf-16", "utf-32", "ISO-8859-1"]
for enc in encodings:
    try:
        with open(requirements_path, "r", encoding=enc) as f:
            required_modules = [line.strip().split("==")[0] for line in f.readlines() if line.strip()]
        break  # Stop trying if we read successfully
    except UnicodeDecodeError:
        continue  # Try the next encoding

# check if modules installed
missing_modules = []
for module in required_modules:
    try:
        __import__(module)
    except ModuleNotFoundError:
        missing_modules.append(module)

# notify user of missing modules
if missing_modules and not getattr(sys,'frozen',False): #skip check if EXE
    for module in missing_modules:
        print(f"Module {module} is missing. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Clear the output screen after installation
    if sys.platform == "win32":  # For Windows
        os.system("cls")
    else:  # For macOS/Linux
        os.system("clear")

def main():
    fileName = input("Enter luau file name: ")
    fileDescription = input("Enter file description: ")
    write_template(fileName,fileDescription)

if __name__ == "__main__":
    main()