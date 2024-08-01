from pythainlp import word_tokenize
import random

text = "นายกฯ เตรียมเชิญหน่วยงานปราบยาเสพติดสหรัฐ ลงพื้นที่ภาคเหนือสิ้นเดือนนี้ ร่วมมือแก้ปัญหายาเสพติด"
tokens = word_tokenize(text)

attack_ps = ["ก้าวไกล", "พิธา", "ด้อมส้ม", "สามกีบ", "พรรคก้าวไกล"]
protect_ps = ["รัฐบาล", "นายก", "เศรษฐา", "เพื่อไทย", "นายกฯ", "ทักษิณ", "ทางรัฐ"]

print("Tokens:", tokens)

# ตัวแปรสำหรับตรวจสอบคำที่พบ
found_gaw_glai = False
found_rut_thabaan = False

# ตรวจสอบคำใน tokens
for token in tokens:
    if token in attack_ps:
        found_gaw_glai = True
        # ตรวจสอบเงื่อนไขเกี่ยวกับ "ก้าวไกล"
        if "รัฐบาล" not in tokens:
            print(f"ด่า {token} ไม่เกี่ยวกับรัฐบาล")
        else:
            print(f"ด่า {token} ปกป้องรัฐบาล")
        # ไม่ออกจากลูปที่นี่เพื่อให้ตรวจสอบคำถัดไปด้วย
        break

    if token in protect_ps:
        found_rut_thabaan = True
        # ตรวจสอบเงื่อนไขเกี่ยวกับ "รัฐบาล"
        if "ก้าวไกล" not in tokens:
            print("ปกป้องรัฐบาลอย่างเดียว")
            files_protect = "protect_file/protect_file.txt"
            with open(files_protect, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:  # ตรวจสอบว่าไฟล์ไม่ว่าง
                    lines_rand = random.sample(lines, min(20, len(lines)))  # เลือกบรรทัดสุ่ม 10 บรรทัด
                    for line_rand in lines_rand:
                        print(line_rand.strip())  # แสดงบรรทัดที่สุ่มเลือก
                else:
                    print("ไฟล์ว่างเปล่า")
        else:
            print("ชื่นชมรัฐบาลแซะก้าวไกล")
            
        # ไม่ออกจากลูปที่นี่เพื่อให้ตรวจสอบคำถัดไปด้วย
        break
