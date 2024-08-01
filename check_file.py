import os

def check_and_write_file(file_path, text_to_append):
    # เช็คว่าไฟล์มีอยู่หรือไม่
    if os.path.exists(file_path):
        # ถ้ามีไฟล์อยู่แล้ว ให้เปิดไฟล์ในโหมด append ('a')
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(text_to_append + '\n')
            print(f"Appended to the file: {file_path}")
    else:
        # ถ้าไม่มีไฟล์ ให้สร้างไฟล์ใหม่และเขียนข้อมูลลงไปในโหมด write ('w')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_to_append + '\n')
            print(f"Created and wrote to the file: {file_path}")

# ตัวอย่างการใช้งาน
file_path = 'example.txt'
text_to_append = 'This is a new line of text.'

check_and_write_file(file_path, text_to_append)
