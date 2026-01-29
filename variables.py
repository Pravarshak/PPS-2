a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("-" * 30)

print(f"Addition       : {a + b:.2f}")
print(f"Subtraction    : {a - b:.2f}")
print(f"Multiplication : {a * b:.2f}")

if b != 0:
    print(f"Division       : {a / b:.2f}")
else:
    print("Division       : Not possible (division by zero)")

print("-" * 30)

print(f"Square of {a}   : {a ** 2:.2f}")
print(f"Square of {b}   : {b ** 2:.2f}")

if a >= 0:
    print(f"Sq. Root of {a} : {a ** 0.5:.2f}")
else:
    print(f"Sq. Root of {a} : Not a real number (negative input)")

if b >= 0:
    print(f"Sq. Root of {b} : {b ** 0.5:.2f}")
else:
    print(f"Sq. Root of {b} : Not a real number (negative input)") 

#output 
Enter first number: 55
Enter second number: 17
------------------------------
Addition       : 72.00
Subtraction    : 38.00
Multiplication : 935.00
Division       : 3.24
------------------------------
Square of 55.0   : 3025.00
Square of 17.0   : 289.00
Sq. Root of 55.0 : 7.42
Sq. Root of 17.0 : 4.12

=== Code Execution Successful ===
