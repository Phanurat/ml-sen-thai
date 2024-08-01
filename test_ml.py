import pandas as pd

# สร้าง DataFrame
data = {
    'ราคา': [3000000, 2500000, 4000000],
    'พื้นที่': [100, 80, 120],
    'จำนวนห้องนอน': [3, 2, 4],
    'ทำเลที่ตั้ง': ['ใจกลางเมือง', 'ชานเมือง', 'ใจกลางเมือง']
}
df = pd.DataFrame(data)

# บันทึกเป็นไฟล์ CSV
df.to_csv('test_data/data.csv', index=False)
