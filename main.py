from datetime import datetime
while (2+2 == 4):   
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    txt = str(input("Choose between 'Add', 'Delete', 'Change' and 'View By Date': "))
    if txt == "Add":
        add_content = str(input("Enter the command to add: "))
        f = open("Commands.txt", "a")
        f.write(dt_string + "  |  " + add_content + "\n")
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
        text = dt_string + "  |  " + input("Text: ")
        replace_line(filename, line_number, text)
    if txt == "View by date":
        filename = "Commands.txt"
        search_date = input("Enter the date: ")
        with open(filename, 'r') as file:
            i = 0
            for line in file:
                if search_date in line:
                    print(line. strip())
                    i = 1
                elif i == 0:
                    print("No command having such date")
                    break