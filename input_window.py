import tkinter as tk
from tkinter import simpledialog # นำเข้าป๊อปอัปรับค่า

class Input_Window:
    def __init__(self, parent_window = None):
        # สร้าง Dialog เด้งขึ้นมาถามบน GUI แทนการใช้ input()
        self.pic_path = simpledialog.askstring(
            "Input Window", "Input the Picture Path:", parent=parent_window
        )

    def getPath(self):
        if self.pic_path is not None:
            return self.pic_path
        else:
            return None

if __name__ == "__main__":
    printer = Input_Window()
    print(printer.getPath())
