while True:

    filename = input("Enter the name of the file to read/type, or type 'quit' to exit: ")

    if filename.lower()=="quit":

        print("Goodbye")

        break

    try:

        with open(filename, "r") as file:

            content=file.read()

            print(content)

            break

    except FileNotFoundError:

        print("File does not exist.")

        tryagain = input("Would you like to try again (yes, no):  ")

        if tryagain .lower() != "yes":

            print("Thank you for using this programme")

            break

     
    

#print("Welcome to the Python programme that reads content from a file (hopefully)\n---------------------------------------------------------------------------------------")

#file = open ("coolfile.txt","w")

#file.write("This is an awesome file. Cool, isn't it?")

#file.close()

#choice = input("What file do you want to see -  ")

#if choice == "coolfile":

    file = open("coolfile.txt","r")

    current_content = file.read()