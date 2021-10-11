print("lets know how much time you are left with until we all met in heaven!")
age = int(input("What is your current age?\n"))
name = input("what is your name?\n")
years_remaining = 77 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = "Hey " +name+", "+f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.\nMake every second count and live it to the fullest😀"
print(message)