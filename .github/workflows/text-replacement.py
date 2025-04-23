#In this script, I've learned to import files into IDLE, allow the program to read it, and, learn on replacing text from witin the same string. The numbered process goes as below:
def main():
    filename = 'learning_python.txt'

    # 1. Read the whole file and print its contents
    with open(filename, 'r') as file:
        contents = file.read()
    print("=== Entire File ===")
    print(contents)

    # 2. Loop over the file object
    print("\n=== Looping Over File Object ===")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

    # 3. Store lines in a list and print outside the with block
    print("\n=== Reading Lines into a List ===")
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        print(line.strip())

    # 4. Replace 'Python' with 'PHP' and print each modified line
    print("\n=== Replacing 'Python' with 'PHP' ===")
    for line in lines:
        modified = line.replace('Python', 'PHP')
        print(modified.strip())


if __name__ == '__main__':
    main()
