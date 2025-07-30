def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("=== Basic Python Calculator ===")
    operations = {
        '1': ('Add', add),
        '2': ('Subtract', subtract),
        '3': ('Multiply', multiply),
        '4': ('Divide', divide),
        'q': ('Quit', None)
    }

    while True:
        print("\nSelect operation:")
        for key in operations:
            print(f"{key}. {operations[key][0]}")

        choice = input("Enter your choice: ").strip().lower()

        if choice == 'q':
            print("Goodbye!")
            break
        elif choice not in operations:
            print("Invalid choice. Try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        operation_name, operation_func = operations[choice]
        result = operation_func(num1, num2)
        print(f"\nResult of {operation_name.lower()}ing {num1} and {num2}: {result}")

if __name__ == "__main__":
    main()
