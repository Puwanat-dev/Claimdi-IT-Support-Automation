
class ReadConfig:
    def __init__(self, filename):
        self.filename = filename

    def read_variable(self, variable_name):  # Fix
        with open(self.filename, "r", encoding="utf-8") as file:  # Fix
            for line in file:
                line = line.strip()

                if line.startswith(variable_name + " ="):
                    value = line.split("=", 1)[1].strip()

                    # ถ้าเป็นข้อความที่อยู่ใน "..."
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]

                    return value

        return None

if __name__ == "__main__":

    config = ReadConfig("config.txt")
    it_support_name = config.read_variable("it_support_name")
    it_support_phone = config.read_variable("it_support_phone")
    print(f"""เรียน แผนกตรวจสภาพ

ขอนำส่งข้อมูลไฟล์รูปภาพงานตรวจสภาพ รายละเอียดตามไฟล์แนบ
รบกวนตรวจสอบอีกครั้งว่าตรงตามที่ทางลูกค้ารีเควสหรือไม่ ขอบคุณครับ

Best Regards,
{it_support_name}
IT Support
Anywhere 2 go Co.,Ltd.
520 Dindaeng Rd., Bangkok 10400, Thailand
Tel: {it_support_phone}
""")
    
