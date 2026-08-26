import tkinter as tk
from tkinter import simpledialog # นำเข้าป๊อปอัปรับค่า

class TestInputClass:
    def __init__(self, parent_window = None):
        # สร้าง Dialog เด้งขึ้นมาถามบน GUI แทนการใช้ input()
        self.x = simpledialog.askstring(
            "Input Window", "Input the x Value:", parent=parent_window
        )

    def print_x(self):
        if self.x is not None:
            print(self.x)



if __name__ == "__main__":
    printer = TestInputClass()
    printer.print_x()
