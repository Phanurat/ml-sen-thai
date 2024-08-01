from pythainlp import word_tokenize
import random

text = "พิธา-ชัยธวัช เตรียมจับมือแถลงแนวทางสู้คดีโค้งสุดท้าย 2 ส.ค. ด้าน ไอติม ขออย่าด่วนสรุปก้าวไกลจะโดนยุบ ยันไม่ถอดใจ ยังเดินหน้าทำงานต่อ"
tokens = word_tokenize(text)

file_attack = "who/attack_ps.txt"
file_protect = "who/protect_ps.txt"
file_attack_file = "attack_file/attack_file.txt"
file_protect_file = "protect_file/protect_file.txt"


print("Tokens:", tokens)
print("Text Content:", text)

# โหลดข้อมูลจากไฟล์
with open(file_attack, 'r', encoding='utf-8') as file:
    who_attack = [line.strip() for line in file]

with open(file_protect, 'r', encoding='utf-8') as file:
    who_protect = [line.strip() for line in file]

# ตัวแปรสำหรับตรวจสอบคำที่พบ
found_gaw_glai = False
found_rut_thabaan = False

# ตรวจสอบคำใน tokens
for token in tokens:
    if any(token in attacker for attacker in who_attack):
        found_gaw_glai = True
        # ตรวจสอบเงื่อนไขเกี่ยวกับ "ก้าวไกล"
        if "รัฐบาล" not in tokens:
            print(f"ด่า {token} ไม่เกี่ยวกับรัฐบาล")

            with open(file_attack_file, 'r', encoding='utf-8') as file:
                attr = file.readlines()
                if attr:
                    attr_rand = random.sample(attr, min(10, len(attr)))
                    for attack in attr_rand:
                        print(attack.strip())
                
                else:
                    print("File unvarieble")
        else:
            print(f"ด่า {token} ปกป้องรัฐบาล")
        # ออกจากลูปเพื่อไม่ให้ตรวจสอบคำถัดไป
        break
    
    if any(token in protector for protector in who_protect):
        found_rut_thabaan = True
        # ตรวจสอบเงื่อนไขเกี่ยวกับ "รัฐบาล"
        if "ก้าวไกล" not in tokens:
            print("ปกป้องรัฐบาลอย่างเดียว")
            with open(file_protect_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:  # ตรวจสอบว่าไฟล์ไม่ว่าง
                    lines_rand = random.sample(lines, min(10, len(lines)))  # เลือกบรรทัดสุ่ม 10 บรรทัด
                    for line_rand in lines_rand:
                        print(line_rand.strip())  # แสดงบรรทัดที่สุ่มเลือก
                else:
                    print("ไฟล์ว่างเปล่า")
        else:
            print("ชื่นชมรัฐบาลแซะก้าวไกล")
            
        # ออกจากลูปเพื่อไม่ให้ตรวจสอบคำถัดไป
        break
