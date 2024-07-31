from pythainlp import word_tokenize

text = "ก้าวไกลด่าการแจกเงินหมื่นดิจิทัลวอลเล็ตของรัฐบาล"
tokens = word_tokenize(text)

print(tokens)

for token in tokens:
    if token == "ก้าวไกล":
        found_gaw_glai = True
        # ตรวจสอบเงื่อนไขเกี่ยวกับ "ก้าวไกล"
        if "รัฐบาล" not in tokens:
            print("ด่าก้าวไกลไม่เกี่ยวกับรัฐบาล")
        else:
            print("ด่าก้าวไกลปกป้องรัฐบาล")
        exit()
    
    if token == "รัฐบาล":
        found_rut_thabaan = True
        # ตรวจสอบเงื่อนไขเกี่ยวกับ "รัฐบาล"
        if "ก้าวไกล" not in tokens:
            print("ปกป้องรัฐบาลอย่างเดียว")
        else:
            print("ชื่นชมรัฐบาลแซะก้าวไกล")
        exit()
