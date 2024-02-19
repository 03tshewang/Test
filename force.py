print("Newton's Second Law of Motion")
print("-----------------------------------------------------------------")

print("Select the missing value")
print("1. Force(f)")
print("2. Mass(m)")
print("3. Acceleration(a)")
missing_value = input("Enter the missing value option number: ")

if missing_value == "1":
    m = float(input("Enter the value of mass: "))
    a = float(input("Enter the value of acceleration: "))
    f = m * a
    print(f"The force is {f}")

elif missing_value == "2":
    f = float(input("Enter the value of force: "))
    a = float(input("Enter the value of acceleration: "))
    m = f / a
    print(f"The mass is {m}")

elif missing_value == "3":
    f = float(input("Enter the value of force: "))
    m = float(input("Enter the value of mass: "))
    a = f / m
    print(f"The acceleration is {a}")

else:
    print("Invalid option selected")
