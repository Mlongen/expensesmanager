


username = input("Enter an username:") # I will insert try and except to safeguard a wrong username(I had this already but removed for a few reasons)

fhand = open(username + ".txt", "r")
text = fhand.read()

while True:
    n = input("Enter a command (for quick entry use -p):")
    if n == "new entry":
        add = str(input("Please write the items name and value:)"))
        if len(add) > 2:  # length needs to be at least 3.
            output_file = open("output.txt", "a")
            output_file.write(add + " \n")
            print("Added.")
            output_file.close()
    elif n == "report":
        report = open("output.txt", "r")
        final = report.read()
        print(final)



