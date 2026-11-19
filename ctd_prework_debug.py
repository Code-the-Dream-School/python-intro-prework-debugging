# Movie ticket price calculator
# This script asks for the user's name and age, then prints the ticket price.
# Children under 12 pay the discount price.
# Adults 65 or older also pay the discount price.
# Everyone else pays the full price.

full_price = 12
discount_price = 8

name = input("What is your name? ")
age = input("How old are you? ")

if age < 12:
    price = discount_price
    ticket_type = "child"
elif age > 65
    price = discount_price
    ticket_type = "senior"
else:
    price = full_price
    ticket_type = "adult"

print("Hello,", name)
print("Your", ticket_type, "ticket costs", prise, "dollars.")
