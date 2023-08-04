from film import Film

name = input("Name: ")
if name:
    print(f"The name you input is {name}")

class produce():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def printValues(self):
        print(f"{self.x} and {self.y}")
        self.run()

    def run(self):
        print("Welcome")

timmy = produce(9, 10)

timmy.printValues()

film1 = Film("Avengers", "123hfh")

film1.printDetails()