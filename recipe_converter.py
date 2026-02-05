def cups_to_grams(cups, conversion_rate):

    return cups*conversion_rate

def tablespoons_teaspoons(tablespoons):

    return tablespoons*3

def grams_cups(grams, conversion_rate):

    return grams/conversion_rate

def recipe_converter():

    print("\nWelcome to the recipe converter \n--------------------------------------------")

    while True:

        print("\nChoose an option:")

        print("1) Convert cups to grams\n2) Convert tablespoons to teaspoons\n3) Convert grams to cups\n4) Exit")

        choice=input("Enter your choice(1-4): ")

        if choice == "1":

            cups=float(input("Enter the number of cups: "))

            conversion_rate=float(input("Enter the grams per cup for the ingredient: "))

            result=cups_to_grams(cups,conversion_rate)

            print("Result: {:.2f} grams".format(result))
        
        elif choice == "2":

            tablespoons=float(input("Enter the number of tablespoons: "))

            result = tablespoons_teaspoons(tablespoons)

            print("Result: {:.2f} teaspoons".format(result))

        elif choice == "3":

            grams=float(input("Enter the number of grams: "))

            conversion_rate=float(input("Enter the grams per cup for the ingredient: "))

            result=grams_cups(grams,conversion_rate)

            print("Result: {:.2f} cups".format(result))

        elif choice == "4":

            print("Thank you for using recipe converter, goodbye.")

            break

        else:
            print("Invalid choice, please try again")


recipe_converter()
