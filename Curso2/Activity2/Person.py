# Person class
class Person:
    # Constructor
    def __init__(self, name):
        self.name = name
        print("Hi, my name is", name)

    # Talk method
    def talk(self, words):
        print(words)

    # Hobby method
    def hobby(self):
        print("My hobby is to watch movies")


# Teacher class - extends from Person class
class Teacher(Person):
    # Constructor
    def __init__(self, name, signature):
        Person.__init__(self, name)
        self.signature = signature

    # Get details method
    def get_details(self):
        return self.name, self.signature

    # Overriding Hobby method 1
    def hobby(self):
        return print("My hobby is to read")

    # Teach method
    def teach(self):
        print(self.name, "is giving", self.signature, "class")


# Engineer Class - extends from Person class
class Engineer(Person):

    # Overriding Hobby method 2
    def hobby(self):
        return print("My hobby is to play video games")


print("Objects creation: ")
print(" ")
# Objects creation
# Person objects
barocio = Person("Javier")
barocio.talk(words="I'm a person ")
barocio.hobby()

print(" ")
# Teacher objects
jocelyne = Teacher("Jocelyne", "sciences")
# jocelyne.signature("Math")
jocelyne.talk(words="I'm a Teacher")
jocelyne.hobby()
jocelyne.teach()

print(" ")
# Engineer objects
carlos = Engineer("Carlos")
carlos.talk(words="I'm a Engineer")
carlos.hobby()
