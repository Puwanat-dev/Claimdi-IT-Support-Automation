from App_UI import App_UI
from ImagePacker import ImagePacker
from Input_Window import Input_Window


def handle_start_process(app_instance):
    """ฟังก์ชันตัวกลางสำหรับควบคุม Workflow เมื่อผู้ใช้กดปุ่มใน App_UI"""
    # 1. เรียกเปิด Input_Window โดยส่ง app_instance (App_UI) เป็น parent
    input_dialog = Input_Window(parent_window=app_instance)
    pic_path = input_dialog.getPath()

    # 2. ถ้าผู้ใช้ป้อน path มา ให้เริ่มทำงาน ImagePacker
    if pic_path:
        print(f"กำลังประมวลผลภาพจาก: {pic_path}")

        # ส่ง pic_path ไปประมวลผลต่อที่ ImagePacker
        packer = ImagePacker(pic_path)
        packer.process()

        return True  # คืนค่า True เพื่อบอก App_UI ให้เปลี่ยนไปหน้า "hello"
    else:
        print("ผู้ใช้ยกเลิกการใส่ Path")
        return False  # คืนค่า False ไม่เปลี่ยนหน้า


if __name__ == "__main__":
    # ส่งฟังก์ชัน handle_start_process เป็น callback เข้าไปใน App_UI
    app = App_UI(on_start_process=handle_start_process) #การเขียน on_start_process=handle_start_process คือการส่งฟังก์ชัน handle_start_process ไปเป็น callback ให้กับ App_UI เมื่อผู้ใช้กดปุ่มในหน้า home ของ App_UI จะเรียกใช้ฟังก์ชัน handle_start_process
    app.mainloop()