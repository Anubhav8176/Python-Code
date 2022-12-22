import art
print(art.logo)


def add(n1, n2):
    result = n1+n2
    return result


def sub(n1, n2):
    result = n1-n2
    return result


def multiplication(n1, n2):
    result = n1*n2
    return result


def division(n1, n2):
    result = n1/n2
    return result


operation = {
    "+":add,
    "-":sub,
    "*":multiplication,
    "/":division
}
answer = 0
calculate = True
num1 = float(input("What is the first number? "))
while calculate == True:
    for symbol in operation:
        print(symbol)

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the second number? "))

    #Dictionary is used for calling the function
    calculation_function = operation[operation_symbol]
    answer = calculation_function(num1, num2)
    # if operation_symbol == "+":
    #     result = add(result, num2)
    # elif operation_symbol == "-":
    #     result = sub(result, num2)
    # elif operation_symbol == "*":
    #     result = multiplication(result, num2)
    # elif operation_symbol == "/":
    #     result = division(result, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    any_player = input(f"Type 'yes' to calaulate with {answer}, or type 'no' to quit.\n")
    if any_player == "no":
        calculate = False
        print(f"answer is {answer}")
    elif any_player == "yes":
        num1 = answer