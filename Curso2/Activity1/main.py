from Activity1.Calculator import Calculator

c = Calculator()


def menu():
    print(" ")
    print("CALCULATOR")
    print(" ")
    print("Select an option: ")
    print("1-Addition")
    print("2-Subtraction")
    print("3-Exit")
    print(" ")
    return int(input("Write the option number: "))


while True:
    option = menu()

    if option >= 3:
        break

    else:
        a = int(input("Write the first number to calculate: "))
        b = int(input("Write the first number to calculate: "))

        if option == 1:
            c.addition(a, b)
        elif option == 2:
            c.subtraction(a, b)
        else:
            print("Wrong option.")

print("Goodbye")
