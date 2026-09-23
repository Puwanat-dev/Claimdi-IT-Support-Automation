from app_ui import App_UI
from image_packer import ImagePacker
from input_window import Input_Window
from mail_script import Mail_Answer


def handle_mail_reply(app_instance):
    mail_answer = Mail_Answer()
    mail_answer.root.mainloop()
    return True


def handle_start_process(app_instance):
    
    
    input_dialog = Input_Window(parent_window=app_instance)
    pic_path = input_dialog.getPath()

    
    if pic_path:
        print(f"กำลังประมวลผลภาพจาก: {pic_path}")

        
        packer = ImagePacker(pic_path)
        packer.process()

        return True  
    else:
        print("ผู้ใช้ยกเลิกการใส่ Path")
        return False  


if __name__ == "__main__":
    
    app = App_UI(mail_reply_start_process=handle_mail_reply, image_pack_start_process=handle_start_process)
    app.mainloop()