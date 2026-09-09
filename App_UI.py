import tkinter as tk
from TestInputClass import TestInputClass


class App_UI(tk.Tk): 
    def __init__(self, image_pack_start_process = None): #เริ่มต้นสร้างหน้าต่างหลักของแอปพลิเคชัน / image_pack_start_process รับค่า call back
        super().__init__() 
        self.title("Simple Page Switch") 
        self.geometry("300x200") 
        self.configure(bg="#f5f5f5")

        self.image_pack_start_process = image_pack_start_process  #Call back

        #สร้างคอนเทนเนอร์กลาง สำหรับวางเนื้อหา
        self.container = tk.Frame(self, bg="#f5f5f5")
        self.container.pack(fill="both", expand=True) # fill = "both" ขยายเต็มพื้นที่ทั้งแกน X และ Y, expand = True สามารถยืดขนาดได้

        #สั่งให้โชว์หน้า home เป็นหน้าแรก
        self.show_page("home")


    def show_page(self, page_name): #ลบ widget เก่า แล้วสร้างอันใหม่
            for widget in self.container.winfo_children(): #.winfo_children() คืนค่าลิสต์ของวิดเจ็ตทั้งหมดที่อยู่ในคอนเทนเนอร์
                widget.destroy()
    
            if page_name == "home":
                self.create_home_page()
            elif page_name == "reply_email":
                self.create_reply_email_page()
            elif page_name == "zip_complete":
                self.create_zip_complete_page()

    def run_image_packer(self):
         # หากมีการส่งฟังก์ชันจัดการมาจาก main ให้ทำงาน
        if self.image_pack_start_process:
            success = self.image_pack_start_process(self) # ส่ง self ไปเพื่อให้ Input_Window เกาะหน้าต่างหลักได้
            if success:
                self.show_page("zip_complete") # ทำงานสำเร็จค่อยเปลี่ยนหน้า
        else:
            print("No action defined!")

    

    def create_home_page(self):
                label = tk.Label(self.container, text="Claimdi Automate 0.1", font=("Arial", 14))
                label.pack(pady=(30, 10)) #ย่อมาจาก padding y-axis คือการกำหนด ระยะห่างในแนวตั้ง (บน-ล่าง)

                reply_email_button = tk.Button(
                    self.container,
                    text="Reply Email",
                    command= lambda: self.show_page("reply_email"),  
                     width=20,
                    height=2,
                )
                reply_email_button.pack()

                ins_pic_button = tk.Button(
                    self.container,
                    text="Get Ins Pic",
                    command=self.run_image_packer,  
                    width=20,
                    height=2,
                )
                ins_pic_button.pack()


    def create_reply_email_page(self):
            label = tk.Label(self.container, text="Reply Email", font=("Arial", 16, "bold"))
            label.pack(expand=True)
    
            back_button = tk.Button(self.container, text="Back", command=lambda: self.show_page("home"))
            back_button.pack(pady=10)
    

    def create_zip_complete_page(self):
        label = tk.Label(self.container, text="Zip Complete!", font=("Arial", 16, "bold"))
        label.pack(expand=True)

        back_button = tk.Button(self.container, text="Back", command=lambda: self.show_page("home"))
        back_button.pack(pady=10)


if __name__ == "__main__":
    app = App_UI()
    app.mainloop()
