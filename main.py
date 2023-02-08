print("Welcome to the tip calculator!")
customer = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
person = int(input("How many people to split the bill? "))
bill_per_person = customer / person
tip_per_percentage = tip / 100
tip_per_person = bill_per_person * tip_per_percentage
total_bill = bill_per_person + tip_per_person

print(f"Each person should pay: $ {round(total_bill,2)}")

