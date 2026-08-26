from App_UI import App_UI
from ImagePacker import ImagePacker
from Input_Window import Input_Window


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
    
    app = App_UI(on_start_process=handle_start_process) 
    app.mainloop()