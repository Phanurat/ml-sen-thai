import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from pythainlp.tokenize import word_tokenize
import os

# ฟังก์ชันสำหรับการตัดคำในภาษาไทย
def tokenize(text):
    return ' '.join(word_tokenize(text))

# กำหนดเส้นทางไฟล์
base_path = os.path.dirname(__file__)
old_data_path = os.path.join(base_path, '../data/old_data.csv')
new_data_path = os.path.join(base_path, '../data/new_data.csv')

# 1. โหลดข้อมูลเก่าและข้อมูลใหม่
old_data = pd.read_csv(old_data_path)
new_data = pd.read_csv(new_data_path)

# รวมข้อมูลเก่าและใหม่
data = pd.concat([old_data, new_data], ignore_index=True)

# 2. ตัดคำและแยกข้อมูล
data['text'] = data['text'].apply(tokenize)
X = data['text']  # ข้อความ
y = data['label']  # ป้ายกำกับ

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. โหลดเวกเตอร์ของข้อมูลที่บันทึกไว้ หรือฝึกเวกเตอร์ใหม่
try:
    vectorizer = joblib.load(os.path.join(base_path, '../model/vectorizer.pkl'))
except FileNotFoundError:
    vectorizer = CountVectorizer()
    vectorizer.fit(X_train)
    joblib.dump(vectorizer, os.path.join(base_path, '../model/vectorizer.pkl'))

# แปลงข้อความเป็นตัวเลข
X_train_vectors = vectorizer.transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

# 4. โหลดโมเดลที่บันทึกไว้ หรือสร้างโมเดลใหม่
try:
    model = joblib.load(os.path.join(base_path, '../model/model.pkl'))
except FileNotFoundError:
    model = MultinomialNB()

# ฝึกโมเดลใหม่ด้วยข้อมูลทั้งหมด
model.fit(X_train_vectors, y_train)

# 5. ทดสอบโมเดล
y_pred = model.predict(X_test_vectors)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print('Classification Report:')
print(classification_report(y_test, y_pred))

# 6. บันทึกโมเดลและเวกเตอร์
joblib.dump(model, os.path.join(base_path, '../model/model.pkl'))
