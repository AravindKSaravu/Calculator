def Calculator():
    try:
        print("Welcome to the calculator")
        num1 = int(input("Input a number:"))
        operator = "+", "-", "*", "/"
        operator_input = input("The Operator(+,-,*,/):")
        num2 = int(input("Input another number:"))
        if operator_input in operator:
            if operator_input == operator[0]:
                print(num1 + num2, "is the answer😊")
            elif operator_input == operator[1]:
                if num1 > num2:
                    print(num1 - num2, "is the answer😊")
                else:
                    print(num2 - num1, "is the answer😊")
            elif operator_input == operator[2]:
                print(num1 * num2, "is the answer😊")
            elif operator_input == operator[3]:
                print(num1 / num2, "is the answer😊")
        else:
            print("Invalid Operator")
    # except BaseException:
    # print("Invalid!Not an Number!")
    except ZeroDivisionError:
        print("Cannot divide by 0!Invalid Input")
    except ValueError:
        print("Not an number!")


Calculator()
