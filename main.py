from src.generator import write_template

def main():
    fileName = input("Enter luau file name: ")
    fileDescription = input("Enter file description: ")
    write_template(fileName,fileDescription)

if __name__ == "__main__":
    main()