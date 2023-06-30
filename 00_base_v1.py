# functions go here

# checks if the name is blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank it outputs an error
        if response == "":
            print("Sorry, this can't be blank. Please try again")
        else:
            return response


# checks users enter an integer to a given question\
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter a normal number?!?!?!?")


# calc the price
def calc_ticket_price(var_age):
    # ticket is 7.50 for under 16yos
    if var_age < 16:
        price = 7.5

    # tickets is 10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # ticket price is 6.5 for 65+
    else:
        price = 6.5

    return price


# checks that users enter a valid response (e.g. yes / no
# cash/credit) based on the list of options
def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0], valid_responses[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)


# main routine starts here

# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

# lists
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
# Ask user if they want to see my instructions
want_instructions = string_checker("Do you want the instructions? (Y/N): ", 1, yes_no_list)

if want_instructions == "yes":
    print("Instructions go here")

print()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("Please enter your name or 'xxx' to quit: ")

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

    # calc the ticket price
    ticket_cost = calc_ticket_price(age)

    # get payment method
    pay_method = string_checker("Choose a payment method (cash / credit): ", 2, payment_list)

    tickets_sold += 1

# output the amount of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congrats you have sold all the tickets!")
else:
    print("You have sold {} ticket/s. There is {} ticket/s "
          "remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
