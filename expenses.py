import time

try:
    username = input("Enter an username:")

    fhand = open(username + ".txt", "r")
    text = fhand.read()
    now = time.strftime("%x")
    while True:
        n = input("Enter a command (for quick entry use -p.)(-help for usage instructions):")
        if n == "new entry":
            add = str(input("Please write the items name and value:)"))
            if len(add) > 2:  # length needs to be at least 3.
                output_file = open("output" + username +".txt", "a")
                output_file.write("Name: " + add + " " + now +" \n")
                print("Added.")
                output_file.close()
        elif n.startswith("-p"):
                output_file = open("output" + username +".txt", "a")
                output_file.write("Name: " + n[3:] + " " + now +" \n")
                print("Added.")
                output_file.close()
        elif n.startswith("-help"):
                fhand2 = open("help.txt", "r")
                help = fhand2.read()
                print(help)
        elif n.startswith("reset"):
                confirmation = input("Are you sure? Y/N  ")
                if confirmation == "y":
                    output_file = open("output" + username +".txt", "w")
                    output_file.write("")
                    print("Done.")
                    output_file.close()
                else:
                    pass
        elif n.startswith("exit"):
            raise SystemExit
        elif n == "report":
            report = open("output" + username +".txt", "r")
            final = report.read()
            capitalized = final.title()
            words = final.split()
            l = []
            for word in words:
                if word[0].isdigit() and word[2] != "/":
                    l.append(int(word))

            print(capitalized, "\n", "\n")
            print("Total spent: CAD ", sum(l))

except:
    print("Terminating")
    raise SystemExit


