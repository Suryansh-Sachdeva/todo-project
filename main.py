txt = str(input("Choose between 'Add', 'Delete' and 'Change': "))
if txt == "Add":
    add_content = str(input("Enter the command to add: "))
    f = open("Commands.txt", "a")
    f.write(add_content + "\n")
    f.close()
if txt == "Delete":
    def delete_line(filename, line_number):
        with open(filename) as file:
            lines = file.readlines()
        if (line_number <= len(lines)):
            del lines[line_number - 1]
            with open(filename, "w") as file:
                for line in lines:
                    file.write(line)
        elif(len(lines) == 1):
            print("Line", line_number, "not in file.", end=" ")
            print("File has 1 line")
        else:
            print("Line", line_number, "not in file.", end=" ")
            print("File has", len(lines), "lines.")
    delete_filename = "Commands.txt"
    delete_file_number = int(input("Line number: "))
    delete_line(delete_filename, delete_file_number)
if txt == "Change":
    def replace_line(filename, line_number, text):
        with open(filename) as file:
            lines = file.readlines()
        if (line_number <= len(lines)):
            lines[line_number - 1] = text + "\n"
            with open(filename, "w") as file:
                for line in lines:
                    file.write(line)
        elif len(lines) == 1:
            print("Line", line_number, "not in file.", end=" ")
            print("File has 1 line.")
        else:
            print("Line", line_number, "not in file.", end=" ")
            print("File has", len(lines), "lines.")
    filename = "Commands.txt"
    line_number = int(input("Line number: "))
    text = input("Text: ")
    replace_line(filename, line_number, text)