from pythainlp import word_tokenize

text = "ศาลรัฐธรรมนูญจะชี้ชะตา คดีถอดถอนนายเศรษฐา ทวีสิน ออกจากตำแหน่งนายกรัฐมนตรี จากเรื่องที่อดีต 40 สว. ร้อง กรณี การแต่งตั้งนายพิชิต ชื่นบาน เป็นรัฐมนตรี ทั้งๆที่รู้ว่า นายพิชิต เคยมีคดีทนายถุงขนม ซึ่งนายเศรษฐา"
tokens = word_tokenize(text)

attack_ps = ["ก้าวไกล", "พิธา", "ด้อมส้ม", "สามกีบ"]
protect_ps = ["รัฐบาล", "นายก", "เศรษฐา", "เพื่อไทย"]

print(tokens)

for token in tokens:
    for att in attack_ps:
        if token == att:
            found_gaw_glai = True
            # ตรวจสอบเงื่อนไขเกี่ยวกับ "ก้าวไกล"
            if att not in tokens:
                print(f"ด่า{att}ไม่เกี่ยวกับรัฐบาล")
            else:
                print(f"ด่า{att}ปกป้องรัฐบาล")
            exit()

    for prot in protect_ps:    
        if token == prot:
            found_rut_thabaan = True
            # ตรวจสอบเงื่อนไขเกี่ยวกับ "รัฐบาล"
            if "ก้าวไกล" not in tokens:
                print("ปกป้องรัฐบาลอย่างเดียว")
            else:
                print("ชื่นชมรัฐบาลแซะก้าวไกล")
            exit()
