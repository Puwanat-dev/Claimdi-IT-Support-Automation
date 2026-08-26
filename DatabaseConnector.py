import pymysql

class SimpleDB:
    import pymysql  # ตัวอย่างไลบรารีสำหรับ MySQL

class MySQLDB:
    # 1. รับค่า Username, Password, Host เข้ามาที่ __init__
    def __init__(self, host, user, password, db_name):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.connection = None

    def connect(self):
        # 2. นำค่ามาใส่ตรงนี้เพื่อเชื่อมต่อ
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db_name
        )

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

    def execute(self, query, params=()):
        """Use this for CREATE, INSERT, UPDATE, or DELETE."""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()  # Save changes to the database

    def fetch_all(self, query, params=()):
        """Use this to SELECT multiple rows from a table."""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()  # Returns a list of tuples


if __name__ == "__main__":
        # 1. สร้างออบเจกต์ (ปรับค่าให้ตรงกับเครื่องของคุณ)
    db = MySQLDB(host="localhost", user="root", password="admin", db_name="claimdiemail")

    try:
        # 2. ลองเชื่อมต่อ
        db.connect()
        print("✅ เชื่อมต่อ Database สำเร็จ!")
        
        # 3. ลองดึงค่าทดสอบ (สั่ง SELECT 1)
        result = db.fetch_all("SELECT 1")
        print("ผลการทดสอบ:", result)

    except Exception as e:
        # ถ้าเชื่อมต่อไม่ได้ (เช่น รหัสผ่านผิด หรือ Server ไม่ได้เปิด) จะวิ่งมาตรงนี้
        print("❌ เชื่อมต่อไม่สำเร็จ:", e)

    finally:
        # 4. ปิดการเชื่อมต่อเสมอ
        db.close()