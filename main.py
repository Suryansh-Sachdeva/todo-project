txt = str(input("Choose between 'Add', 'Delete' and 'Change': "))
if txt == "Add":
    add_content = str(input("Enter the command to add: "))
    f = open("Commands.txt", "a")
    f.write(add_content + "\n")
    f.close()