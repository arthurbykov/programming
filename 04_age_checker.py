# function goes here
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter a normal number that everyone uses?!?!?!?")


# main routine goes here
tickets_sold = 0

while True:
    name = input("Enter your name or type 'xxx' to quit")
    if name == "xxx":
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("sorry ur too young")
        continue
    else:
        print("that looks like a type?")
        continue

tickets_sold += 1
