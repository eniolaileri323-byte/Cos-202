# Mathematical Calculator

while True:
    print("\n===== MATHEMATICAL CALCULATOR =====")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("// Integer Division")
    print("^  Power")
    print("%  Modulus")
    print("C  Clear")
    print("OFF Exit")

    choice = input("Enter operation: ").upper()

    if choice == "OFF":
        print("Calculator OFF")
        break

    elif choice == "C":
        print("Screen Cleared")
        continue

    elif choice in ["+", "-", "*", "/", "//", "^", "%"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "+":
            print("Answer =", num1 + num2)

        elif choice == "-":
            print("Answer =", num1 - num2)

        elif choice == "*":
            print("Answer =", num1 * num2)

        elif choice == "/":
            if num2 != 0:
                print("Answer =", num1 / num2)
            else:
                print("Division by zero is not allowed.")

        elif choice == "//":
            if num2 != 0:
                print("Answer =", num1 // num2)
            else:
                print("Division by zero is not allowed.")

        elif choice == "^":
            print("Answer =", num1 ** num2)

        elif choice == "%":
            if num2 != 0:
                print("Answer =", num1 % num2)
            else:
                print("Division by zero is not allowed.")

    else:
        print("Invalid operation!")