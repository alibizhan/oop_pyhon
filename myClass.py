class Cat:
    # class attribute
    species = "Cat"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Cat class
persian = Cat("Persian", 20)
bengal = Cat("Bengal", 16)
birman = Cat("Birman", 15)

# access the class attributes
print("Persian is a {}".format(persian.__class__.species))
print("Bengal is a {}".format(bengal.__class__.species))
print("Birman is a {}".format(birman.__class__.species))

# access the instance attributes
print("{} is {} years old".format(persian.name, persian.age))
print("{} is {} years old".format(bengal.name, bengal.age))
print("{} is {} years old".format(birman.name, birman.age))