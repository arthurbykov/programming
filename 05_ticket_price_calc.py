# Calculate the ticket price based on the age
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


# loop for testing
while True:

    # Get age
    age = int(input("Age: "))

    # calc ticket cost
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, Ticket Price: ${:.2f}".format(age, ticket_cost))
