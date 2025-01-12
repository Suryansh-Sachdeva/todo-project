from datetime import datetime
while (2+2 == 4):   
    now = datetime.now()
    t_string = now.strftime("%H:%M")
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    txt = str(input("Choose between 'Add', 'Delete', 'Change' and 'View by date': "))
    if txt == "Add":
        add_content = str(input("Enter the command to add: "))
        f = open("Commands.txt", "a")
        f.write(dt_string + "  |  " + add_content + "\n")
        f.close()
    elif txt == "Delete":
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
    elif txt == "Change":
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
        date = input("Enter the date: ")
        line_number = int(input("Line number: "))
        text = date + " " + t_string + "  |  " + input("Text: ")
        replace_line(filename, line_number, text)
    elif txt == "View by date":
        filename = "Commands.txt"
        search_date = input("Enter the date: ")
        with open(filename, 'r') as file:
            line_number = 0
            i = 0
            for line in file:
                line_number += 1
                if search_date in line:
                    print(line_number, line. strip())
                    i = 1
            if i == 0:
                print("No command having such date")
    else:
        print("No such command")