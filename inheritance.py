# parent class
class Cat:
    
    def __init__(self):
        print("This is a Cat")

    def whoisThis(self):
        print("Cat")

# child class
class Siamese(Cat):

    def __init__(self):
        # call super() function
        super().__init__()
        print("This is a Siamese cat")

    def whoisThis(self):
        print("Siamese")

    def jump(self):
        print("Jump high")

siam = Siamese()
siam.whoisThis()
siam.jump()