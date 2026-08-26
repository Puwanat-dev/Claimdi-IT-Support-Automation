class TestInputClass:
    def __init__(self):
        self.x = input("Input the x Value: ")  

    def print_x(self):
        print(self.x)



if __name__ == "__main__":
    printer = TestInputClass()
    printer.print_x()
