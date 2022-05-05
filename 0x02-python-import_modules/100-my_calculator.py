#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    if(len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    i = 0
    operator = ["+", "-", "*", "/"]

    while i < 4:
        if operator[i] == argv[2]:
            break
        i += 1

    if i == 4:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator[i] == '+':
        res = add(int(argv[1]), int(argv[3]))
    elif operator[i] == '-':
        res = sub(int(argv[1]), int(argv[3]))
    elif operator[i] == '*':
        res = mul(int(argv[1]), int(argv[3]))
    elif operator[i] == '/':
        res = div(int(argv[1]), int(argv[3]))

    print(f"{argv[1]} {operator[i]} {argv[3]} = {res}")
