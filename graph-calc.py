import numpy as np
import matplotlib.pyplot as plt
import math

# Allowed math functions for user input
allowed_funcs = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'sqrt': math.sqrt,
    'log': math.log,
    'log10': math.log10,
    'exp': math.exp,
    'pi': math.pi,
    'e': math.e,
    'abs': abs,
    'pow': pow,
}

def safe_eval(expr, x_val):
    """
    Evaluate the expression expr with variable x = x_val,
    allowing only safe functions from allowed_funcs.
    """
    # Define a safe environment dictionary for eval
    safe_dict = allowed_funcs.copy()
    safe_dict['x'] = x_val
    try:
        return eval(expr, {"__builtins__": None}, safe_dict)
    except Exception as e:
        raise ValueError(f"Error evaluating expression at x={x_val}: {e}")

def get_function_input():
    print("Enter a function of x to plot, e.g., sin(x) + x**2")
    print("Allowed functions: sin, cos, tan, sqrt, log, log10, exp, abs, pow")
    print("Use 'x' as the variable.")
    while True:
        expr = input("f(x) = ").strip()
        # Test the expression on a sample value
        try:
            test_val = safe_eval(expr, 1)
            # Check that the result is a number
            if not isinstance(test_val, (int, float)):
                print("The function must return a numeric value.")
                continue
            return expr
        except Exception as e:
            print(f"Invalid function: {e}")
            print("Please try again.")

def get_float(prompt, default=None):
    while True:
        val = input(prompt)
        if val == '' and default is not None:
            return default
        try:
            return float(val)
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("=== Python Graphing Calculator ===")

    expr = get_function_input()
    x_start = get_float("Enter start of x range (default -10): ", default=-10)
    x_end = get_float("Enter end of x range (default 10): ", default=10)

    if x_end <= x_start:
        print("End of range must be greater than start. Using defaults -10 to 10.")
        x_start, x_end = -10, 10

    points = 500
    x_vals = np.linspace(x_start, x_end, points)
    y_vals = []

    print(f"Calculating f(x) for x in [{x_start}, {x_end}]...")

    for x in x_vals:
        try:
            y = safe_eval(expr, x)
            y_vals.append(y)
        except Exception as e:
            # For undefined points (e.g., log(negative)), use NaN to skip plotting
            y_vals.append(np.nan)

    print("Plotting...")

    plt.figure(figsize=(10,6))
    plt.plot(x_vals, y_vals, label=f"f(x) = {expr}")
    plt.title("Graphing Calculator")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
