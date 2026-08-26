import os
import shutil
import zipfile

# --- Class definition --- (ใหม่)
class ImagePacker: 
    """คลาสสำหรับการคัดลอกและบีบอัดโฟลเดอร์รูปภาพ""" 

    def __init__(self, pic_storage_domain): 
        
        

        # --- Configuration ---
        domain_check = pic_storage_domain[7:11].lower()  # ดึง 3 ตัวอักษรแรกออกมาเช็ค (และใช้ .lower() กันเรื่องตัวพิมพ์ใหญ่)
        if "opi" in domain_check:

            if pic_storage_domain[58] == "/":
                self.relative_path = pic_storage_domain[48:77] 
                self.folder_name = pic_storage_domain[59:77]
            else :
                self.relative_path = pic_storage_domain[48:78] 
                self.folder_name = pic_storage_domain[60:78]
        elif "pic" in domain_check:
            self.relative_path = pic_storage_domain[45:75] 
            self.folder_name = pic_storage_domain[57:75]
        else:
            raise ValueError("Wrong path")  # Raise an error if the prefix is neither "pic" nor "opi"

        
        self.source_base = r"P:\pic.claimdi.com\bike\ImageInspection" 
        self.desktop = os.path.join(os.path.expanduser("~"), "Desktop")  # Note : os.path.expanduser("~") คือคำสั่งที่จะคืนค่าเป็น home directory เช่น C:\Users\Zee
                                                                        # Note : พอมี os.path.join มาด้วยก็จะกลายเป็น C:\Users\Zee\Desktop

        # --- Paths ---
        self.source_folder = os.path.join(self.source_base, self.relative_path) #เอา path ของโฟลเดอร์ต้นทางมารวมกับ path ที่ผู้ใช้ป้อนเข้ามา
        self.destination_folder = os.path.join(self.desktop, self.folder_name) #สร้าง โฟลเดอร์บน Desktop
        self.zip_output = os.path.join(self.desktop, f"{self.folder_name}.zip") 

    def process(self): 
        
        # --- Step 1: Copy folder to Desktop ---
        print(f"Copying '{self.folder_name}' to Desktop...")
        if os.path.exists(self.destination_folder):
            shutil.rmtree(self.destination_folder)               # Remove if already exists
                                                            # Note shutil.rmtree() คือ ลบโฟลเดอร์ พร้อมไฟล์ทั้งหมดด้านใน ⚠️ เป็นคำสั่งที่แรงมาก เพราะลบถาวร
        shutil.copytree(self.source_folder, self.destination_folder)  #shutil.copytree() จะคัดลอกโฟลเดอร์ทั้งโครงสร้าง โดย Para1 จะถูกคัดลอกไปเป็น Para2

        # --- Step 2: Zip the folder ---
        print(f"Zipping folder into '{self.folder_name}.zip'...") 
        with zipfile.ZipFile(self.zip_output, "w", zipfile.ZIP_DEFLATED) as zipf:    # Note : "w" = mode write : new file
                                                                                # Note : ZIP_DEFLATED is standard algorithm to compress
                                                                                # Note : with > auto close file when process completed
            for root, dirs, files in os.walk(self.destination_folder):               
                                                                                # Note : root คือ path ของโฟลเดอร์ปัจจุบัน
                                                                                # Note : dits คือ list ของโฟลเดอร์ย่อย
                                                                                # Note : files คือ ไฟล์ในโฟลเดอร์นั้น
                                                                                # Note : คำสั่งนี้จะลงลึกทุก Subfolder
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, self.desktop)               # Note : relpath จะตัด path ส่วนแรกๆที่ไม่จำเป็นออก ให้เหลือแต่โฟลเดอร์ใหญ่ของมันกับไฟล์ด้านใน เพื่อให้ไฟล์ที่แตกออกมามีโครงสร้างที่ไม่ผิดปกติ
                    zipf.write(file_path, arcname)

        print(f"Zip created at: {self.zip_output}") 

        # --- Step 3: Remove the unzipped copy (optional) ---
        shutil.rmtree(self.destination_folder) 
        print("Done! Temporary folder removed.")


# --- Main Execution --- 
if __name__ == "__main__": 
    # UI
    print("Input the Picture path")
    relative_path = input("Input : ")

    # Create Object & Run Process (ใหม่)
    packer = ImagePacker(relative_path) 
    packer.process() 