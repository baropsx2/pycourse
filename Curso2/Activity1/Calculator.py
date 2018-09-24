import sys


class Calculator:
    def addition(self, a, b):
        print("The result of the sum between " + str(a) + " and " + str(b) + " is : " + str(a + b))
        sys.exit(print("Goodbye"))

    def subtraction(self, a, b):
        print("The result of subtraction between " + str(a) + " and " + str(b) + " is : " + str(a - b))
        sys.exit(print("Goodbye"))
