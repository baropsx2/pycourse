from Activity2.Calculator import Calculator

c = Calculator()


# Calculator menu
def menu():
    print(' ')
    print('Select an option to calculate the values: ')
    print('1 - Addition')
    print('2 - Subtraction')
    print('3 - Exit')
    print(' ')
    return int(input("Write the option number: "))


while True:
    option = menu()

    if option >= 3:
        break

    else:
        if option == 1:
            c.addition()
        elif option == 2:
            c.subtraction()
        else:
            print("Wrong option.")

print("Goodbye")
