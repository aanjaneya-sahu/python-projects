file = open("example.txt","w")



file.write("Hello World\n")

file.write("This is a sample file")



file.close()

file = open("example.txt","r")

current_content = file.read()

print("File content:\n",current_content)

file.close()

with open("data.txt","w") as file:

    file.write("Line 1:\n")

with open("data.txt","a") as file:

    file.write("Line 2:\n") 

with open("data.txt","r") as file:

    print(file.read())

file = open("birthday.txt","w")

file.write("Happy birthday\nmay god bless you")


file = open("birthday.txt","r")
print(file.read())

file.close()



