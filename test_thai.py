import spacy

# โหลดโมเดลภาษาไทย
nlp = spacy.load('th_core_news_sm')

# ข้อความที่ต้องการตรวจสอบ
text = "ในวันนี้ นายกรัฐมนตรีของประเทศไทยได้ประชุมกับผู้นำของประเทศญี่ปุ่น"

# ประมวลผลข้อความ
doc = nlp(text)

# แสดงผลลัพธ์
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")
