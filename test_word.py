from pythainlp import word_tokenize

text = "ในวันนี้ นายกรัฐมนตรีคนไทยของประเทศไทยได้ประชุมกับผู้นำของประเทศญี่ปุ่น"
tokens = word_tokenize(text)

pos = "pos"
folder = "data/"

# สร้างชื่อไฟล์
filename = 'test_data.csv'

# เปิดไฟล์ในโหมด 'w' (เขียนทับ)
with open(folder + filename, 'w', encoding='utf-8') as file:
    # เขียนหัวตาราง
    file.write("text,label\n")
    
    # ตัวแปรเพื่อตรวจสอบว่าพบคำที่ต้องการหรือไม่
    found = False
    
    # ใช้ลูป for เพื่อค้นหาคำที่ต้องการ
    for token in tokens:
        if token == "นายกรัฐมนตรี":
            print(token)
            
            # เขียนข้อมูลลงในไฟล์
            file.write(f"{text},{pos}\n")
            found = True
    
    # ถ้าไม่พบคำที่ต้องการ ให้พิมพ์ข้อความ
    if not found:
        print("ไม่มีคำที่ต้องการ")

print(f'ไฟล์ {folder + filename} ถูกเขียนทับเรียบร้อยแล้ว')
