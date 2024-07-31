import pandas as pd

# โหลดข้อมูลจากไฟล์ CSV
data = pd.read_csv('data/test.csv')
print(data.head())
