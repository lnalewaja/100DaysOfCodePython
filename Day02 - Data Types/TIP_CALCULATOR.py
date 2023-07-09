print("Welcome to the tip calculator.")

total_bill = float(input("What is the total bill? $"))
percentage_tip = float(input("What percentage tip would you like to give? %"))
total_people = float(input("How many people to split the bill? "))

total_bill = total_bill + (total_bill * (percentage_tip / 100))
final_amount = total_bill / total_people
final_amount = format(final_amount, ".2f")

print(f"Each person should pay: ${final_amount}")
