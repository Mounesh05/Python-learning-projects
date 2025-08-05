while(True):
    op=input("Enetr the operation(+,-,*,/,%,** and 0 to exit):")
    if(op=="0"):
        break
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    match op:
        case "+":
            print("Result:",a+b)
        case "-":
            print("Result:",a-b)
        case "*":
            print("Result:",a*b)
        case "/":
            if b == 0:
                print("Error: Division by zero")
            else:
                print("Result:", a / b)
        case "%":
            if b == 0:
                print("Error: Modulo by zero")
            else:
                print("Result:", a % b)
        case "**":
            print("Result:",a**b)
        case _:
            print("Enter valid opreator")