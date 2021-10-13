print("Welcome to the tip calculator.")
total_bill=int(input("What was the total bill? $"))
total_people=int(input("How many people to split the bill? "))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_bill=((total_bill*tip*0.01)+total_bill)/total_people
print(f"Each person should pay: ${round(split_bill,2)}")
