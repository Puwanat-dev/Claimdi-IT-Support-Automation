#x = "https://pic.claimdi.com/bike/ImageInspection/2024/Aug/30/CLM-INS-2408177320/PT04/f6a44528-29c7-4c0f-a89b-f46c1a77423c.Jpeg"  # ตัวแปรโดเมน
#x = "http://opic.claimdi.com:82/bike/ImageInspection/2022/Sep/22/CLM-INS-2209216866/PT04/be4ac6ac-e84c-4232-8a44-0243ff1d53b3.Jpeg"
x = "http://opic.claimdi.com:82/bike/ImageInspection/2022/Oct/3/CLM-INS-2209224186/PT04/ff23425a-177a-4516-a0a5-ada5812e1189.Jpeg"

# ดึง 3 ตัวอักษรแรกออกมาเช็ค (และใช้ .lower() กันเรื่องตัวพิมพ์ใหญ่)
prefix = x[7:11].lower()
print(prefix)

if "opi" in prefix :
    if x[58] == "/":
            # ทำงานแบบที่ 1.1
            print(x[48:77]) #ใช้ในการค้น
            print(print(x[59:77]))
            

    else: 
        print(x[48:78]) #ใช้ในการค้น
        print(print(x[60:78]))
     #ใช้ในการตั้งชื่อ



elif "pic" in prefix:
    # ทำงานแบบที่ 2
    print(x[45:75]) #ใช้ในการค้น
    print(x[57:75]) #ใช้ในการตั้งชื่อ

else:
    print("3 ตัวแรกไม่ใช่ทั้ง pic และ opi")