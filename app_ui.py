import tkinter as tk


class AppUI(tk.Tk): 
    def __init__(self,text_reply_start_process = None, mail_reply_start_process = None, image_pack_start_process = None, policy_ui_start_process = None): #เริ่มต้นสร้างหน้าต่างหลักของแอปพลิเคชัน / image_pack_start_process รับค่า call back
        super().__init__() 
        self.title("Simple Page Switch") 
        self.geometry("300x250") 
        self.configure(bg="#f5f5f5")

        self.text_reply_start_process = text_reply_start_process  #Text reply call back
        self.mail_reply_start_process = mail_reply_start_process  #Mail reply call back
        self.image_pack_start_process = image_pack_start_process  #Image packer call back
        self.policy_ui_start_process = policy_ui_start_process  #Policy UI call back

        #สร้างคอนเทนเนอร์กลาง สำหรับวางเนื้อหา
        self.container = tk.Frame(self, bg="#f5f5f5")
        self.container.pack(fill="both", expand=True) # fill = "both" ขยายเต็มพื้นที่ทั้งแกน X และ Y, expand = True สามารถยืดขนาดได้

        #สั่งให้โชว์หน้า home เป็นหน้าแรก
        self.show_page("home")


    def show_page(self, page_name): 
            #ลบ widget เก่า แล้วสร้างอันใหม่
            for widget in self.container.winfo_children(): #.winfo_children() คืนค่าลิสต์ของวิดเจ็ตทั้งหมดที่อยู่ในคอนเทนเนอร์
                widget.destroy()
    
            if page_name == "home":
                self.create_home_page()
            elif page_name == "text_reply":
                self.create_text_reply_page()
            elif page_name == "reply_email":
                self.create_reply_email_page()
            elif page_name == "zip_complete":
                self.create_zip_complete_page()
            elif page_name == "policy_ui_home":
                self.create_policy_ui_home_page()


    def run_text_reply(self):
            # หากมีการส่งฟังก์ชันจัดการมาจาก main ให้ทำงาน
            if self.text_reply_start_process:
                success = self.text_reply_start_process(self) # ส่ง self ไปเพื่อให้ Input_Window เกาะหน้าต่างหลักได้
                if success:
                    self.show_page("text_reply") # ทำงานสำเร็จค่อยเปลี่ยนหน้า
            else:
                print("No action defined!") 

    def run_mail_reply(self):
        # หากมีการส่งฟังก์ชันจัดการมาจาก main ให้ทำงาน
        if self.mail_reply_start_process:
            success = self.mail_reply_start_process(self) # ส่ง self ไปเพื่อให้ Input_Window เกาะหน้าต่างหลักได้
            if success:
                self.show_page("reply_email") # ทำงานสำเร็จค่อยเปลี่ยนหน้า
        else:
            print("No action defined!")            

    def run_image_packer(self):
         # หากมีการส่งฟังก์ชันจัดการมาจาก main ให้ทำงาน
        if self.image_pack_start_process:
            success = self.image_pack_start_process(self) # ส่ง self ไปเพื่อให้ Input_Window เกาะหน้าต่างหลักได้
            if success:
                self.show_page("zip_complete") # ทำงานสำเร็จค่อยเปลี่ยนหน้า
        else:
            print("No action defined!")

    def open_policy_ui(self):   
        if self.policy_ui_start_process:
            success = self.policy_ui_start_process(self) # ส่ง self ไปเพื่อให้ Input_Window เกาะหน้าต่างหลักได้
            if success:
                self.show_page("policy_ui_home") # ทำงานสำเร็จค่อยเปลี่ยนหน้า
        else:
            print("No action defined!")

    

    def create_home_page(self):
                label = tk.Label(self.container, text="Claimdi Support 1.1", font=("Arial", 14))
                label.pack(pady=(30, 10)) #ย่อมาจาก padding y-axis คือการกำหนด ระยะห่างในแนวตั้ง (บน-ล่าง)

                text_reply_button = tk.Button(
                    self.container,
                    text="Text Reply",
                    command=self.run_text_reply,  
                    width=20,
                    height=2,
                )
                text_reply_button.pack()

                reply_email_button = tk.Button(
                    self.container,
                    text="Reply Email",
                    command=self.run_mail_reply,  
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

                policy_ui_button = tk.Button(
                    self.container,
                    text="Policy Moving",
                    command=self.open_policy_ui,
                    width=20,
                    height=2,
                )
                policy_ui_button.pack()

    def create_text_reply_page(self):
        label = tk.Label(self.container, text="Text Reply", font=("Arial", 16, "bold"))
        label.pack(expand=True)

        back_button = tk.Button(self.container, text="Back", command=lambda: self.show_page("home"))
        back_button.pack(pady=10)


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

    def create_policy_ui_home_page(self):
        label = tk.Label(self.container, text="Policy UI Home", font=("Arial", 16, "bold"))
        label.pack(expand=True)
         
        back_button = tk.Button(self.container, text="Back", command=lambda: self.show_page("policy_ui_home"))
        back_button.pack(pady=10)


if __name__ == "__main__":
    app = AppUI()
    app.mainloop()
