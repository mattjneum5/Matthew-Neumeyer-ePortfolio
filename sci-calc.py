import math

def get_number(prompt="Enter a number: "):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def factorial(n):
    if n < 0:
        return "Error: Factorial is undefined for negative numbers."
    elif not n.is_integer():
        return "Error: Factorial only works with whole numbers."
    return math.factorial(int(n))

def show_menu():
    print("\n=== Scientific Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Sine (degrees)")
    print("8. Cosine (degrees)")
    print("9. Tangent (degrees)")
    print("10. Logarithm (base 10)")
    print("11. Natural Logarithm (ln)")
    print("12. Factorial")
    print("q. Quit")

def main():
    while True:
        show_menu()
        choice = input("Choose an operation: ").strip().lower()

        if choice == 'q':
            print("Goodbye!")
            break

        try:
            if choice == '1':
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                print(f"Result: {a + b}")
            elif choice == '2':
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                print(f"Result: {a - b}")
            elif choice == '3':
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                print(f"Result: {a * b}")
            elif choice == '4':
                a = get_number("Enter numerator: ")
                b = get_number("Enter denominator: ")
                if b == 0:
                    print("Error: Division by zero.")
                else:
                    print(f"Result: {a / b}")
            elif choice == '5':
                a = get_number("Enter base: ")
                b = get_number("Enter exponent: ")
                print(f"Result: {math.pow(a, b)}")
            elif choice == '6':
                a = get_number("Enter number: ")
                if a < 0:
                    print("Error: Cannot take square root of a negative number.")
                else:
                    print(f"Result: {math.sqrt(a)}")
            elif choice == '7':
                a = get_number("Enter angle in degrees: ")
                print(f"Result: {math.sin(math.radians(a))}")
            elif choice == '8':
                a = get_number("Enter angle in degrees: ")
                print(f"Result: {math.cos(math.radians(a))}")
            elif choice == '9':
                a = get_number("Enter angle in degrees: ")
                print(f"Result: {math.tan(math.radians(a))}")
            elif choice == '10':
                a = get_number("Enter number: ")
                if a <= 0:
                    print("Error: Logarithm only defined for positive numbers.")
                else:
                    print(f"Result: {math.log10(a)}")
            elif choice == '11':
                a = get_number("Enter number: ")
                if a <= 0:
                    print("Error: Natural log only defined for positive numbers.")
                else:
                    print(f"Result: {math.log(a)}")
            elif choice == '12':
                a = get_number("Enter a whole number: ")
                result = factorial(a)
                print(f"Result: {result}")
            else:
                print("Invalid selection. Please choose a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
