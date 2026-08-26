import tkinter as tk
from TestInputClass import TestInputClass


class App_UI(tk.Tk): #สือทอดคลาส tk.Tk 
    def __init__(self): #เริ่มต้นสร้างหน้าต่างหลักของแอปพลิเคชัน
        super().__init__() #เรียกคุณสมบัติของคลาสแม่ (tk.Tk) มายังคลาสนี้
        self.title("Simple Page Switch") 
        self.geometry("300x200") #.geometry() กำหนดขนาดและตำแหน่ง
        self.configure(bg="#f5f5f5")

        #สร้างคอนเทนเนอร์กลาง สำหรับวางเนื้อหา
        self.container = tk.Frame(self, bg="#f5f5f5")
        self.container.pack(fill="both", expand=True) # fill = "both" ขยายเต็มพื้นที่ทั้งแกน X และ Y, expand = True สามารถยืดขนาดได้

        #สั่งให้โชว์หน้า home เป็นหน้าแรก
        self.show_page("home")

    ############################ test ###################################
    def run_test_input(self):
        printer = TestInputClass()  # สร้าง instance (จะถาม input ใน terminal)
        printer.print_x()  # พิมพ์ค่าออกทาง terminal
        self.show_page("hello")  # เปลี่ยนหน้าไปยัง "hello" ต่อทันที
    ############################ test ###################################

    def show_page(self, page_name): #ลบ widget เก่า แล้วสร้างอันใหม่
        for widget in self.container.winfo_children(): #.winfo_children() คืนค่าลิสต์ของวิดเจ็ตทั้งหมดที่อยู่ในคอนเทนเนอร์
            widget.destroy()

        if page_name == "home":
            self.create_home_page()
        elif page_name == "hello":
            self.create_hello_page()

    def create_home_page(self):
                label = tk.Label(self.container, text="Welcome", font=("Arial", 14))
                label.pack(pady=(30, 10)) #ย่อมาจาก padding y-axis คือการกำหนด ระยะห่างในแนวตั้ง (บน-ล่าง)
        
                button = tk.Button(
                    self.container,
                    text="Go to next page",
                    command=self.run_test_input,  # เรียกใช้ฟังก์ชัน run_test_input() เมื่อกดปุ่ม
                    width=20,
                    height=2,
                )
                button.pack()

    def create_hello_page(self):
        label = tk.Label(self.container, text="Hello cQ", font=("Arial", 16, "bold"))
        label.pack(expand=True)

        back_button = tk.Button(self.container, text="Back", command=lambda: self.show_page("home"))
        back_button.pack(pady=10)


if __name__ == "__main__":
    app = App_UI()
    app.mainloop()
