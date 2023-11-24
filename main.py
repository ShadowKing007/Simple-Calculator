# Author: Shaik Ibrahim Shariff
# Date: 2023-11-23
# Description: Simple calculator program that performs arithmetic operations based on user input.
# Change log:
#   - Initial version
#   - Added support for user-specified arithmetic operations with any number of operands and BODMAS/BIDMAS rules

def apply_operator(operators, operands, op):
    while op in operators:
        index = operators.index(op)
        operators.pop(index)
        left_operand = operands.pop(index)
        right_operand = operands.pop(index)
        if op == '+':
            result = left_operand + right_operand
        elif op == '-':
            result = left_operand - right_operand
        elif op == '*':
            result = left_operand * right_operand
        elif op == '/':
            # Handling division by zero
            if right_operand != 0:
                result = left_operand / right_operand
            else:
                print("Error: Division by zero. Please enter a non-zero divisor.")
                return None
        operands.insert(index, result)
    return operands[0]

def calculate_expression(components):
    operators = ['+', '-', '*', '/']

    # Performing multiplication and division first
    for op in ['*', '/']:
        result = apply_operator(components[1], components[0], op)
        if result is None:
            return None

    # Performing addition and subtraction next
    for op in ['+', '-']:
        result = apply_operator(components[1], components[0], op)
        if result is None:
            return None

    return result

def calculator():
    user_input = input("Enter expression (e.g., 2 + 3 * 4 / 2, 5 - 2): ")

    try:
        # Splitting the input into numbers and operators
        components = user_input.replace(' ', '')
        components = [c if c in ['+', '-', '*', '/'] else float(c) for c in components]

        # Separating numbers and operators
        operands = [components[i] for i in range(0, len(components), 2)]
        operators = [components[i] for i in range(1, len(components), 2)]

        # Calculating the expression based on BODMAS/BIDMAS rules
        result = calculate_expression([operands, operators])
        if result is not None:
            print("Entered expression:", user_input)
            print("Result:", result)
        else:
            print("Error in calculation.")

    except (ValueError, TypeError, IndexError):
        print("Invalid input. Please enter a valid expression.")

calculator()
