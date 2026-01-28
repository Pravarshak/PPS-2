age = int(input("Please enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print(f"You must wait {18 - age} more years to vote.")
