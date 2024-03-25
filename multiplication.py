num1 = int(input("Enter the number for which you want the multiplication table: "))
num2 = int(input("Enter the limit up to which you want the multiplication table generarted:"))
print(f"Multiplication Table for {num1}:")
for i in range (1, num2 +1):
    product = num1 * i
    print(f"{num1}x{i}={product}")

