#This file is to learn some ways to use decorator function

def tell(f):
    def wrapper():
        print("Welcome the Function is about to Run")
        f()
        print("The function has finished running")

@tell
def cube(x):
    print(f"{x * x * x}")

cube(10)