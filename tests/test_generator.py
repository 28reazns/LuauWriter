import os
from src.generator import write_template

def test_write():
    file_name = "test_script"
    description = "this is a script for testing purposes."
    write_template(file_name,description)

    assert os.path.exists(f"{file_name}.lua"), "File was not created."

if __name__ == "__main__":
    test_write()