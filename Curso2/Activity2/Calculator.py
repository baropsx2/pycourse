import sys


class Calculator:
    # Constructor
    def __init__(self):
        self.a = int(input("Write the first number to calculate: "))
        self.b = int(input("Write the second number to calculate: "))

    # Addition method
    def addition(self):
        print("The result of the sum between " + str(self.a) + " and " + str(self.b) + " is : " + str(self.a + self.b))
        sys.exit(print("Goodbye"))

    # Subtraction method
    def subtraction(self):
        print("The result of subtraction between " + str(self.a) + " and " + str(self.b) + " is : " + str(
            self.a - self.b))
        sys.exit(print("Goodbye"))


