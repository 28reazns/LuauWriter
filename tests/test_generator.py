import os,unittest
from src.generator import write_template

class TestStringMethods(unittest.TestCase):
    def test_write(self):
        file_name = "test_script"
        description = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
        write_template(file_name,description)

        self.assertTrue(os.path.exists(f"templates/{file_name}.lua"), "File was not created.")

if __name__ == "__main__":
    unittest.main()