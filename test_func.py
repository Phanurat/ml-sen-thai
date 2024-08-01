from pythainlp import word_tokenize

text = "ในเดือนสิงหาคมนี้ มีปรากฏการณ์ทางการเมือง 3 เรื่องที่น่าจับตา ทั้ง คดียุบพรรคก้าวไกล คดีถอดถอนนายกฯ และ การพ้นโทษของ“ทักษิณ"
tokens = word_tokenize(text)

attack_ps = ["ก้าวไกล", "พิธา", "ด้อมส้ม", "สามกีบ", "พรรคก้าวไกล"]
protect_ps = ["รัฐบาล", "นายก", "เศรษฐา", "เพื่อไทย","นายกฯ", "ทักษิณ"]

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
            print(f"ด่า{token}ไม่เกี่ยวกับรัฐบาล")

        #elif {protect_ps[5]} == 
        else:
            print(f"ด่า{token}ปกป้องรัฐบาล")
        # ไม่ออกจากลูปที่นี่เพื่อให้ตรวจสอบคำถัดไปด้วย
        exit()

    if token in protect_ps:
        found_rut_thabaan = True
        # ตรวจสอบเงื่อนไขเกี่ยวกับ "รัฐบาล"
        if "ก้าวไกล" not in tokens:
            print("ปกป้องรัฐบาลอย่างเดียว")
        else:
            print("ชื่นชมรัฐบาลแซะก้าวไกล")
        # ไม่ออกจากลูปที่นี่เพื่อให้ตรวจสอบคำถัดไปด้วย
        exit()
