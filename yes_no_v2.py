# functions go here
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"

        elif response == "n" or response == "no":
            return "no"

        else:
            print("Please enter Y or N")


# main routine goes here
while True:
    want_instructions = yes_no("Do you want the instructions?: ")

    if want_instructions == "yes":
        print("Instructions go here")

    print("program continues...")
    print("We are done")
