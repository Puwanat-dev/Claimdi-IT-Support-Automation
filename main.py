from app_ui import AppUI
from image_packer import ImagePacker
from input_window import Input_Window
from mail_script import MailScript
from text_script import TextScript


def handle_mail_reply(app_instance):
    mail_answer = MailScript()
    mail_answer.root.mainloop()
    return True


def handle_text_reply(app_instance):
    text_script = TextScript()
    text_script.root.mainloop()
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
    
    app = AppUI(text_reply_start_process=handle_text_reply, mail_reply_start_process=handle_mail_reply, image_pack_start_process=handle_start_process)
    app.mainloop()